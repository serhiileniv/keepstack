# North Star

> **Revised 2026-08-30** after [ADR-011](decisions/ADR-011-niche-change.md) (niche change) and
> [ADR-012](decisions/ADR-012-the-shape.md) (the shape). The previous version was written for
> technical consultants.

## The one-line goal

Be the place a developer checks to find out **whether an AI skill, workflow or config still
works** — and sell them the version that is already installed and kept current.

## Who

Developers who use agentic coding tools daily: Claude Code, Cursor, Codex, agent CLIs, MCP
servers, subagents. [ADR-011](decisions/ADR-011-niche-change.md).

**The named task:** *keeping an agent setup that works — and that still works after this week's
model release.*

## The target

> **10 paying users, or $100 — whichever comes first.**

Unchanged, and deliberately so. The shape changed; the bar did not. A destination that never
takes money is a hobby, and we would rather find out early.

## The goal ladder

Aim at the next rung, never the top.

| Rung | Target | Proves | Status |
|---|---|---|---|
| 0 | 8 verified artifacts public + the first *what broke this week* post shipped | The treadmill is real, not a claim | ☐ |
| 1 | **4 consecutive weekly posts, none missed** | One part-time person can sustain it. **This is the gate on everything else** | ☐ |
| 2 | First payment from a stranger | Someone will pay at all | ☐ |
| 3 | **10 paying users / $100+** ← **THE TARGET** | It is a product, not a hobby | ☐ |
| 4 | 5 of those 10 come back (renew or buy again) | The maintenance promise is real | ☐ |
| 5 | $500/mo recurring | The treadmill is fundable | ☐ |
| 6 | Contributors other than us | It could become a platform ([ADR-007](decisions/ADR-007-platform-vision.md)) | ☐ |

**Rung 1 is the new one, and it is the honest one.** The entire business is a promise to keep
re-checking. Four weeks without missing one is the cheapest possible proof that the promise is
keepable. If it cannot be done for four weeks with no audience and no pressure, it will not be
done for a year with both.

**"Stranger" is load-bearing.** Friends and colleagues do not count toward any rung.

## The core value promise

1. **Curated** — we already threw away the 90% that doesn't work.
2. **Verified** — every artifact has a worked example and a measured outcome.
3. **Maintained** — when a model or API changes and something breaks, we fix it and **say so
   publicly, with a date**.

Item 3 is the entire moat, and in this version it is also the **content**. The weekly breakage
post is produced by running the maintenance we already promised. Nothing is done twice.

Content is copyable in an afternoon. A dated record of re-testing is not.

## What "done" looks like at Rung 3

- ~20 artifacts, each passing the gates in [validation.md](validation.md).
- A public catalog anyone can read, ungated.
- 8+ consecutive weekly breakage posts.
- A paid kit that installs in one command.
- 10 payments from people we have never met.
- A written answer from each: *"What made you pay?"*

## Non-goals

- **A marketplace.** Many sellers, unverified volume, cold start. See
  [ADR-007](decisions/ADR-007-platform-vision.md) and the Neura Market note in
  [market.md](market.md). Their 27,000 workflows are possible *because* nothing is checked.
- **General AI news.** The most crowded niche on the internet and we have no edge in it. Only
  **breakage news**, which nobody else can write because nobody else runs the evals.
  [ADR-012](decisions/ADR-012-the-shape.md).
- **Selling raw prompt packs.** [ADR-001](decisions/ADR-001-what-we-sell.md).
- **Paywalling the artifacts.** The free catalog is the entire distribution mechanism.
- **Accounts, search backends, databases** before Rung 3.
- **Being comprehensive.** "5,000 workflows" is an anti-signal. Small and known-good beats large.

## Operating constraint

One operator, part-time. Every decision is filtered through: *can one person still maintain this
in six months?* If the answer is no, the decision is wrong regardless of its upside.

**The new constraint this shape adds:** a weekly cadence, indefinitely. Missing it publicly is
worse than never starting, because we would be visibly failing at the exact thing we sell.
If weekly proves unsustainable, drop to monthly **in advance and in public** — never silently.
