# ADR-003 — One-time $39–49 first; subscription only after Rung 2

**Status:** Accepted
**Date:** 2026-08-30

## Context

The stated goal is "make even $10." A $9 price would hit that fastest. It would also be a
mistake, and the goal deserves a better interpretation than the literal one.

## Decision

- **v1 price: $39–49, one-time.** Start at $39; test $49.
- **No subscription until Rung 2** (10 paying strangers).
- **No free tier of the product.** Free artifacts exist, but they are marketing, published
  separately from the paid library.
- Launch discount is acceptable (e.g. $29 for the first 20 buyers) because it creates urgency
  without setting the anchor low.

## Reasoning

- **Cheap signals worthless.** At $9 the buyer assumes low quality, and the price does not
  clear the mental threshold where they actually adopt the thing.
- **$9 buyers complain the most.** Support cost per dollar of revenue is worst at the bottom.
- The buyer bills $100–200/hr. At $49, the product pays for itself in **under 30 minutes of
  saved time**. That is trivially defensible in the sales copy — and impossible to argue with.
- One-time pricing removes every objection at the first sale. Recurring revenue is earned by
  demonstrating maintenance over months, not asserted on day one.
- Ten sales at $49 is ~$490 — enough to prove the model. Ten at $9 is $90 and proves nothing.

## Alternatives rejected

| Option | Why not |
|---|---|
| $9 to hit "$10" fastest | Literal goal, wrong goal. Signals low value, attracts worst customers, proves nothing. |
| Subscription from day one | Asking for ongoing trust before earning any. Kills first conversion. |
| $199+ premium | Enters considered-purchase territory. Needs a track record and social proof we don't have. |
| Free with paid upsell | Two products to build. Premature. |

## Consequences

- Rung 1 ($10) is reached by a **single $39 sale**, not four $9 ones. The literal goal is met
  on the first transaction either way; this route also builds toward Rung 2.
- We must justify $49 with visible quality: worked examples, stated outcomes, real polish.
- The subscription question is deferred, not dropped — see the Phase 3 gate in the roadmap.

## What would reverse this

- Consistent price objection at $39 from qualified buyers in segment 1 (not from dev teams —
  their objection is expected and does not count).
- Buyers asking unprompted for ongoing updates as a paid thing. That's the signal to introduce
  the subscription early, and it's a good problem.
