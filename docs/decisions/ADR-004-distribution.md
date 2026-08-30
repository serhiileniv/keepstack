# ADR-004 — Free artifacts for developers, paid offer to consultants

**Status:** Accepted
**Date:** 2026-08-30

## Context

The two audiences that matter serve different functions. Developers amplify but pay reluctantly.
Consultants pay but don't amplify. Trying to make one audience do both jobs fails at both.

## Decision

Run a **split funnel**:

- **Top (reach):** free, genuinely good artifacts published publicly on GitHub, X, HN, Reddit
  and relevant Discords. Aimed at developers and agentic-tooling users. No paywall, no email gate.
- **Bottom (revenue):** the paid library, sold to solo consultants via LinkedIn, direct outreach,
  and their own professional communities.

Two of the paid library's workflows are released free, permanently. **The free ones are the ad.**

## Reasoning

- Distribution is ~90% of this business and we have no audience. Free work is the only currency
  we have to buy attention with.
- Developer channels are the highest-velocity, lowest-cost reach available. Consultant channels
  (LinkedIn, discipline-specific communities) convert but do not spread.
- Gating the free artifacts behind an email would suppress the reach that is their entire purpose.
- Giving away real work from the paid library — not a watered-down teaser — is what makes the
  paid version credible. A weak free sample proves the paid one is weak too.

## Alternatives rejected

| Option | Why not |
|---|---|
| Paid-only, no free tier | No audience, no reach, no trust. Nothing to launch into. |
| Email-gated free content | Kills virality for a list we're not yet equipped to use. |
| Paid ads | No proven funnel to spend into. Burns money to learn what free posts teach for nothing. |
| Build an audience first, product later | Slow, and the product is what teaches us what the audience wants. Run both. |

## Consequences

- A meaningful share of effort produces no direct revenue. **That is the marketing budget.**
- The free repo must be maintained to the same standard as the paid library — a stale free repo
  actively discredits the paid promise.
- Metrics must separate **reach** (dev channels) from **revenue** (consultant channels), and
  never average them together. See [metrics](../metrics.md).

## What would reverse this

- The free repo drives traffic that never crosses into segment 1. If reach is high and paid
  conversion is zero after a full cycle, the funnel is disconnected and needs redesigning.
- A consultant channel turns out to amplify on its own. Then the split is unnecessary and we
  should concentrate.
