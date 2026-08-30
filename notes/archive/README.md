# Archive — the startup version

Everything here was written on 2026-08-30 for a **different project**: a paid, maintained
library of AI workflows sold to technical consultants for $39, with a phased roadmap toward
10 paying strangers.

That project was abandoned the same day, for a good reason: its central premise was that the
operator had fractional-CTO experience to write from. He doesn't — he's a developer building
with AI daily. Everything downstream of that premise was scaffolding on sand.

**It is kept because parts of it are genuinely useful and were expensive to think through.**

## Still worth reading

| File | Why |
|---|---|
| [docs/artifact-spec.md](docs/artifact-spec.md) | The record schema — frontmatter, `verified_on`, `expires`, status lifecycle. The entry format in the hub is a stripped-down version of this. |
| [docs/validation.md](docs/validation.md) | Gate A ("no worked example → the artifact does not exist") and Gate C (freshness). The dating idea in the hub comes from here. |
| [docs/decisions/ADR-001-what-we-sell.md](docs/decisions/ADR-001-what-we-sell.md) | Why the scarce good is *"this works, on the current model"* and not the artifact itself. Still the sharpest thing in here. |
| [docs/market.md](docs/market.md) | The read on why prompt marketplaces collapsed. Unchanged by the pivot. |
| [docs/risks.md](docs/risks.md) | R1 (free is the competitor) and R2 (distribution, not building, is the hard part) apply to any version of this. |

## Not worth reading

The revenue roadmap, the customer segments, the pricing ADRs, the outreach plan, and the 7
catalog artifacts written for consultants. All built for an audience that was never real.

Three of those artifacts survived the pivot and moved to `hub/drafts/`.

## The lesson, recorded once

The strategy was excellent and the premise was unchecked. **Check who you actually are before
building the plan around who you'd need to be.**
