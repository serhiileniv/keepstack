---
id: wf-0001
type: workflow
title: "Unfamiliar-codebase orientation — clone to defensible mental model"
version: 0.1.0
segments: [technical-consultant, fractional-cto]
job: "Week one of a new engagement: get oriented in a codebase you have never seen well enough to speak about it credibly"
outcome: ""                       # Gate B pending — measure baseline and with-artifact, never estimate
evidence: examples/wf-0001.md
status: draft
verified_on:
verified_against: []
expires:
eval: evals/wf-0001.md
requires: [dec-0001, dec-0003, cfg-0001, skill-0001]
tags: [week-one, orientation, codebase, wedge]
tier: paid
author: kotkot
license: proprietary
---
> **REFRAME NEEDED — retarget from "week one with a client" to new job / new repo / OSS contribution. Steps largely survive.** Niche changed in [ADR-011](../../docs/decisions/ADR-011-niche-change.md).


# Unfamiliar-codebase orientation

## Goal

By the end of this you can, without opening the repo: draw the system on a whiteboard, name
every way a request enters it, say where the money flows, and answer *"what happens when a
customer does X"* end to end. You can also name, precisely, the things you do **not** know —
which is the part that makes the rest credible.

Explicitly **not** the goal: an opinion on the code quality. That is `wf-0003`, and forming it
now will bias everything you read.

## Preconditions

- `dec-0001` settled — SOW clause signed, tooling permitted.
- `cfg-0001` scaffold in place: engagement directory, secret scan run, no production credentials
  anywhere near the agent.
- Read access to the repository **and** the ability to run its build and test commands. If you
  cannot run commands, this workflow degrades badly — see `dec-0003` on why executed evidence is
  worth more than inferred evidence.
- 30 minutes booked with the longest-tenured engineer, for **step 8**. Book it on day one; it is
  the hardest thing to get and the highest-value step.

## Steps

### 1. Map the estate before you open the repo *(20 min)*

The repository you were handed is almost never the whole system. Ask, in writing:

- Every repository, and who owns each.
- Where it deploys, and how a deploy happens.
- Every third-party service that holds data or runs code (payments, auth, email, queues,
  analytics, one abandoned Zapier account).
- Anything with a scheduled trigger.

**Done when:** you have a written list, and it is longer than one item. If the answer was "just
this repo", ask specifically about cron jobs, mobile clients and the marketing site — that
question finds a second repo about half the time.

### 2. Clone and make it safe *(15 min)*

Apply `cfg-0001`. Scan for secrets and customer data *before* pointing anything at the tree — an
`.env` committed in 2022 or a PII-bearing fixture is your exposure, not the model's terms.
Exclude any dump, fixture or archive that contains real customer records.

**Done when:** the scan is clean, or the offending paths are in the ignore file and on your
findings list for `wf-0003` (a committed secret is a **day-one, out-of-band** finding under
`dec-0004`, not an appendix item).

### 3. Get the mechanical facts by running commands, not by asking *(30 min)*

Every fact in this step must come from a command whose output you can re-run. This is the
"executed evidence" rule from `dec-0003`. Run — or have the agent run, showing its output:

- **Size and languages.** `tokei` / `cloc`. One number per language, and the ratio matters more
  than the total.
- **Dependency reality.** Every manifest in the tree, with versions and how far behind they are.
  A framework two majors behind is a schedule constraint on everything else you will recommend.
- **Who actually works here.** `git log --since=12.months --format='%an' | sort | uniq -c | sort -rn`
  — the difference between this list and the org chart is one of the most informative things you
  will learn all week.
- **Where the system actually lives.**
  `git log --since=6.months --name-only --format= | sort | uniq -c | sort -rn | head -30`
  — the thirty most-changed files. This is the real centre of the codebase, regardless of what
  the directory structure claims.
- **Whether it builds, and whether the tests pass.** Do this yourself, on your machine, on day
  one. How long it takes a competent stranger to get a green build is a finding in its own right
  and you can only measure it once.

