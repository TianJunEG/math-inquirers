-- Math Inquirers portal: grants + row level security. Run AFTER schema.sql.
-- Supabase grants ALL on new public tables/functions to anon/authenticated by default, so everything is revoked first
-- and re-granted narrowly. Direct writes are NOT granted at all except parents.full_name/phone: every write goes
-- through a SECURITY DEFINER function in schema.sql (PIN hashing, capacity, consent and admin checks live there).

alter table public.parents           enable row level security;
alter table public.children          enable row level security;
alter table public.groups            enable row level security;
alter table public.enrolments        enable row level security;
alter table public.payments          enable row level security;
alter table public.consents          enable row level security;
alter table public.practice_attempts enable row level security;
alter table public.admins            enable row level security;   -- no policy, no grant: only is_admin() (definer) reads it
alter table public.deletion_requests enable row level security;   -- no policy, no grant

revoke all on all tables    in schema public from anon, authenticated;
revoke all on all sequences in schema public from anon, authenticated;
revoke all on all functions in schema public from public, anon, authenticated;

-- ---- table privileges (RLS then filters rows) ----
grant select on public.groups to anon, authenticated;
grant select (id, email, full_name, phone, family_code, created_at) on public.parents to authenticated;
grant update (full_name, phone) on public.parents to authenticated;
-- children: the PIN hash and lockout counters are never selectable by a client
grant select (id, parent_id, display_name, level, created_at, updated_at) on public.children to authenticated;
grant select on public.enrolments, public.payments, public.consents, public.practice_attempts to authenticated;

-- ---- policies ----
create policy groups_read on public.groups for select to anon, authenticated using (active);

create policy parents_own_select on public.parents for select to authenticated using (id = auth.uid() or public.is_admin());
create policy parents_own_update on public.parents for update to authenticated
  using (id = auth.uid() and deleted_at is null) with check (id = auth.uid() and deleted_at is null);

create policy children_own_select on public.children for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy enrolments_own_select on public.enrolments for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy payments_own_select on public.payments for select to authenticated using (
  public.is_admin() or exists (select 1 from public.enrolments e where e.id = payments.enrolment_id and e.parent_id = auth.uid()));

create policy consents_own_select on public.consents for select to authenticated using (parent_id = auth.uid() or public.is_admin());

create policy attempts_own_select on public.practice_attempts for select to authenticated using (
  public.is_admin() or exists (select 1 from public.children c where c.id = practice_attempts.child_id and c.parent_id = auth.uid()));

-- ---- function execute grants ----
grant execute on function public.is_admin()                                   to authenticated;   -- used inside policies
grant execute on function public.add_child(text, int, text)                   to authenticated;
grant execute on function public.update_child(uuid, text, int, text)          to authenticated;
grant execute on function public.delete_child(uuid)                           to authenticated;
grant execute on function public.record_consents(jsonb, text, text)           to authenticated;
grant execute on function public.my_consents()                                to authenticated;
grant execute on function public.enrol_child(uuid, text)                      to authenticated;
grant execute on function public.cancel_my_enrolment(uuid)                    to authenticated;
grant execute on function public.my_enrolments()                              to authenticated;
grant execute on function public.group_fill()                                 to authenticated;
grant execute on function public.delete_my_data()                             to authenticated;
grant execute on function public.admin_list_enrolments()                      to authenticated;   -- checks is_admin() inside
grant execute on function public.admin_mark_paid(uuid, text)                  to authenticated;
grant execute on function public.admin_cancel_enrolment(uuid, text)           to authenticated;
grant execute on function public.child_sign_in(text, text, text)              to anon, authenticated;
grant execute on function public.service_begin_payment(uuid, uuid)                      to service_role;
grant execute on function public.service_attach_session(uuid, text)                     to service_role;
grant execute on function public.service_mark_paid(uuid, text, text, int, text)         to service_role;
grant execute on function public.service_mark_session_failed(uuid, text)                to service_role;
grant execute on function public.expire_unpaid_reservations(int)                        to service_role;
-- _require_parent(), gen_code(), forbid_mutation(), handle_new_user() are internal: not granted to any API role.
-- service_role bypasses RLS but its table privileges are untouched by the revokes above.
