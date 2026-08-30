# Decision log

Every settled call lives here as an ADR (Architecture Decision Record — here, "Architecture"
means the business as much as the code).

## Rules

- **Append-only.** Never edit a decision to reflect a new opinion. Write a new ADR and mark
  the old one `Superseded by ADR-NNN`.
- **Record the reasoning, not just the verdict.** The reasoning is what lets us re-evaluate
  correctly when the facts change.
- **Record what we rejected and why.** Half the value of this log is not re-litigating
  options we already dismissed.
- **Status values:** `Accepted` · `Superseded` · `Proposed` · `Reversed`

## Index

| ADR | Decision | Status |
|---|---|---|
| [001](ADR-001-what-we-sell.md) | Sell maintained workflows/skills, not prompt packs | Accepted |
| [002](ADR-002-target-customers.md) | Four segments, worked in strict sequence | Accepted |
| [003](ADR-003-pricing.md) | One-time $39–49 first; subscription only after Rung 2 | Accepted |
| [004](ADR-004-distribution.md) | Free artifacts for devs; paid offer to consultants | Accepted |
| [005](ADR-005-no-product-before-revenue.md) | No product surface before a stranger pays | Accepted |
| [006](ADR-006-stack.md) | Gumroad/Polar + a single Next.js page. No app. | Accepted |
| [007](ADR-007-platform-vision.md) | Community platform is Phase 4, gated on Rung 3 | Accepted |
| [008](ADR-008-niche.md) | First niche: technical consultants / fractional CTOs | Accepted |

New decisions start from [ADR-000-template.md](ADR-000-template.md).