**Done when:** you have raw command output saved in the engagement directory. Do not paraphrase
it yet.

### 4. Enumerate the entry points *(30 min)*

Not "the architecture" — the **doors**. Every way work enters the system:

HTTP routes · queue consumers · scheduled jobs · webhook receivers · CLI/admin commands ·
event subscriptions · anything a mobile or partner client calls directly.

Have the agent produce this list with a `file:line` for each, then spot-check one in five
yourself. Structure claims are the class you are allowed to trust (`dec-0003`) — spot-checking
is enough.

**Done when:** the list is exhaustive enough that you would be surprised by a new entry point.
Surprises at this stage are cheap; in week four they are expensive.

### 5. Trace the money path, end to end *(2–4 hrs, and this is the day that matters)*

Pick **one** vertical slice by a single criterion: *where a failure costs the business money
today.* Checkout, signup, the ingestion pipeline, the thing the client sells. Not the ugliest
code — see `dec-0002`.

Follow one real request from the door to the datastore and back: handler → service → data
access → schema → external calls → what gets written → what gets returned. Have the agent lay
out the chain with citations; **read the three to five files at the centre of it yourself.**

This is the step that produces the one non-obvious finding the engagement is actually judged on,
and it is the step under time pressure that people skip.

**Done when:** you can narrate the path aloud, in order, without notes.

### 6. Write the map *(45 min)*

`map.md` in the engagement directory. Not a deliverable — your instrument.

- Components and what each is responsible for, in one line each.
- Data stores, and what is authoritative for what.
- External services, and what breaks if each is down.
- Entry points from step 4.
- The money path from step 5, as a sequence.
- **Ownership:** who is the only person who understands each part. Single points of human
  failure are findings.

### 7. Write the unknowns list *(15 min — do not skip)*

Everything you could not determine from the code: intent, history, what is dead, what actually
runs in production, why a thing is the way it is. Under `dec-0003` these are exactly the claim
classes an agent cannot settle.

**Done when:** you have at least five questions no amount of further reading would answer.
Fewer than five means you have not noticed what you do not know yet.

### 8. Spend 30 minutes with the longest-tenured engineer *(30 min, highest value in the workflow)*

Take the unknowns list. Then ask these three, in this order:

1. *"What would you fix if you had a free week?"*
2. *"What breaks most often?"*
3. *"What's the thing everyone here knows that isn't written down anywhere?"*

Question 3 is the one. Expect the answer to reframe at least one item on your map.

**Done when:** the unknowns list is answered or explicitly marked "nobody here knows either" —
which is itself a finding, and usually a serious one.

## Worked example

See [`examples/wf-0001.md`](../examples/wf-0001.md). Real repository, anonymised client, real
command output, including the parts the agent got wrong.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| The map reads generic — true of any system of this type | You stayed in breadth and skipped step 5 | Do the vertical slice. Generic findings come from never touching a real code path. |
| You find a whole subsystem in week three | Step 1 was answered by one person from memory | Ask the deploy pipeline what exists, not a human. Deploy targets do not forget repos. |
| An engineer disputes a claim in the meeting | Trusted an absence or intent claim | `dec-0003`. Absence claims never ship unverified. |
| Ran out of week one | Step 5 expanded, or you traced three paths instead of one | One slice. `dec-0002` caps the ramp at three days for exactly this reason. |
| Everything looks like it needs rewriting | You formed a quality opinion during orientation | Orientation and assessment are separate passes on purpose. Park every judgement in the `wf-0003` inbox and keep reading. |
| Agent output confidently describes a framework version that isn't installed | Inferred from docs rather than read from the lockfile | Every version number comes from the lockfile, run as a command. Step 3 is not optional. |

## Time saved

Baseline: __ · With this: __ · Measured on: __

*(Gate B. Time an unfamiliar repo of comparable size without this workflow, then with it. Do not
fill this in with an estimate — see [validation.md](../../docs/validation.md).)*
