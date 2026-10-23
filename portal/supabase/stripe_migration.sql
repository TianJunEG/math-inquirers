-- stripe_migration.sql  (22-23 Oct 2026)   REVIEW FIRST. NOT APPLIED to any database yet.
-- Owner decision: the payment gateway is Stripe, replacing HitPay. Run once in the Supabase SQL editor on the existing project
-- (after schema.sql / policies.sql / finish_setup.sql). Idempotent: safe to re-run. A fresh install from schema.sql + policies.sql
-- already contains all of this, so a fresh install does not need this file.
--
-- What it does
--   1. payments: `method` is the provider ('paynow_manual' | 'stripe' | 'hitpay' kept for history). New columns:
--      provider_ref (Checkout Session id, cs_...), provider_payment_ref (PaymentIntent id, pi_...), provider_attempt (retry counter
--      that goes into the Stripe idempotency key). Index on provider_ref.
--   2. New service_role-only functions: service_begin_payment, service_attach_session, service_mark_paid (amount in cents AND currency
--      checked, idempotent), service_mark_session_failed.
--   3. DROPS the three HitPay functions (nothing calls them any more). The columns hitpay_payment_request_id / hitpay_payment_id are
--      KEPT (empty until anything was ever paid via HitPay; none was) so no data can be lost; drop them later if you wish:
--        alter table public.payments drop column hitpay_payment_request_id, drop column hitpay_payment_id;
--   4. service_mark_paid now flags duplicate/late payments and never flips refunded/failed back to paid; unpaid reservations expire
--      (_expire_stale_reservations, expire_unpaid_reservations, enrol_child replaced).
--   5. The manual PayNow route (admin_mark_paid, method 'paynow_manual') is untouched.

begin;

alter table public.payments add column if not exists provider_ref         text;
alter table public.payments add column if not exists provider_payment_ref text;
alter table public.payments add column if not exists provider_attempt     int not null default 0;

alter table public.payments drop constraint if exists payments_method_check;
alter table public.payments add  constraint payments_method_check check (method in ('paynow_manual','stripe','hitpay'));

create index if not exists payments_provider_ref_idx on public.payments (provider_ref) where provider_ref is not null;

-- HitPay is retired.
drop function if exists public.service_begin_hitpay(uuid, uuid);
drop function if exists public.service_attach_hitpay(uuid, text);
drop function if exists public.service_mark_hitpay_paid(uuid, text, text, int);

