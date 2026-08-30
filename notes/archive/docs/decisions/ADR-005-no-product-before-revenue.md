# ADR-005 — No product surface before a stranger pays

**Status:** Accepted
**Date:** 2026-08-30

## Context

The instinct on a project like this is to start building: a searchable vault, accounts,
versioning, team sync, a nice UI. All of it is enjoyable and all of it is a way of avoiding
the actual risk, which is that nobody wants this.

## Decision

Until **Rung 1** (one payment from a stranger), the only artefacts that may be built are:

1. The content itself (8–12 workflows).
2. One landing page with a price on it.
3. A checkout link.

No database. No accounts. No search. No app. Delivery is a zip or a repo link.

## Reasoning

- Every feature built before validation is a bet on an unvalidated assumption, and it is
  simultaneously the most fun and the least informative work available.
- A zip file and a Gumroad link can reach Rung 1. If they cannot, no amount of UI will.
- The features we would build now would be the wrong ones. The buyer's first ten questions
  will tell us which ones are right, and those questions cost nothing to collect.
- Building is ~10% of this business. Spending the first month on it inverts the ratio.

## Alternatives rejected

| Option | Why not |
|---|---|
| Build the vault app first | Months of work betting on an unvalidated assumption. |
| Build a "small" MVP app | "Small MVP" reliably becomes six weeks. A zip takes an afternoon. |
| No-code app builder | Still building. Same avoidance, faster syntax. |

## Consequences

- Early delivery will feel unimpressive. **This is correct and must not be optimised away.**
- Manual work (sending files, answering questions by hand) is accepted and is a feature: it is
  the highest-bandwidth customer research available.
- Phase 3 unlocks product work — and only then, against real requests from paying customers.

## What would reverse this

- Paying customers repeatedly ask for the same specific capability that genuinely cannot be
  delivered by files. That is a validated feature request, and the gate opens.
- Manual delivery becomes the bottleneck on revenue. A good problem; automate exactly that step
  and nothing more.
