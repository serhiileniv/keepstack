# ADR-010 — The surface: a catalog with a freshness column, not a feed

**Status:** Accepted
**Date:** 2026-08-30
**Relates to:** [ADR-001](ADR-001-what-we-sell.md) · [ADR-004](ADR-004-distribution.md) ·
[ADR-005](ADR-005-no-product-before-revenue.md) · [ADR-006](ADR-006-stack.md) ·
[ADR-007](ADR-007-platform-vision.md)

## Context

[ADR-004](ADR-004-distribution.md) decided the **channels** — free artifacts to developer
channels, paid offer to consultants. It never decided the **surface**: what the thing looks
like, where it lives, who can put content on it, and whether it needs accounts.

That gap keeps re-opening the question, so it gets answered here. Four questions, in the order
they were asked:

1. How do we distribute it?
2. Who posts — us, or other people?
3. Do we need an account system?
4. Is it a feed, a catalog, or something else?

## Decision

### The governing principle

> **The delivery target is the buyer's filesystem, not a web page.**

Our buyer runs agentic tooling. A skill is useful when it is in a directory their agent reads;
a workflow is useful when it is open next to their terminal. Nobody wants to log into a website
to read Markdown they then have to copy out by hand.

So the web surface is **not where the product is consumed.** It exists to do three things the
filesystem cannot: **be found**, **be bought**, and **show that it is current.** Every design
question below follows from that, and most of them answer themselves once it is stated.

### 1. How we distribute

Three surfaces. Only two of them exist before revenue.

| Surface | Purpose | Audience | Exists from |
|---|---|---|---|
| **Public GitHub repo** | The free artifacts. Reach, format demo, and the intake point for contribution signal | Developers (ADR-004 top of funnel) | **Phase 2.1** |
| **Polar** | Checkout, tax, file delivery, license key | Consultants | **Phase 2.4** |
| **One static page** | The offer: named task, measured outcome, maintenance promise, one button | Consultants | **Phase 2.3** |
| ~~The portal~~ | Catalog browsing + freshness signal | Both | **Phase 3.5**, not before |

The paid product ships as a **git repository the buyer clones**, delivered as a zip via Polar
with clone instructions. Not a PDF, not a Notion link, not a members' area. A repo is the format
that (a) drops straight into their tooling, (b) makes updates a `git pull`, and (c) makes the
maintenance promise mechanically visible — the commit log *is* the receipt.

### 2. Who posts: only us, for a long time

Single-author curation **is** the product ([ADR-001](ADR-001-what-we-sell.md)). Opening
contribution early destroys the one thing being sold. Contribution unlocks at Phase 4 under the
four conditions in [ADR-007](ADR-007-platform-vision.md).

**But we add the intake path now**, because ADR-007's condition 3 — *"three people have
contributed something good, unprompted"* — is currently unmeasurable. There is no way for anyone
to contribute anything, so the condition can never be met and the platform can never unlock.

Two GitHub issue templates on the free repo, and nothing more:

- **"This broke for me"** — model, date, artifact, what happened. Feeds Gate C directly.
- **"I have a decision"** — free text. No PR process, no contribution guide, no promise to merge.

Cost: an afternoon, once. It converts a locked door into a measurement instrument.

### 3. Accounts: no, until a subscription needs one

No accounts, no login, no email gate anywhere, until **Phase 3.4** introduces the subscription.
Then an account exists for exactly one reason: to know whether someone's maintenance
subscription is current. Not for profiles, not for saved items, not for personalisation.

Until then Polar's license key is the entire auth system, and the free repo is public.

An email gate on the free artifacts is explicitly forbidden by
[ADR-004](ADR-004-distribution.md) — it would suppress the reach that is their whole purpose.

### 4. A catalog with a freshness column — never a feed

**A feed is the wrong shape, and it is the most tempting wrong shape.** A feed rewards recency
and volume. Our catalogue is deliberately capped at ~40 artifacts and most weeks nothing new is
added — a feed would render a healthy, maintained, deliberately-small library as an abandoned
blog. It also makes the newest thing the most prominent thing, when the most prominent thing
should be the **most recently verified** thing.

