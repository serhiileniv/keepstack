# ADR-009 — The Phase 1 twelve

**Status:** Void — the twelve were chosen for the superseded niche. See [ADR-011](ADR-011-niche-change.md).
**Date:** 2026-08-30

## Context

The [niche brief](../customers/niche-fractional-cto.md) listed **15 seed candidates** and
instructed Phase 1.3 to edit them from recall and Phase 1.4 to cut to 12. Two things were wrong
with the list as written:

1. It was a list of **tasks**, and tasks map cleanly to workflows but badly to decisions. Taking
   the top 12 tasks by `time saved × frequency` would have produced 9 workflows and 3 weak
   decisions — the exact failure the brief warns about.
2. It had no artifact for the thing that actually blocks day one: **whether you are allowed to
   put the client's code through an AI tool at all.** Every workflow in the list assumes that
   question is settled, and in practice it is the first thing a client asks.

## Decision

The Phase 1 catalogue is these twelve. Mix matches
[artifact-spec](../artifact-spec.md): **4 decisions, 5 workflows, 3 skills/configs.**

### Decisions — the differentiator

| ID | Title | From |
|---|---|---|
| `dec-0001` | Putting client code through AI tooling — what's allowed, and how to answer when they ask | **new** |
| `dec-0002` | How deep to go in week one before the ramp stops paying for itself | seed #4 |
| `dec-0003` | When to trust an agent's read of a codebase, and when to verify by hand | seed #5 |
| `dec-0004` | Which tech debt to raise with a client, and which to absorb silently | seed #10 |

### Workflows

| ID | Title | From |
|---|---|---|
| `wf-0001` | Unfamiliar-codebase orientation — clone to defensible mental model | seed #1 |
| `wf-0002` | The week-one written assessment | seed #2 |
| `wf-0003` | Risk and tech-debt inventory, severity-ranked | seed #3 |
| `wf-0004` | Monthly stakeholder update — engineering reality to board language | seed #6 |
| `wf-0005` | Build-vs-buy evaluation with a written recommendation | seed #7 |

### Skills and configs

| ID | Title | From |
|---|---|---|
| `skill-0001` | `codebase-cartographer` — the repeatable repo-mapping pass behind `wf-0001` | **new** |
| `skill-0002` | `findings-writer` — engineering findings into founder-readable language | **new** |
| `cfg-0001` | Engagement scaffold — per-client project setup, secret hygiene, tool permissions | **new** |

**Three of the five workflows are week-one work.** That is deliberate: the wedge is week one,
and a wedge product should look lopsided. A catalogue with even coverage across the whole
consulting year would be a worse product, not a better one.

## Cut, and why

| Seed | Task | Why cut |
|---|---|---|
| #8 | ADR from a messy discussion | Genuinely good and genuinely frequent, but it duplicates the *decision* format we are already selling. Better as a free artifact in Phase 2.1 — it demonstrates the format, which is the whole pitch. |
| #9 | Estimate translation | High frequency, but the output is mostly negotiation judgement and only lightly agentic. Weak `outcome` number. First candidate for Phase 3.3. |
| #11 | Technical hiring loop | Episodic. Also drifts toward segment 4 (dev teams) vocabulary — see the overlap risk in [ADR-008](ADR-008-niche.md). |
| #12 | Incident postmortem | Rare per engagement, and when it happens nobody is buying a product mid-incident. |
| #13 | Cloud cost review | Real money, but the work is in vendor consoles, not in a repo. Different tool surface, poor fit with the rest of the bundle. |
| #14 | Migration plan | Very high value, very low frequency, and highly client-specific — the artifact would be generic enough to be worthless. |
| #15 | Exit tooling handover | Deferred to the retention pass. It is an artifact about *ending* engagements, and we have no customers who have finished one yet. |

Cut items are not dead. They are the Phase 3.3 backlog, to be pulled forward **only when a
paying customer asks** for one.

## Reasoning

- **The four decisions were chosen for what cannot be researched**, not for what saves the most
  time. Each one encodes a call the operator has actually made and been wrong about at least
  once. That is the part a competitor cannot copy in an afternoon.
- `dec-0001` is promoted to first artifact because it is a **precondition for every workflow we
  sell**. Shipping the workflows without it means shipping advice that a cautious buyer cannot
  legally follow.
- The two skills are **extracted from** `wf-0001` and `wf-0002` rather than invented. A skill
  that isn't the mechanical core of a workflow we already validated is speculation.
- `cfg-0001` exists because configs "rot fastest" (artifact-spec §1) and therefore best
  demonstrate the maintenance promise. It is the artifact most likely to break first, which
  makes it the best possible advertisement for Gate C.

## Alternatives rejected

| Option | Why not |
|---|---|
| Take the top 12 by `time saved × frequency`, as written | Produces 9 workflows / 3 decisions. Sells the commodity half of the catalogue. |
| Ship 8 and skip the skills/configs | Tempting, and 1.9 explicitly permits it. Rejected because the skills are near-zero marginal cost once the workflows exist, and "directly loadable, zero setup" is the thing that makes a buyer open the file in the first minute rather than never. |
| Write all 15 | Violates the cap logic in [ADR-001](ADR-001-what-we-sell.md) and guarantees the Phase 1 failure mode. |

## Consequences

- The catalogue is week-one-heavy. If Gate M3 conversations say the worst task is stakeholder
  reporting rather than the ramp (an open question in the niche brief), the mix is wrong and
  `wf-0004` becomes the wedge. **Ask before writing `wf-0005`.**
- Seven of the twelve share `wf-0001` as an upstream dependency. That is efficient to build and
  is a **single point of failure for Gate C** — when the orientation pass breaks against a new
  model, most of the catalogue goes stale at once. Accepted, and noted in
  [risks](../risks.md).

## What would reverse this

- Three or more Gate M3 conversations name a task that is not in these twelve.
- A buyer says they would pay for the decisions alone (open question in the niche brief). Then
  the mix shifts further toward decisions and the workflows become the free half.
