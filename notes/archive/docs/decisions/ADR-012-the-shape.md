# ADR-012 — One funnel: a maintained public catalog, with "what broke this week" as the engine

**Status:** Accepted
**Date:** 2026-08-30
**Supersedes:** [ADR-004](ADR-004-distribution.md)
**Amends the staging in:** [ADR-010](ADR-010-distribution-surface.md)
**Depends on:** [ADR-011](ADR-011-niche-change.md)

## Context

Three things changed at once:

1. [ADR-011](ADR-011-niche-change.md) made the audience **developers using agentic coding
   tools** — a single audience, where [ADR-004](ADR-004-distribution.md) assumed two.
2. The operator wants *"a place people go to stay in touch with AI skills, workflows and best
   practices"* — a **destination**, not a one-time file sale.
3. The money goal **stays near-term**: 10 paying users / $100 remains rung 2.

Those three are in tension. Destinations monetise late; the money goal says soon. This ADR is
how they are reconciled.

## Decision

### One funnel, not two

[ADR-004](ADR-004-distribution.md)'s split — free artifacts to devs for reach, paid library to
consultants for revenue — assumed the amplifiers and the buyers were different people. They are
now the same person. The funnel collapses:

```
public catalog + what-broke-this-week   ──▶   the paid kit
        (free, ungated, the audience)          (installable, current)
```

### The engine: "what broke this week"

**This is the decision that matters.** The recurring, public, dated record of what stopped
working:

> *"Model X shipped Tuesday. Six skills and two MCP configs broke. Here is each one, what
> changed, and the fix."*

Nobody publishes this. Every `awesome-*` list is a graveyard of untested links; the new skill
directories collect and never re-test. The gap on the internet is not *collecting* AI tooling —
it is that **nothing tells you whether a given setup still works today.**

It is also the only content shape that gives a destination a reason to be revisited. A catalog
is read once. A decay log is checked repeatedly, because the thing it tracks keeps decaying.

**In [ADR-010](ADR-010-distribution-surface.md) the staleness log was "the most valuable page on
the site." Here it is the front page.**

### Explicitly not: general AI news

The operator asked about news. General AI news is the most crowded niche on the internet and we
would have no advantage in it whatsoever.

The only news we can write that nobody else can is **breakage news**, and we can only write it
because we run the evals. Every unit of effort goes there. If a model release does not break
anything, the post is *"nothing broke, here is what we re-verified"* — which is also worth
publishing, and is a stronger claim than most AI newsletters make all year.

### What is free and what is paid

| | Free, ungated | Paid |
|---|---|---|
| **What** | Every artifact, readable. The catalog. What-broke-this-week. | **The kit**: the whole verified set, installed in one command, plus the update channel |
| **Why someone takes it** | It's the best answer on the internet to "does this still work" | They want it working in their setup in 60 seconds, and to keep working |
| **Role** | The entire audience engine. This *is* the marketing budget | Rung 2 |

**The first paid product** — concrete, so Phase 2 is executable:

> **The Agent Setup Kit.** A complete, tested agent configuration: `CLAUDE.md` patterns, skills,
> MCP server configs, permission settings, subagent definitions. One command to install. Every
> piece dated and verified against named models. Updated when they break, and you are told when
> they do.

**The paywall is deliberately leaky.** The artifacts are readable free; a determined developer
can assemble the kit by hand. That is accepted. What is sold is **convenience and currency**,
which is the same bet every successful developer tool makes. A paywall that hides the content
would kill the audience engine, and the audience engine is the business.

## Reasoning

- **The audience engine and the maintenance treadmill are the same work.** Running Gate C
  produces the weekly post. Nothing is done twice. For a one-person part-time operation this is
  the only structure that survives contact with reality.
- **Freshness is the only inherently recurring content in this category.** Everything else in
  AI tooling is written once and abandoned. That is why every list dies, and why a decay log
  does not.
- **It is copyable but not sustainable.** Anyone can fork the catalog tomorrow. Nobody will
  re-test it every month. That is the whole moat, restated for this audience.
- **Money stays near-term without a paywall**, because the paid thing is packaging, not access.
  That lets the free surface be genuinely free — which is what makes it spread.

## Amendment to ADR-010's staging

[ADR-010](ADR-010-distribution-surface.md) gated the public browsing surface at Phase 3.5, after
10 paying customers. That was correct when the surface was a post-revenue convenience. It is
wrong now: **the public surface is the acquisition mechanism**, so it must exist first.

What changes:

- **Brought forward:** the public repo, the readable catalog, the what-broke log. These are
  marketing, which [ADR-005](ADR-005-no-product-before-revenue.md) has always permitted — *"free
  artifacts are marketing, not the product."*
- **Still gated, unchanged:** accounts, search backends, databases, comments, contributions,
  anything with a login. [ADR-007](ADR-007-platform-vision.md) stands untouched — a
  single-author destination is not a two-sided network.
- **Unchanged and now stronger:** ADR-010's governing principle. *The delivery target is the
  buyer's filesystem, not a web page.* More true for this audience than the last one.

The surface starts as a **GitHub repo plus a generated static page**. No framework decision
needed to begin; [ADR-006](ADR-006-stack.md) still covers the page when it is time.

## Alternatives rejected

| Option | Why not |
|---|---|
| General AI news / newsletter | No advantage, brutal competition, daily treadmill forever |
| Paywall the artifacts | Kills the audience engine, which is the only distribution we have |
| Audience first, monetise in year two | Considered and explicitly rejected by the operator. Money stays at rung 2 |
| A skills *marketplace* (many contributors) | [ADR-007](ADR-007-platform-vision.md). Cold start, and it destroys curation |
| Just another awesome-list | It is the default outcome and it is the failure mode, not the plan. The re-testing is the entire difference |

## Consequences

- **A weekly cadence is now a commitment.** A "what broke this week" that skips three weeks is
  worse than never having started — it becomes public evidence that we do not run the treadmill
  we sell. **This is the single biggest new risk in the business.**
- **The catalogue cap loosens but does not disappear.** [ADR-001](ADR-001-what-we-sell.md) capped
  it at ~40 for one operator. Artifacts about tooling are cheaper to re-verify than artifacts
  about consulting engagements — many can be checked by running a command. The cap is now
  *"whatever can genuinely be re-verified in a day each month,"* and it is still a cap.
- **[ADR-003](ADR-003-pricing.md) is pending revision.** See
  [ADR-011](ADR-011-niche-change.md) consequences.
- **Metrics change.** Reach and revenue were tracked separately under ADR-004 because they came
  from different audiences. Now the funnel is one, and the number that matters between them is
  **return visits to the what-broke log**.

## What would reverse this

- The weekly post proves unsustainable at one part-time operator. Then drop to monthly and say
  so publicly, in advance — never silently.
- A vendor ships a first-party, maintained, dated skill registry covering the same ground. That
  is R4 in [risks.md](../risks.md) and it is the existential one for this shape specifically.
- Nobody returns. If the what-broke log does not produce repeat visits after a full cycle, the
  destination thesis is wrong and this collapses back to a one-time product sale.
