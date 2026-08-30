# Metrics

Few numbers, checked weekly. Everything else is noise that feels like insight.

## The one number

> **Paying strangers.** Target: 10.

If exactly one number is tracked, it's this one. It cannot be gamed and it cannot be faked
by activity.

## Weekly scoreboard

| Metric | Why it's here | Target at Rung 2 |
|---|---|---|
| **Paying strangers** | The only real validation | 10 |
| **Revenue** | Secondary to user count — 10 users teaches more than $100 | $100+ |
| **Qualified conversations** | The leading indicator of everything | 30/round |
| **Verified artifacts** | Inventory that passed the gates | ≥ 8, capped ~40 |
| **Stale %** | Health of the moat | < 15% |
| **Days since Gate C pass** | The early warning for R5 | < 35 |

## Reach vs. revenue — never average these

Per [ADR-004](decisions/ADR-004-distribution.md), the funnel is split, so the metrics are too:

**Reach metrics** (dev channels, free artifacts) — GitHub stars, post impressions, repo clones.
*Judged on volume. These do not indicate demand.*

**Revenue metrics** (consultant channels, paid library) — conversations, checkout starts, sales,
referrals. *Judged on conversion.*

A dashboard that averages a viral GitHub repo with zero sales into "things are going okay" is
worse than no dashboard.

## Contribution pressure — the Phase 4 unlock counter

[ADR-007](decisions/ADR-007-platform-vision.md) unlock condition 3 requires *three people to
contribute something good, unprompted.* It was unmeasurable until
[ADR-010](decisions/ADR-010-distribution-surface.md) added the issue templates on the public
repo. Count them, monthly:

| Counter | Source | Means |
|---|---|---|
| `broke-for-me` issues filed | public repo | Someone used it, on a real system, and cared enough to report. **The highest-quality signal in this document.** |
| `i-have-a-decision` issues filed | public repo | Direct count against ADR-007 condition 3 |
| Distinct people filing either | public repo | Three distinct good ones = condition 3 met |

A `broke-for-me` issue is not a complaint. It is free Gate C coverage from someone who trusted
the product enough to run it — treat the filer accordingly, and reply the same day.

## Vanity metrics — explicitly ignored

- Followers, stars, upvotes as success measures *(they are reach inputs, nothing more)*
- Newsletter subscribers *(we aren't running that play)*
- Number of artifacts *(volume is an anti-signal — see ADR-001)*
- Website traffic without checkout starts
- "This is great!" messages *(a card charge is validation; enthusiasm is not)*

## The qualitative record — worth more than the numbers

Kept verbatim, per customer, from the first ten:

1. **"What made you pay?"** — becomes the headline copy.
2. **"What almost stopped you?"** — becomes the objection to answer on the page.
3. **"What's missing?"** — becomes the Phase 3 backlog.

At ten customers the sample is too small for statistics and exactly right for sentences. The
sentences are the asset.

## Review cadence

- **Weekly:** the scoreboard. 10 minutes.
- **Monthly:** Gate C pass + changelog. Half a day.
- **At each rung:** re-read the ADRs. Anything contradicted by reality gets a superseding ADR,
  never a silent edit.
