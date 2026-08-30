# ADR-001 — We sell maintained workflows and skills, not prompt packs

**Status:** Accepted
**Date:** 2026-08-30

## Context

The original idea was broad: a site for "AI decisions, workflows, prompts, skills and stuff."
That covers two very different businesses — one dead, one live — and they cannot be run at
the same time because they require opposite positioning.

## Decision

We sell a **curated, verified, actively maintained library of role-specific AI workflows and
agent skills.** We do not sell prompts as a product, and we never use the phrase "prompt pack"
in any customer-facing copy.

## Reasoning

- Prompt marketplaces collapsed for structural reasons that have only gotten stronger: models
  improved past the point where prompt craft is scarce, supply is infinite and free, and there
  is zero switching cost or repeat purchase.
- The scarce good is not the artifact — it is the assurance that **this works, on the current
  model, and someone fixes it when it breaks**.
- Maintenance is unattractive work that never ends, which is precisely why competitors won't
  do it and why it is the only defensible position available to us.
- Role-specific framing ("workflows for consultants") converts far better than category
  framing ("AI workflows") and supports a higher price.

## Alternatives rejected

| Option | Why not |
|---|---|
| Prompt marketplace | Dead market. Zero moat, zero repeat purchase, infinite free supply. |
| Free open-source repo + donations | Doesn't reach Rung 1. Donations are not a business. |
| Consulting / done-for-you services | Fastest real money, but it's a job, not a startup. Optional side revenue only. |
| Broad "everything AI" library | No one sees themselves in it. Comprehensiveness is an anti-signal here. |

## Consequences

- We are committing to an **ongoing maintenance obligation**. If we stop, the product becomes
  a stale PDF and the business is over. This is accepted deliberately: it is the moat.
- Inventory is perishable. Every model release can invalidate part of the library. Budget
  recurring time for this, permanently.
- The library must stay **small enough for one person to maintain**. This caps catalogue size
  and that cap is a feature.

## What would reverse this

- Vendors (Anthropic/OpenAI) ship first-party maintained skill registries that cover our niche
  well. Then our maintenance promise stops being scarce and we need a new wedge.
- Customer conversations reveal that buyers explicitly don't value updates and just want a
  one-time artifact dump. Unlikely, but it would change the pricing model entirely.
