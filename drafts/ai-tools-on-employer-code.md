---
id: dec-0001
type: decision
title: "Putting client code through AI tooling — what's allowed, and how to answer when they ask"
version: 0.1.0
segments: [technical-consultant, fractional-cto]
job: "Start an engagement using agentic tooling on a client's private codebase without creating a contract problem or a trust problem"
outcome: ""                       # Gate B pending — measure, never estimate
evidence: examples/dec-0001.md
status: draft
verified_on:
verified_against: []
expires:
eval: evals/dec-0001.md
requires: [cfg-0001]
supersedes:
superseded_by:
tags: [engagement-setup, confidentiality, contracts, week-one]
tier: paid
author: kotkot
license: proprietary
---
> **REFRAME NEEDED — becomes "what your employer's policy actually allows, and how to check". Currently written for client engagements.** Niche changed in [ADR-011](../../docs/decisions/ADR-011-niche-change.md).


# Putting client code through AI tooling

## Context

Day one of an engagement. There is an NDA, probably a two-page one the client's lawyer wrote for
a different purpose. You are about to clone a private repository and point an agent at it,
because that is the entire reason you can deliver a week-one assessment in three days instead of
ten.

Nobody has asked you anything yet. They will — usually in week three, usually in front of other
people, usually phrased as *"wait, is our code going to OpenAI?"* The answer you give at that
moment is decided now, by what you did on day one. There is no good answer available later if
you got day one wrong.

This is the first artifact in the catalogue because every other workflow we sell assumes it is
settled.

## Options

| Option | Real trade-off |
|---|---|
| **A. Ask permission per engagement, in writing, before cloning** | Survives any later question. But you are asking a non-technical founder to approve a thing they don't understand, in week one, when their default answer to any unfamiliar risk is "let me think about it" — which never resolves. You can lose the tool by asking for it. |
| **B. Just use it; disclose if asked** | Fastest, and it is what most consultants actually do. You are making an NDA interpretation on the client's behalf and betting they'd agree. Usually they would. The one time they wouldn't, it is not a disagreement — it is a termination. |
| **C. Local or self-hosted models only** | The disclosure problem disappears completely. So does most of the value: whole-repo reasoning is exactly the capability that degrades most on what you can run locally, and it is the only capability you were buying. |
| **D. Commercial tier with no-training / zero-retention terms, disclosed once as a standing clause in your own SOW** | Costs more per month and costs one paragraph of paperwork once. Removes the question permanently and makes the answer boring, which is the goal. |

## The call

**D, with A's paperwork folded into your standard SOW.**

Put a standing clause in the SOW you send every client. It names the *class* of tooling, states
the retention and training terms, and grants blanket permission for the engagement. Then never
ask again, and never use anything outside what the clause covers.

Draft clause, to adapt with your own lawyer:

> *Consultant uses commercial AI-assisted development tooling under business terms that
> prohibit training on submitted content and provide zero or limited retention. Client materials
> may be processed by such tooling in the course of the engagement. Consultant will not submit
> Client production credentials, customer personal data, or Client-designated restricted
> materials to any such tool. Client may withdraw this permission in writing at any time.*

Two operational rules that go with it, and matter more than the clause does:

1. **Scan before you clone, not after.** Secrets, `.env` files, database dumps and PII in test
   fixtures are the actual exposure. The model provider's retention policy is a contract
   question; a customer table checked into `fixtures/` is an incident. See `cfg-0001`.
2. **Ban the tool from production credentials, permanently.** Read-only access to code is a
   defensible position. Access to a live environment is not, and no clause makes it one.

## Why

The reasoning is about **who is being asked to make the decision**, not about the technology.

Asking per engagement puts a founder in the position of approving something where the downside
is vivid ("our code, a third party") and the upside is invisible to them (your speed, which they
assumed was just how fast you are). That asymmetry has one rational answer, and it is no. Once
the same fact is a line item in the SOW, alongside your laptop, your password manager and your
error-tracking account, it is a **term**, not a **request** — and terms get signed.

What was tried and failed:

- **Verbal disclosure at kickoff.** Everyone nods. Four weeks later nobody remembers it, there
  is no record, and you are now the person who says "I did tell you" — which reads as a defence
  regardless of it being true. If it is not in a document with a signature on it, it did not
  happen.
- **Asking after the fact, when it came up.** The question arrives with an audience. Answering
  it well requires paperwork you don't have yet, and the delay is what does the damage, not the
  substance.
- **Anonymising the code first.** Sounds responsible, is theatre. Identifiers, domain language
  and business logic are the code; stripping the client's name from it protects nothing and adds
  an hour per repo.
- **A separate one-page "AI usage addendum".** Better than nothing, worse than the SOW clause:
  a standalone document about AI invites a standalone conversation about AI. Burying it in the
  tooling section of the SOW gets it signed without a meeting.

The clause also does something the other options don't: it is **evidence of diligence**. If the
client is ever asked by *their* customer whether subprocessors touched the code, you have handed
them the answer in advance. That converts your biggest liability in the relationship into a
small demonstration of competence.

## When this is wrong

- **Regulated clients with a real DPA.** Healthcare, financial services, anything with a
  named data-processing addendum and a subprocessor list. Your SOW clause does not override
  their contracts with their customers. Work in their tenancy, on their approved tooling, or
  without agents. Ask their counsel, not their founder.
- **Government, defence, or anything with a clearance requirement.** Not a judgement call. No.
- **When you would be the named subprocessor.** If the client's own customer agreements require
  disclosure of subprocessors, your tooling may need to appear on a public list. That is a
  conversation with their legal team before day one, not a clause in your SOW.
- **When the client's engineering leadership has already banned the tooling internally.** Using
  it as the outside consultant, under your own terms, is technically defensible and politically
  fatal. You will not survive being the person with an exemption.
- **Very small or greenfield repos.** If you can read the whole thing in an afternoon, the
  benefit does not justify the conversation at all. Just read it.

## Expiry trigger

- Any change to the retention or training terms of the tooling named in your clause. **Re-read
  the terms whenever you renew a plan or change tiers** — the clause makes a factual claim, and
  a factual claim that quietly stops being true is worse than no clause.
- A provider introducing (or withdrawing) a tenancy or zero-retention option that changes what
  the clause should say.
- New deployer-side obligations under regional AI regulation that require disclosure beyond a
  contract term.
- The first time a client redlines the clause. Their edit tells you what the market's actual
  boundary is — rewrite this decision around it.
