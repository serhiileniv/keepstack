---
id: dec-0003
type: decision
title: "When to trust an agent's read of a codebase, and when to verify by hand"
version: 0.1.0
segments: [technical-consultant, fractional-cto]
job: "Decide which agent-produced claims about an unfamiliar codebase can go into a client-facing assessment unverified"
outcome: ""                       # Gate B pending — measure, never estimate
evidence: examples/dec-0003.md
status: draft
verified_on:
verified_against: []
expires:
eval: evals/dec-0003.md
requires: [wf-0001]
supersedes:
superseded_by:
tags: [week-one, verification, agent-reliability, assessment]
tier: paid
author: kotkot
license: proprietary
---
> **SURVIVES WHOLE — universal to anyone running agents on code. Only the segments field changes.** Niche changed in [ADR-011](../../docs/decisions/ADR-011-niche-change.md).


# When to trust an agent's read of a codebase

## Context

Twenty minutes after cloning, you have a confident architecture summary: services, data flow,
the auth model, where the tests are, what the risks are. It is well written and mostly correct.

Some of it is wrong. Not obviously wrong — wrong in the specific, plausible way that survives a
skim and dies in a meeting, when the engineer who wrote the thing says *"that's not what that
does."* You are about to put your name on this in front of the person paying your rate, and your
entire credibility in the engagement is one confidently stated false claim away from gone.

Verifying all of it costs the time you just saved. So the question is not *whether* to verify.
It is *which claims*.

## Options

| Option | Real trade-off |
|---|---|
| **A. Trust it and ship** | Keeps the whole time saving. Works right up until the one wrong claim is the one an internal engineer disputes in front of the founder — and that engineer is often motivated to find it. |
| **B. Verify everything before it leaves your machine** | Zero risk of the meeting going badly. Also zero time saving; you have just paid for a tool to produce a first draft you then re-derive by hand. |
| **C. Verify by claim class, with a fixed rule** | Keeps most of the saving and removes most of the risk. Requires you to have the rule. The rule is this artifact. |
| **D. Ship it, but hedge the language throughout** | Feels safe. Reads as uncertain, which is the one thing a founder is not paying $250/hr for. Hedging everything is indistinguishable from knowing nothing. |

## The call

**C.** Trust the agent on claims about **structure**; never trust it on claims about **history,
intent, absence, or production**; and personally verify every claim that appears in the written
assessment as a **number** or as a **named risk**.

| Class | Example claim | Default |
|---|---|---|
| **Structure** — what exists, where, how it is wired | "Auth is a middleware in `api/middleware/auth.ts`; three services call it" | **Trust.** Derived from text that is in the repo. Spot-check one in five. |
| **Quantity** — counts, sizes, versions, coverage | "42% test coverage", "Django 3.2" | **Verify by running the thing that produces the number.** Never quote a number an agent inferred rather than read. |
| **Absence** — what is missing | "There are no integration tests", "nothing calls this" | **Never trust.** See below. |
| **History and intent** — why it is like this | "This was built as a temporary workaround" | **Never trust.** Ask a human. It is also the best question you can ask one. |
| **Production reality** — what actually runs | "The worker runs on a five-minute schedule" | **Never trust the repo.** Get the deploy config, the dashboard, or the actual crontab. |

The rule as it goes in the deliverable:

> **Verify anything you would be embarrassed to be wrong about in front of the client's board.**

## Why

The failure is not hallucination in the folk sense — agents rarely invent a file that does not
exist. The failure is **reasoning correctly over an incomplete view**, which produces claims that
are locally well-supported and globally false. Those are much harder to catch than invented ones,
because everything the agent cites is real.

**Absence claims are the one that ends engagements.** An agent can only see what it retrieved.
It says "there are no integration tests" and it is right about the repository it read — and
wrong, because the tests live in a separate `-e2e` repo that nobody thought to mention. It says
"nothing calls this endpoint" and it is right about the codebase — and wrong, because it is
called by a cron job defined in the infrastructure repo, or by a mobile client on a two-year-old
release, or by a customer's integration. You cannot prove a negative from a partial view, and
the assessment is where negatives are most tempting to state, because negatives sound decisive.

**Repository is not production.** This one is cheap to get wrong and expensive to be wrong about:
config in the repo is not the config that is deployed, the branch you cloned may not be what
shipped, and the feature flag defaults in code are not the flag values in the live account. Ask
for the deploy pipeline and one production config dump before you believe anything about runtime
behaviour. If you cannot get it, say "in the repository" in every sentence that needs it — that
qualifier is precise rather than hedging, which is why it is the one hedge worth keeping.

What was tried and failed:

- **Asking the agent to rate its own confidence.** The confidence scores correlate with how
  well-written the claim is, not with whether it is true. Useless as a filter.
- **A second model as a checker.** Both models read the same partial view and agree. Agreement
  between two models is evidence about the retrieval, not about the code.
- **Verifying by asking the client's engineers to review the draft.** They do catch the errors.
  They also now know your assessment was agent-generated and unverified, which costs more than
  the errors would have.
- **Blanket hedging** (option D). One senior founder's feedback, roughly: *"I can't tell which
  of these you're sure about."* That is the whole problem in one sentence.

**What upgrades a claim:** an agent with tool access that actually **executes** — runs the test
suite, greps the whole tree, resolves the dependency graph, hits the endpoint — produces
evidence, not inference. A claim backed by a command you can see and re-run moves from
"verify by hand" to "trust, spot-check". This is the single biggest lever on the cost of this
decision, and it is why the orientation workflow (`wf-0001`) insists the agent runs commands
rather than reads.

## When this is wrong

- **Small or greenfield repos** (say, under ~20k lines). You can read the whole thing in an
  afternoon. Don't build a verification protocol around a system you can hold in your head.
- **When the agent has full execution access and the repo is self-contained** — monorepo, tests
  runnable locally, deploy config in-tree. Absence claims become checkable, and the "never
  trust" row softens to "verify cheaply".
- **Internal notes, as opposed to client-facing writing.** Speed beats precision for your own
  map. The rule applies at the boundary of the deliverable, not to your thinking.
- **When the client explicitly wants a fast, rough, caveated read** and has said so in writing.
  That is a different product and it is legitimate — just make sure "rough" is in the document,
  not only in the conversation.

## Expiry trigger

- **Agents gaining reliable retrieval across an organisation's full code estate**, not just the
  repo in front of them. That is what makes absence claims trustworthy, and it moves the biggest
  row in the table. Watch for it directly.
- Default file-and-line citation in agent output: changes the *cost* of verification enough to
  change the rule.
- Any model release that materially changes long-context recall over large repositories.
  **Re-run this artifact's eval against every new frontier model** — this decision is the most
  model-dependent one in the catalogue and will go stale first.
