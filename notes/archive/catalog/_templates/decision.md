---
id: dec-NNNN
type: decision
title: ""
version: 0.1.0
segments: [solo-consultant]
job: ""                          # the NAMED consulting task. Vague here = unsellable.
outcome: ""                      # MEASURED, e.g. "3 hrs -> 25 min". Never estimated.
evidence: examples/dec-NNNN.md
status: draft                    # draft | verified | stale | retired
verified_on:
verified_against: []             # e.g. [claude-opus-5, claude-sonnet-5]
expires:                         # verified_on + 90 days
eval: evals/dec-NNNN.md
requires: []
supersedes:
superseded_by:
tags: []
tier: paid                       # free | paid
author: kotkot
license: proprietary
---

# <Title>

## Context
The situation that forces a choice. When does the reader find themselves here?

## Options
| Option | Real trade-off |
|---|---|
| A | |
| B | |

No strawmen. If an option has no genuine case for it, it isn't an option — it's padding.

## The call
What to choose. One or two sentences, unambiguous.

## Why
The reasoning, **including what you tried that failed.** The failures are the part that can't
be found on GitHub, and they're what the buyer is actually paying for.

## When this is wrong
The conditions under which the opposite call is correct.
**This section is what separates a decision from an opinion.** If it's empty, you have an opinion.

## Expiry trigger
What change in the world invalidates this — a model release, an API change, a pricing shift.
This is what makes the artifact maintainable rather than a liability.
