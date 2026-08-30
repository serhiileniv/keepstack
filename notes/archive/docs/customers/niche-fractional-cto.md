# Niche brief — technical consultants & fractional CTOs

**Locked in [ADR-008](../decisions/ADR-008-niche.md). This is who Phase 1 is written for.**

## Who, precisely

Independent technical operators who sell judgement by the hour or the retainer:
fractional CTOs, technical advisors, solo architecture consultants, technical due-diligence
contractors, one-person "I fix your engineering org" shops. Typically 1–3 concurrent clients.

**Not** salaried engineers, and **not** dev-shop owners with a delivery team. Both look similar
and neither buys the same way.

## Why they buy

- Bills **$150–300/hr**. A $39 product breaks even in ~10 minutes of recovered time.
- Sole decision-maker. No procurement, no approval, no security review.
- Already fluent with agentic tooling — **zero onboarding cost**.
- Their pain is **per-engagement and recurring**: every new client restarts the same expensive ramp.

## The qualifying answer *(Phase 1.2)*

> **The named recurring task:** *Week one with a new client — get oriented in an unfamiliar
> codebase and organisation, and produce a written assessment credible enough to justify the rate.*

This is the wedge. It is expensive (often 10–20 hours), it is largely **unbillable or
under-billable**, it recurs with every engagement, it directly determines whether the client
renews, and it is unusually amenable to agentic tooling. Nothing else in their week scores that
well on all five.

## Candidate artifact list *(seed — superseded by [ADR-009](../decisions/ADR-009-phase1-twelve.md))*

> **Phase 1.3/1.4 are done.** The final twelve, and what was cut and why, are in
> [ADR-009](../decisions/ADR-009-phase1-twelve.md). The list below is kept as the original seed.


Ranked by `time saved × frequency`. Cut to 12 in Phase 1.4.

### Tier 1 — the wedge (write these first)
1. **Unfamiliar-codebase orientation** — from clone to a defensible mental model
2. **Written technical assessment** — findings a non-technical founder can act on
3. **Risk & tech-debt inventory** — severity-ranked, not a wall of nitpicks
4. **Decision:** how deep to go in week one before it stops paying for itself
5. **Decision:** when to trust an agent's read of a codebase vs. verify by hand

### Tier 2 — the recurring grind
6. **Monthly stakeholder update** — engineering reality → board language
7. **Build-vs-buy evaluation** with a written recommendation
8. **Architecture decision record** produced from a messy discussion
9. **Estimate translation** — roadmap into something a non-technical founder can plan against
10. **Decision:** which technical debt to raise with a client and which to silently absorb

### Tier 3 — episodic but high-value
11. **Technical hiring loop** — JD, screen, take-home review
12. **Incident postmortem** for a client without a postmortem culture
13. **Cloud cost review** with a prioritised action list
14. **Migration plan** with a staged risk profile
15. **Decision:** agent tooling setup to hand a client's team on exit

**Watch the mix.** [artifact-spec](../artifact-spec.md) calls for **4 decisions** in the first
12, and decisions are harder to write than workflows. They are also the differentiator. Do not
let the easy ones crowd them out.

## Vocabulary

| Say | Never say |
|---|---|
| engagement, client, retainer, scope | users, team members |
| billable / unbillable hours | productivity |
| assessment, findings, recommendation | output, content |
| decision, trade-off | best practice |
| verified, maintained, current | curated collection |

**Copy always addresses the person who bills.** The instant it reads as "for engineering teams,"
we've slipped into segment 4 and the price objection starts — see the overlap risk in ADR-008.

## Channels

| Channel | Use | Note |
|---|---|---|
| LinkedIn | Primary for **selling** | Where fractional CTOs actually present themselves |
| X / HN | Primary for **reach** (free artifacts) | Overlaps segment 4 — track separately |
| Fractional-exec / CTO communities | High-intent | Slack and Discord groups; join before posting |
| GitHub | Free artifacts | Top of funnel, not a sales channel |
| Direct outreach | **Phase 2.5–2.6** | 30 named people who publicly complained about the wedge task |

## Message

> "Week one with a new client, done in an afternoon. Codebase oriented, risks ranked, assessment
> written. Verified against current models, and updated when they change."

**Not:** "AI workflows for developers."

## Open questions for customer conversations

- [ ] Is week-one ramp really the worst task, or is it stakeholder reporting? **Ask before writing.**
- [ ] Do they bill the ramp-up, absorb it, or fold it into a fixed fee? Changes the copy entirely.
- [ ] What have they already tried for this, and did they still use it in week two?
- [ ] Would they pay for the *decisions* alone, or only the executable workflows?
