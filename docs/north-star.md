# North Star

## The one-line goal

Build a small, profitable product that sells **time back** to people who bill for their time,
by maintaining a curated library of AI decisions, workflows and skills that are known to work
**on today's models**.

## The target

> **10 paying users, or $100 — whichever comes first.**

This is the real bar, set by the founder, and it is a much better bar than "$10." Ten users
is a *sample*: it tells us who buys, why, and what they ask for next. One user is an anecdote.
At the v1 price of $39 (see [ADR-003](decisions/ADR-003-pricing.md)), 10 users is ~$390, so
hitting 10 users clears $100 on the way. **Optimise for the 10, not the $100.**

## The goal ladder

We aim at the next rung, never the top.

| Rung | Target | Proves | Status |
|---|---|---|---|
| 0 | Ship a public artifact strangers actually use for free | The content is useful | ☐ |
| 1 | First payment from a stranger | Someone will pay at all | ☐ |
| 2 | **10 paying users / $100+** ← **THE TARGET** | It is a product, not a favour | ☐ |
| 3 | 5 of those 10 come back (renew or buy again) | The maintenance promise is real | ☐ |
| 4 | $500/mo recurring | The treadmill is fundable | ☐ |
| 5 | Contributors other than us | It could become a platform | ☐ |

**"Stranger" is load-bearing.** Friends, colleagues and people who owe us a favour do not count
toward any rung. A sale to someone who found us on their own is the only real signal.

## What "done" looks like at Rung 2

- 12 artifacts, each passing the validation gates in [validation.md](validation.md).
- A public landing page with a price on it.
- 10 payments from people we have never met.
- A written answer from each of them to: *"What made you pay?"*
- At least 3 unprompted feature or content requests. These become the Phase 3 backlog.

## The core value promise

Not "here are prompts." Three things, in this order:

1. **Curated** — we already threw away the 90% that doesn't work.
2. **Verified** — every artifact has a worked example and a measured outcome.
3. **Maintained** — when a model or API changes and something breaks, we fix it and tell you.

Item 3 is the entire moat. Content is copyable in an afternoon; a maintenance commitment is not.
If we ever stop maintaining, we are selling a stale PDF and we should shut down.

## The long-term shape (not the current goal)

A community-contributed, reputation-ranked repository of AI decisions — Stack Overflow / Hugging
Face for *"which approach, and why."* This is a legitimate destination and a genuinely
differentiated one. It is also a two-sided network, which is the hardest thing in software to
start from zero. See [ADR-007](decisions/ADR-007-platform-vision.md) for why it is deferred to
Phase 4 and what specifically unlocks it.

**The curated library is the seed crystal for the platform.** Come for the vault, stay for
the network. But we earn the network; we do not launch it.

## Non-goals (things we will say no to)

- **Selling raw prompt packs.** Commodity, zero defensibility. See ADR-001.
- **Serving AI hobbyists / prompt collectors.** They consume infinitely and pay nothing.
- **Enterprise.** 9-month sales cycles, one operator. Not now.
- **Launching the community platform before Rung 3.** See ADR-007.
- **Building the SaaS before Phase 3.** Search, accounts, team sync, versioning — premature
  until people pay for the static version.
- **Free tier as a business model.** Free artifacts are marketing, not the product.
- **Being comprehensive.** "500 prompts" is an anti-signal. Small and known-good beats large.

## Operating constraint

One operator, part-time. Every decision is filtered through: *can one person still maintain this
in six months?* If the answer is no, the decision is wrong regardless of its upside.
