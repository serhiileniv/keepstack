# Evals

One eval per artifact. Required before `status: verified` — an artifact we cannot re-test is an
artifact we cannot honour the maintenance promise on, and the promise is the business
([validation.md](../../docs/validation.md), Gate C).

## The fixture repository

Gate C compares runs across months. That only works if the input never changes, so every
codebase eval runs against **one pinned open-source repository**, not against a client system.

**Selection criteria** (pin once, then never change it — changing the fixture resets the
history):

- 50k–200k LOC. Small enough to run monthly, large enough that orientation is non-trivial.
- More than one language or service, and a real datastore.
- A genuine revenue-shaped path — checkout, subscription, billing, ingestion — so `wf-0001`
  step 5 has something to trace.
- At least one thing that is genuinely absent (no integration tests, an unversioned migration,
  an undocumented cron), so `dec-0003`'s absence-claim test has a real answer.
- Permissively licensed and public, so worked examples can quote it.

**Pinned fixture:** `FIXTURE_REPO` = _to set at first Gate A run_ · `FIXTURE_SHA` = _to set_

Record both here the first time an eval runs, and treat them as immutable afterwards. A second
fixture may be added later; the first is never replaced.

## Run rules

- **Fresh session, every time.** No prior context, no author hand-holding. A run that needed a
  nudge is a fail, and the nudge is the finding.
- **Two models**, one frontier and one cheaper, recorded in `verified_against`.
- **Record the run even when it passes.** The run log is the maintenance audit trail and the
  receipt when a customer asks whether we actually update this.
- **A fail flips `status: stale` the same day**, before the fix. See
  [validation.md](../../docs/validation.md) Gate C.

## What an eval for a *decision* tests

Not "is the advice good" — that is not testable in a session. An eval for a decision tests its
**expiry trigger**: has the world changed in the specific way that would make the call wrong?
Each decision eval below reduces that to something checkable in under 30 minutes.
