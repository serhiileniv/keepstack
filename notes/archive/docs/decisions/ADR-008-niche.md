# ADR-008 — First niche: technical consultants & fractional CTOs

**Status:** Superseded by [ADR-011](ADR-011-niche-change.md) — the operator is not a practising fractional CTO, so this ADR's core premise was false.
**Date:** 2026-08-30

## Context

[ADR-002](ADR-002-target-customers.md) selected solo consultants as segment 1, but "solo
consultant" is a segment, not a niche. The artifacts, the vocabulary and the channel all
change with the discipline. This was the single open decision blocking Phase 1.

## Decision

**Technical consultants and fractional CTOs.** All Phase 1 inventory is written for them.

## Reasoning

- **Existing expertise is the only unfair advantage available.** We can write from recall
  instead of research, which removes the slowest part of Phase 1 entirely. Twelve artifacts
  written from memory take days; twelve researched take weeks we don't have.
- **The economics work.** Fractional CTOs bill $150–300/hr, own the budget, need no approval,
  and expense tooling without thinking. A $39 product pays for itself in ~10 minutes of
  recovered time.
- **They already use agentic tooling**, so onboarding cost is near zero — no need to teach
  Claude Code or MCP before the artifact is useful.
- **The pain is per-engagement and recurring.** Every new client restarts the same expensive
  ramp-up. That is a repeat-purchase shape, not a one-off.
- Same-language selling: no translation layer between what we know and what they buy.

## The overlap risk, addressed

This niche sits close to segment 4 (small dev teams), which
[ADR-002](ADR-002-target-customers.md) ranked as low willingness-to-pay. That ranking still
holds, and the distinction is the whole point:

> **A fractional CTO sells their hours. A salaried engineer does not.**

The consultant converts saved time directly into billable capacity or into a shorter working
week. The employee converts it into… slightly less work, for the same salary. Same technical
content, completely different buying behaviour.

**Practical consequence:** every piece of copy must speak to *the person who bills*. The moment
it reads as "for engineering teams," we've drifted into segment 4 and the price objection starts.

## Alternatives rejected

| Option | Why not |
|---|---|
| Recruiters / talent | Very high pain and underserved, but needs real workflow research we can't shortcut. Strong candidate for niche #2. |
| Marketing / growth consultants | Largest and most reachable, but the most crowded — nearly all AI content already targets them. |
| Accountants / bookkeepers | High WTP and repetitive work, but conservative, slow-adopting, and accuracy stakes raise the verification burden. |
| Lawyers (solo/small) | Highest WTP of all, but compliance and liability overhead is disproportionate for a v1. |

## Consequences

- Phase 1 artifacts are technical in nature — codebase assessment, architecture decisions,
  stakeholder translation, hiring. See [the niche brief](../customers/niche-fractional-cto.md).
- Distribution partly collapses: dev channels now reach both our free-artifact audience *and*
  our buyers, so [ADR-004](ADR-004-distribution.md)'s split funnel is shorter than planned.
  Good for speed. **The metrics must still be kept separate**, because the audiences overlap
  but do not convert alike.
- The `job` field on every artifact must name a *consulting* task, not an engineering task.

## What would reverse this

- We can't write 12 artifacts from recall. That means the expertise claim was wrong and the
  entire reason for this choice is gone — reconsider immediately.
- Buyers consistently turn out to be salaried engineers rather than consultants. Then we're
  accidentally in segment 4, and pricing needs rethinking, not persistence.
