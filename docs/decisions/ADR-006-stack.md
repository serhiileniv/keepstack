# ADR-006 — Gumroad or Polar, plus a single Next.js page

**Status:** Accepted
**Date:** 2026-08-30

## Context

We need to take money and show an offer. That is the entire technical requirement until Phase 3.
See [ADR-005](ADR-005-no-product-before-revenue.md).

## Decision

- **Payments + delivery:** Polar (preferred) or Gumroad. Both handle checkout, VAT/sales tax,
  payouts and file delivery. Setup: under an hour.
- **Landing page:** one static Next.js page deployed on Vercel. Or, if it delays launch by even
  a day, the Polar/Gumroad product page alone.
- **Analytics:** Vercel Web Analytics. Nothing more.
- **Everything else:** does not exist yet.

## Reasoning

- Polar/Gumroad remove the two genuinely annoying problems — international tax compliance and
  file delivery — for a percentage fee. Building either ourselves at this stage is indefensible.
- A static page needs no database, no auth and no backend, so there is nothing to maintain and
  nothing to break while we are focused on selling.
- Deferring Stripe avoids tax registration questions entirely until there is revenue worth the
  paperwork.

## Alternatives rejected

| Option | Why not |
|---|---|
| Stripe direct | Handling VAT/sales tax ourselves at $0 revenue is pure overhead. |
| Full app with Supabase auth | Violates ADR-005. |
| Carrd / Framer | Fine, honestly. Next.js chosen only because it's already familiar. Not a load-bearing choice. |

## Consequences

- Polar/Gumroad take a percentage. Accepted — it buys compliance and delivery.
- We will outgrow this. That is a Phase 3 problem and a good one to have.

## The Phase 3 stack (do not build yet)

Recorded so it isn't re-debated later, **not** as permission to start:
Next.js on Vercel · Supabase (Postgres + auth) · Polar for subscriptions · MDX or DB-backed
content · Vercel Web Analytics.

## What would reverse this

- Polar/Gumroad cannot deliver the product format we need. Unlikely for files.
- Revenue reaches a point where the percentage fee exceeds the cost of running billing
  ourselves. Nowhere near that.
