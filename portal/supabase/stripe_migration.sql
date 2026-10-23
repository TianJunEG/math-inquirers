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
--   4. The manual PayNow route (admin_mark_paid, method 'paynow_manual') is untouched.

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

-- Idempotent. Returns: paid | already_paid | paid_enrolment_cancelled | amount_mismatch | currency_mismatch | not_found
-- A mismatch changes nothing: the owner sees it in the Cloudflare log and handles it by hand.
create or replace function public.service_mark_paid(p_payment uuid, p_session_id text, p_payment_intent text, p_amount_cents int, p_currency text)
returns text language plpgsql security definer set search_path = public as $$
declare pay public.payments; est text;
begin
  select p.* into pay from public.payments p where p.id = p_payment for update;
  if not found then return 'not_found'; end if;
  if pay.status = 'paid' then return 'already_paid'; end if;
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
  return 'paid_enrolment_cancelled';   -- money arrived for a cancelled enrolment: owner must refund by hand
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