-- ---------- Stripe, service-role only (Cloudflare Functions) ----------
-- Look up a payable enrolment for a parent (the Cloudflare Function has already verified the parent's JWT).
-- Returns the payment id, the amount agreed at reservation (payments.amount_cents, copied from groups.fee_cents when the seat was reserved),
-- the group's current fee_cents (for logging; the function charges amount_cents), and the retry counter used in the Stripe idempotency key.
create or replace function public.service_begin_payment(p_enrolment uuid, p_parent uuid)
returns table (payment_id uuid, amount_cents int, currency text, group_fee_cents int, group_name text, reference text,
               payment_status text, enrolment_status text, parent_email text, parent_name text, attempt int)
language sql stable security definer set search_path = public as $$
  select p.id, p.amount_cents, p.currency, g.fee_cents, g.name, p.reference, p.status, e.status, pa.email, pa.full_name, p.provider_attempt
    from public.enrolments e
    join public.payments p on p.enrolment_id = e.id
    join public.parents pa on pa.id = e.parent_id
    join public.groups g on g.id = e.group_id
   where e.id = p_enrolment and e.parent_id = p_parent;
$$;

-- Remember which Checkout Session belongs to the payment. Only touches a payment that is still pending.
create or replace function public.service_attach_session(p_payment uuid, p_session_id text) returns void
language sql security definer set search_path = public as $$
  update public.payments set method = 'stripe', provider_ref = p_session_id, updated_at = now()
   where id = p_payment and status = 'pending';
$$;

-- Idempotent. Returns: paid | already_paid | duplicate_payment | not_payable:<status> | paid_enrolment_cancelled | amount_mismatch | currency_mismatch | not_found
--  * duplicate_payment: the payment is already paid by something else (manual PayNow ticked by the admin, or another PaymentIntent). Nothing is
--    changed; the webhook logs NEEDS OWNER ATTENTION so the owner refunds the second payment by hand. A repeat of the SAME PaymentIntent is already_paid.
--  * not_payable:refunded / not_payable:failed: a late event can never turn a refunded (or failed) payment back into paid. Nothing is changed.
--  * paid_enrolment_cancelled: money arrived after the enrolment was cancelled or the unpaid reservation expired (a LATE payment). The payment is
--    recorded as paid and the owner decides: re-open the seat if it is still free, or refund.
-- A mismatch changes nothing: the owner sees it in the Cloudflare log and handles it by hand.
create or replace function public.service_mark_paid(p_payment uuid, p_session_id text, p_payment_intent text, p_amount_cents int, p_currency text)
returns text language plpgsql security definer set search_path = public as $$
declare pay public.payments; est text;
begin
  select p.* into pay from public.payments p where p.id = p_payment for update;
  if not found then return 'not_found'; end if;
  if pay.status = 'paid' then
    if pay.method <> 'stripe' then return 'duplicate_payment'; end if;                                  -- paid by hand (PayNow), now Stripe too
    if p_payment_intent is not null and pay.provider_payment_ref is not null
       and pay.provider_payment_ref <> p_payment_intent then return 'duplicate_payment'; end if;        -- a second, different Stripe payment
    return 'already_paid';
  end if;
  if pay.status not in ('pending', 'cancelled') then return 'not_payable:' || pay.status; end if;       -- refunded / failed never flip back to paid
  if upper(coalesce(p_currency, '')) <> pay.currency then return 'currency_mismatch'; end if;
  if pay.amount_cents <> p_amount_cents then return 'amount_mismatch'; end if;
  update public.payments set status = 'paid', method = 'stripe', paid_at = now(),
         provider_ref = coalesce(p_session_id, provider_ref), provider_payment_ref = p_payment_intent, updated_at = now()
   where id = pay.id;
  select status into est from public.enrolments where id = pay.enrolment_id;
  if est = 'pending_payment' then
    update public.enrolments set status = 'confirmed' where id = pay.enrolment_id;
    return 'paid';
  end if;
  return 'paid_enrolment_cancelled';   -- money arrived for a cancelled/expired enrolment: owner must re-open the seat or refund by hand
end $$;

-- Checkout Session expired or an async (PayNow) payment failed: the payment stays 'pending' so the parent can try again,
-- but the session reference is cleared and the retry counter moves on so the next attempt gets a fresh idempotency key.
-- Returns: reset | ignored (not pending, or a different/newer session) | not_found
create or replace function public.service_mark_session_failed(p_payment uuid, p_session_id text) returns text
language plpgsql security definer set search_path = public as $$
declare pay public.payments;
begin
  select p.* into pay from public.payments p where p.id = p_payment for update;
  if not found then return 'not_found'; end if;
  if pay.status <> 'pending' or pay.provider_ref is distinct from p_session_id then return 'ignored'; end if;
  update public.payments set provider_ref = null, provider_attempt = provider_attempt + 1, updated_at = now() where id = pay.id;
  return 'reset';
end $$;

-- Seat reservations expire (new) and enrol_child frees expired ones before counting seats (replaces the live enrol_child; same signature).

-- Unpaid seat reservations expire. A pending_payment enrolment whose payment is still pending after p_days is cancelled (frees the seat).
-- Called (a) inside enrol_child for the group being booked, so no cron is needed, and (b) optionally by a scheduled job as
-- expire_unpaid_reservations(). Default 7 days: OWNER TO CONFIRM (docs/audit_final/open_owner_items.md). A payment that arrives afterwards
-- is recorded and reported as paid_enrolment_cancelled (late payment), never silently lost.
create or replace function public._expire_stale_reservations(p_group text default null, p_days int default 7) returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  with stale as (
    select e.id from public.enrolments e join public.payments p on p.enrolment_id = e.id
     where e.status = 'pending_payment' and p.status = 'pending'
       and e.created_at < now() - make_interval(days => greatest(p_days, 1))
       and (p_group is null or e.group_id = p_group)
     for update of e, p),
  ce as (update public.enrolments e set status = 'cancelled', cancelled_at = now() from stale s where e.id = s.id returning e.id)
  update public.payments p set status = 'cancelled', note = left(coalesce(p.note || ' ', '') || '[reservation expired, unpaid]', 500), updated_at = now()
    from ce where p.enrolment_id = ce.id;
  get diagnostics n = row_count;
  return n;
end $$;

create or replace function public.expire_unpaid_reservations(p_days int default 7) returns int
language sql security definer set search_path = public as $$ select public._expire_stale_reservations(null, p_days); $$;

create or replace function public.enrol_child(p_child uuid, p_group text) returns uuid
language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid := public._require_parent(); ch public.children; g public.groups; eid uuid; ref text; tries int := 0; taken int; missing text;
begin
  select * into ch from public.children where id = p_child and parent_id = uid;
  if not found then raise exception 'not_found'; end if;
  select * into g from public.groups where id = p_group and active for update;   -- row lock serialises seat checks
  if not found then raise exception 'group_not_found'; end if;
  if g.level <> ch.level then raise exception 'level_mismatch'; end if;
  perform public._expire_stale_reservations(g.id);   -- free seats held by unpaid reservations older than 7 days
  if exists (select 1 from public.enrolments where child_id = p_child and status <> 'cancelled') then raise exception 'already_enrolled'; end if;
  select string_agg(t, ',') into missing from unnest(array['contact','terms','recording','childs_work']) t
   where not coalesce((select c.granted from public.consents c where c.parent_id = uid and c.consent_type = t order by c.seq desc limit 1), false);
  if missing is not null then raise exception 'consents_missing:%', missing; end if;
  select count(*) into taken from public.enrolments where group_id = g.id and status <> 'cancelled';
  if taken >= g.seats then raise exception 'group_full'; end if;
  insert into public.enrolments (parent_id, child_id, child_label, group_id) values (uid, ch.id, ch.display_name, g.id) returning id into eid;
  loop
    ref := 'MI-' || public.gen_code(6);
    exit when not exists (select 1 from public.payments where reference = ref);
    tries := tries + 1; if tries > 20 then raise exception 'ref_alloc'; end if;
  end loop;
  insert into public.payments (enrolment_id, reference, amount_cents) values (eid, ref, g.fee_cents);
  return eid;
end $$;

revoke all on function public._expire_stale_reservations(text, int) from public, anon, authenticated;
revoke all on function public.expire_unpaid_reservations(int)             from public, anon, authenticated;
grant execute on function public.expire_unpaid_reservations(int)          to service_role;

revoke all on function public.service_begin_payment(uuid, uuid)                         from public, anon, authenticated;
revoke all on function public.service_attach_session(uuid, text)                        from public, anon, authenticated;
revoke all on function public.service_mark_paid(uuid, text, text, int, text)            from public, anon, authenticated;
revoke all on function public.service_mark_session_failed(uuid, text)                   from public, anon, authenticated;
grant execute on function public.service_begin_payment(uuid, uuid)                      to service_role;
grant execute on function public.service_attach_session(uuid, text)                     to service_role;
grant execute on function public.service_mark_paid(uuid, text, text, int, text)         to service_role;
grant execute on function public.service_mark_session_failed(uuid, text)                to service_role;

commit;

-- Check afterwards (as the SQL editor user):
--   select proname from pg_proc where pronamespace = 'public'::regnamespace and proname like 'service\_%' order by 1;
--   select column_name from information_schema.columns where table_name = 'payments' and column_name like 'provider%';
