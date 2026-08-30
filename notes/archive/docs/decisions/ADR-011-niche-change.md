# ADR-011 — Niche change: developers using agentic coding tools

**Status:** Accepted
**Date:** 2026-08-30
**Supersedes:** [ADR-008](ADR-008-niche.md)

## Context

[ADR-008](ADR-008-niche.md) chose technical consultants and fractional CTOs, and it chose them
for one stated reason:

> *"Existing expertise is the only unfair advantage available. We can write from recall instead
> of research."*

That premise is false. The operator is **a developer with a job and side projects, building
primarily with AI tooling** — not a practising fractional CTO. Writing twelve artifacts about
week-one client engagements would have meant researching them, or inventing them, which is the
one thing a product selling *verified* cannot survive doing.

ADR-008's reasoning was sound. Its input was wrong.

## Decision

**Developers who use agentic coding tools daily** — Claude Code, Cursor, Codex, agent CLIs,
MCP servers, subagents. People whose editor now contains something that acts on its own.

### The named recurring task

> **Keeping an agent setup that actually works — and that still works after this week's
> model release.**

Configs, skills, `CLAUDE.md` files, MCP servers, permissions, subagent definitions. They are
assembled once from scattered blog posts, they work for a while, and they silently rot. Nothing
announces the rot. You find out when the agent starts doing something stupid and you cannot tell
whether it is you, the config, or the model.

This is the right wedge because it is the only pain in this space that is **inherently
recurring**. A prompt collection is read once. A setup that decays needs re-checking forever,
and re-checking is the thing we are building anyway.

## The uncomfortable part: our own docs say developers don't pay

[ADR-002](ADR-002-target-customers.md) ranked dev teams low on willingness-to-pay.
[ADR-008](ADR-008-niche.md) went further and made it the crux:

> *"A fractional CTO sells their hours. A salaried engineer does not. The employee converts
> saved time into… slightly less work, for the same salary."*

**That reasoning is correct about time, and wrong about developers.** Developers buy tools on a
personal card constantly — editors, terminals, launchers, database clients, dictation apps,
their own AI subscriptions. Typically $10–100, no approval, decided in minutes. What they
reliably do *not* buy is a **document about productivity**.

So the objection is real but it is an objection to the **packaging and the price**, not to the
audience:

| ADR-008's consultant pitch | What has to replace it |
|---|---|
| "Save 7 unbillable hours" | "This works. Installed in one command. Still current." |
| $39, justified by a billable hour | The impulse band — **lower**, see consequences |
| A library you read | A thing you install |
| Sold by direct outreach on LinkedIn | Found on GitHub, HN, X, Reddit, Discord |

**This is not yet proven and it is the first thing to test.** It is recorded here as the
assumption the business now rests on, so that if it fails we know exactly which sentence was
wrong.

## Reasoning

- **Content cost drops to near zero.** The operator runs this tooling every working day. An
  artifact is produced by doing the work once with a timer and recording it honestly — not by
  recalling engagements that never happened. This is ADR-008's original logic, finally applied
  to a true premise.
- **The audience is reachable for free.** GitHub, HN, X, Reddit, agent-tooling Discords. No cold
  LinkedIn outreach to thirty strangers — which was the single hardest step in the old Phase 2
  and the one most likely to simply not happen.
- **One audience now does both jobs.** [ADR-004](ADR-004-distribution.md) split the funnel
  because devs amplify without paying and consultants pay without amplifying. With a single
  audience that split collapses — see [ADR-012](ADR-012-the-shape.md).
- **Model churn hits this audience hardest and most visibly.** A config breaking on release day
  is a shared, dated, public event. The maintenance moat is more obviously valuable here than
  anywhere else, because the decay is something they have personally experienced.

## What we give up

Stated plainly, because these were real advantages:

- **The price justification.** $150–300/hr made $39 trivially defensible. That argument is gone
  and the price has to come down.
- **The unbillable-ramp story** — a genuinely strong, specific, expensive pain. The replacement
  ("your setup rots") is more universal but less acute.
- **Sole-decision-maker economics.** Still true for a personal-card purchase, but the amounts
  are smaller.
- **Four of the seven drafted artifacts.** See consequences.

## Consequences

- **[ADR-003](ADR-003-pricing.md) needs revising.** $39 was priced against a billable hour that
  no longer exists. The developer impulse band is lower — likely $19–29 one-time. **Do not
  change the price silently; write the ADR after the first real conversations.**
- **[ADR-004](ADR-004-distribution.md) is superseded** by [ADR-012](ADR-012-the-shape.md). The
  split funnel assumed two audiences.
- **Artifact triage** — of the seven drafted for the old niche:

  | Artifact | Fate |
  |---|---|
  | `dec-0003` when to trust an agent's read of a codebase | **Keep whole.** Universal to anyone running agents on code |
  | `wf-0001` unfamiliar-codebase orientation | **Keep, reframe.** New job, new repo, OSS contribution — not "week one with a client" |
  | `dec-0001` client code through AI tooling | **Rewrite.** Becomes "what your employer's policy actually allows, and how to check" |
  | `dec-0002` how deep to go in week one | **Retire.** Consultant engagement economics |
  | `dec-0004` what debt to raise vs absorb | **Retire.** Client politics |
  | `wf-0002` week-one written assessment | **Retire.** Consultant deliverable |
  | `wf-0003` risk and tech-debt inventory | **Retire.** Consultant deliverable |

  Three of seven survive. Cheap, because the pivot happened at seven and not at twelve.
- **[ADR-009](ADR-009-phase1-twelve.md) is void.** The twelve were chosen for consultants. A new
  set is chosen against the new wedge task.
- The niche brief at `docs/customers/niche-fractional-cto.md` is now historical.

## What would reverse this

- **Developers will not pay at any price**, in any packaging, after a genuine test. Then move
  *up* to engineering leads standardising tooling across a team — who have budget — rather than
  back to consultants. Do not re-pick a niche the operator cannot write from.
- The operator stops using agentic tooling daily. The whole advantage is that the content is a
  by-product of the actual working day; if that stops, so does the content.
