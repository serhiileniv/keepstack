# KotKot — AI Decisions Vault

> **First niche:** technical consultants & fractional CTOs
> ([ADR-008](docs/decisions/ADR-008-niche.md)).

This repo is the **brain** of the business, not the product. Nothing here is code.
It records what we decided, why, for whom, and what we do next — so that six weeks from
now we don't re-argue a settled question or forget why we said no to something.

## What we are building

A **maintained, role-specific library of AI decisions, workflows and agent skills** — sold to
people whose billable hour is worth more than the price of the product.

The differentiated unit is the **decision**: *"when X, choose Y, because Z — and here's when
that stops being true."* Prompts rot. Decisions compound.

We are explicitly **not** building a prompt marketplace. See
[ADR-001](docs/decisions/ADR-001-what-we-sell.md).

## Read in this order

| # | File | What it answers |
|---|---|---|
| 1 | [North Star](docs/north-star.md) | The goal (10 users / $100) and how we know we hit it |
| 2 | [Market](docs/market.md) | What's dead, what's live, who else is here |
| 3 | [Customers](docs/customers/README.md) | Who pays us, in what order |
| 3b | [Niche brief](docs/customers/niche-fractional-cto.md) | **The specific buyer, their wedge task, and the seed artifact list** |
| 4 | [Artifact spec](docs/artifact-spec.md) | **What we distribute and what we save** |
| 4b | [catalog/](catalog/README.md) | The inventory itself + templates to write against |
| 5 | [Validation](docs/validation.md) | **How we prove it works — and that anyone wants it** |
| 6 | [Roadmap](docs/roadmap.md) | The step-by-step. **Start executing here.** |
| 7 | [Decisions](docs/decisions/README.md) | Every settled call and its reasoning |
| 8 | [Risks](docs/risks.md) | What kills this, and the early warning signs |
| 9 | [Metrics](docs/metrics.md) | The only numbers we look at |

## The target

**10 paying strangers, or $100 — whichever comes first.** Ten users is a sample that teaches
us something; $100 is just a number. Optimise for the ten.

## The long game

A community-contributed, reputation-ranked repository of AI decisions — Stack Overflow / Hugging
Face for *"which approach, and why."* Real, differentiated, and deferred: it is a two-sided
network, and those die at cold start. The curated library is the seed crystal.
See [ADR-007](docs/decisions/ADR-007-platform-vision.md).

## House rules

1. **Every non-obvious call becomes an ADR.** If we argued about it, it gets written down.
2. **ADRs are append-only.** We don't edit history; we supersede it with a new ADR.
3. **The roadmap has exit criteria, not deadlines.** A phase ends when its criterion is
   met, not when a date passes.
4. **No building before selling.** Any task that adds product surface before a stranger
   has paid us is out of scope until Phase 3.
5. **Open questions get an owner and a deadline**, or they get closed with an assumption
   written down. An unanswered question in this repo is a stalled business.
