# ADR-007 — The community platform is the destination, not the starting point

**Status:** Accepted
**Date:** 2026-08-30

## Context

The vision raised: *"something like Stack Overflow or Hugging Face, but for AI decisions."*

This is a good idea. It is genuinely differentiated — Stack Overflow answers *"how do I do X"*
and Hugging Face hosts *artifacts*, but neither captures *"which approach should I choose, and
why, and when does that change."* That gap is real and nobody good is sitting in it.

It is also a **two-sided network**, which is the hardest possible thing to start from zero.

## Decision

The community platform is the **long-term destination and Phase 4**. It does not start until
**Rung 3** (10 paying users, 5 of whom came back).

Until then, we build the curated library. Every artifact we write to the schema in
[artifact-spec.md](../artifact-spec.md) is deliberately seed content for the platform — same
schema, same validation rules, no migration required later.

## Reasoning

**Why the platform is right eventually:**

- The "decision" unit type genuinely has no good home today.
- Decisions **compound**, unlike prompts, which rot. A library of them gets more valuable over time.
- It is the only known way the maintenance moat scales past one operator: Gate D in
  [validation.md](../validation.md) turns freshness into a crowd-sourced signal instead of a
  monthly chore that eventually crushes us.
- Network effects, once started, are the only real defensibility in this space. Content isn't.

**Why it must not start now:**

- **Cold start.** An empty Stack Overflow is worthless to both sides. Contributors won't
  contribute without readers; readers won't read without content. Someone has to eat that cost,
  and with one part-time operator and no audience, that someone is us — for months, unpaid.
- Both named comparables took **years and substantial funding** to cross the cold-start threshold.
  Neither did it as a side project.
- Platforms monetise **late**. Our target is 10 paying users, and a platform is the slowest
  possible route to a first sale.
- Unmoderated contribution at low volume produces low-quality content, which destroys the one
  thing we're actually selling: curation.

**The resolution — come for the tool, stay for the network.** The curated library is the seed
crystal. It attracts the exact people who would contribute, and it proves the schema works
before we ask anyone else to write to it. This is how most successful communities actually
started; almost none started as an empty forum.

## Alternatives rejected

| Option | Why not |
|---|---|
| Launch the community platform now | Cold start with no audience, no funding, one operator. This is the plan that quietly consumes a year. |
| Open contributions to the paid library immediately | Destroys curation, which is the product. |
| Never build the platform | Gives up the only durable defensibility available. Keep the option. |
| Build platform features "just in case" | Violates ADR-005 and builds the wrong ones. |

## Consequences

- Everything we write now uses the platform's schema. **Seeding is free if we do it from day
  one and expensive if we retrofit** — this is the main cost we're paying up front, and it's cheap.
- We resist adding contribution features when people ask. They will ask before it's ready.
- The public free repo doubles as the recruiting ground for future contributors. Watch who
  files good issues against it — those are the first ten contributors.

## The unlock conditions (all four required)

1. Rung 3 reached: 10 paying users, 5 returning.
2. ≥ 40 verified artifacts in the catalogue.
3. ≥ 3 people have contributed something good **unprompted** (via issues, PRs or email).
4. The monthly re-verification pass is taking more than a day — i.e. the manual moat is
   genuinely hitting its ceiling.

Condition 3 is the important one. **If nobody contributes when there's no mechanism, nobody
will contribute when there is one.** Building the mechanism does not create the desire.

## What would reverse this

- Unprompted contribution pressure arrives far earlier than expected — many people asking to
  add their own decisions before Rung 3. That's a real signal; open a narrow contribution path
  and write a superseding ADR.
- A well-funded competitor takes the position first. Then the choice is to concede the platform
  layer and stay a curated publisher — which is still a viable business, just a smaller one.