So: a **catalog**, sorted by job-to-be-done, with one column nobody else has —

> `Last verified: 2026-08-30 · claude-opus-5, claude-sonnet-5 · expires 2026-11-30`

That row is the entire business rendered as UI. It is the visible difference between us and a
free GitHub repo of prompts, and it should be the most prominent element on every page.

And the corollary, which is counterintuitive enough to state as a rule:

> **The public staleness log is the most valuable page on the site.**

A dated, public record of what broke, when, against which model, and when it was fixed. Anyone
can claim to maintain something; only a maintainer publishes their own breakages
([validation.md](validation.md) Gate C). That page is the proof, and it is the page a
competitor cannot fake without doing the work.

## Reasoning

- **The surface follows the buyer's workflow, not the seller's convenience.** A portal is
  convenient for us (analytics, control, upsell). It is friction for a buyer whose agent needs
  files on disk.
- **Every one of the four answers above defers work.** No portal until Phase 3.5, no accounts
  until 3.4, no contributions until Phase 4. That is not caution for its own sake — it is
  [ADR-005](ADR-005-no-product-before-revenue.md) applied. The static page plus Polar can be
  standing by Friday; a portal cannot.
- **The freshness column is the only UI element that is genuinely ours.** Everything else — a
  list of artifacts, categories, search — is a solved, copyable interface. The verification
  metadata is the part that requires actually running the treadmill.
- **A repo as the delivery format makes updates free.** When Gate C fixes something, the
  customer runs `git pull`. Without that, every update is a re-delivery problem, and the
  maintenance promise becomes an email-attachment business.

## Alternatives rejected

| Option | Why not |
|---|---|
| **Portal first, then content** | Cold start with nothing in it. Also ADR-005: it is product surface before revenue. |
| **A feed / "latest AI workflows"** | Wrong shape for a capped catalogue, rewards volume, makes a maintained library look dead. Also drifts toward the prompt-directory positioning ADR-001 rejects. |
| **Notion / Gitbook as the product** | Reads well, delivers nothing to a filesystem. Copy-paste is the buyer's job then, and that is the job we are supposed to be removing. |
| **Members' area with accounts from day one** | Auth, sessions, password resets and support load, at zero revenue, for a product that is a folder of files. |
| **Email course / drip** | Turns a reference library into a schedule. Wrong for something you consult when a new engagement starts. |
| **Discord as the primary surface** | Real community potential, but content in Discord is unsearchable, unversionable and ungrantable. Fine as a channel; fatal as a home. |
| **Open contribution now** | ADR-007. Destroys curation, which is the product. |

## Consequences

- **The free repo must be maintained to the paid standard.** It is now also the contribution
  intake and the reputation surface. A stale free repo discredits everything
  ([ADR-004](ADR-004-distribution.md) already says this; it matters more now).
- **Two distributions, one source.** A generation step splits `tier: free` from `tier: paid`.
  Roughly thirty lines of script — write it in Phase 2.1, not before.
- **We will be asked for a portal before it is due.** By buyers who want to browse and by us,
  because building it is more pleasant than outreach (R2). The answer is Phase 3.5 and the
  gate is revenue.
- **`index.json` becomes load-bearing earlier than expected.** Generated from frontmatter, it
  drives the free/paid split, the freshness column and the staleness log. It stays generated,
  never hand-edited.

## What would reverse this

- Buyers say, unprompted and more than twice, that they want to *read* rather than *clone*.
  That would mean the audience is less tooling-native than ADR-008 assumes, and the surface
  should invert.
- The free repo produces reach but no crossover to paid after a full cycle — that is
  ADR-004's own reversal condition, and it would put the surface back on the table.
- Unprompted contribution pressure arrives early via the issue templates. That is ADR-007's
  reversal condition, and it arrives through the intake path this ADR adds.
