# How it reaches people

The companion to [artifact-spec.md](artifact-spec.md). That document is the **content model** —
what an artifact is. This one is the **delivery model** — where artifacts live, how a buyer gets
them, what the portal eventually looks like, and what deliberately does not exist yet.

Decisions behind it: [ADR-010](decisions/ADR-010-distribution-surface.md) (the surface),
[ADR-004](decisions/ADR-004-distribution.md) (the channels),
[ADR-005](decisions/ADR-005-no-product-before-revenue.md) (the gate).

---

## 0. The one principle

> **The delivery target is the buyer's filesystem, not a web page.**

They run agentic tooling. A skill is useful in a directory their agent reads. A workflow is
useful open next to their terminal. Nobody logs into a website to read Markdown they then have
to copy out by hand.

The web surface therefore does three jobs, and only these three:

1. **Be found** — someone with the problem discovers this exists.
2. **Be bought** — one page, one price, one button.
3. **Show it is current** — the freshness signal, which is the only thing here a free GitHub
   repo cannot reproduce.

Everything below is that principle applied. When a design question comes up later, re-derive the
answer from this line rather than re-arguing it.

---

## 1. The surfaces

| # | Surface | Job | Audience | Exists from | Built with |
|---|---|---|---|---|---|
| S1 | **Public repo** — free artifacts | Reach, format demo, contribution intake | Developers | Phase 2.1 | GitHub, generated from the private catalog |
| S2 | **Offer page** — one static page | Convert | Consultants | Phase 2.3 | Next.js on Vercel ([ADR-006](decisions/ADR-006-stack.md)) |
| S3 | **Checkout** | Take money, deliver files, issue a key | Consultants | Phase 2.4 | Polar |
| S4 | **The delivered product** — a git repo | The actual thing they use | Buyers | Phase 2.4 | zip + clone instructions |
| S5 | **Changelog email** | Renew the product monthly | Buyers | Phase 3.2 | Polar's customer list |
| S6 | **The portal** | Browse + freshness signal | Both | **Phase 3.5** | static, generated from `index.json` |
| S7 | ~~Contribution platform~~ | — | — | **Phase 4, gated** | see [ADR-007](decisions/ADR-007-platform-vision.md) |

**S1–S5 are the entire business until Rung 2.** They can all be standing inside a week. S6 does
not begin until people have paid for S4.

---

## 2. What the buyer actually receives (S4)

A git repository. Delivered as a zip through Polar, with a clone URL in the receipt.

```
kotkot-week-one/
  README.md              ← start here: the named task, and which file to open first
  CHANGELOG.md           ← what changed, when, and what broke. The receipt.
  index.json             ← generated. Everything, with verification dates.
  decisions/             dec-NNNN.md
  workflows/             wf-NNNN.md
  skills/                skill-NNNN/SKILL.md    ← drops straight into an agent's skills dir
  configs/               cfg-NNNN.md
  examples/              <id>.md                ← the worked examples ship WITH the product
  evals/                 <id>.md                ← so they can re-verify us
```

Four things here are deliberate and each is a sales argument:

- **`examples/` ships.** The worked example is the proof; withholding it would be withholding
  the evidence. It is also the part that is hardest to fake, so it should be in the buyer's
  hands.
- **`evals/` ships.** The buyer can re-run our verification themselves. Publishing the test
  alongside the claim is what separates "verified" from "we say so".
- **`CHANGELOG.md` ships from day one**, even when it has one line in it. It is the artifact
  that proves the maintenance promise is a practice, not a marketing claim.
- **Updates are `git pull`.** No re-delivery problem, no attachment emails, no version confusion.

**Install instruction, and it should be this short:**

```bash
git clone <url> ~/kotkot-week-one
ln -s ~/kotkot-week-one/skills/* ~/.claude/skills/     # optional
```

If onboarding needs more than four lines, the format is wrong.

---

## 3. The free/paid split (S1)

One source of truth, two distributions — the rule is already in
[artifact-spec.md](artifact-spec.md) §3 and is made concrete here.

```
private catalog/  ──generate──┬──▶  public repo   (tier: free)
   (this repo)                └──▶  paid zip      (all tiers)
```

The generator, roughly thirty lines, run manually:

1. Read frontmatter across `catalog/**`.
2. Emit `index.json`: id, type, title, job, outcome, status, `verified_on`,
   `verified_against`, `expires`, tier.
3. Copy `tier: free` artifacts **plus their examples and evals** into the public repo.
4. Copy everything into the paid bundle.
5. Regenerate both `README.md` files and both `CHANGELOG.md` files from `index.json`.

**Rules:**

- The free artifacts are **complete and real**, not teasers. A weak free sample proves the paid
  one is weak too ([ADR-004](decisions/ADR-004-distribution.md)).
- Free artifacts carry the same freshness metadata and the same gates. A stale free repo
  discredits the paid promise.
- `index.json` is generated, never hand-edited. It becomes the database in Phase 3 and the
  contribution schema in Phase 4 — same fields, no migration.
- **Write the generator in Phase 2.1. Not before.** Until there are free artifacts to publish,
  it is product surface with no product behind it.

---

## 4. Contribution intake (from Phase 2.1)

Contribution is Phase 4 ([ADR-007](decisions/ADR-007-platform-vision.md)). The **measurement**
of contribution pressure starts now, because ADR-007's unlock condition 3 —
*three people contribute something good, unprompted* — is unmeasurable while there is no way for
anyone to contribute anything.

Two issue templates on the public repo. Nothing else — no CONTRIBUTING.md, no PR process, no
promise to merge.

**`This broke for me`**
> Artifact ID · Model and date · What you expected · What happened · Repo type if relevant

Feeds Gate C directly and is genuinely useful the day someone files one.

**`I have a decision`**
> Free text. "When X, choose Y, because Z."

Files against ADR-007 condition 3. Track the count in [metrics.md](metrics.md).

Also watch **who** files good issues. Per ADR-007, they are the first ten contributors.

---

## 5. The portal (S6) — Phase 3.5, specified now so it is not redesigned later

Static, generated from `index.json`. No accounts, no database, no search backend. Three screens.

### Screen 1 — the catalog

Not a feed. Grouped by **job to be done**, because that is how the buyer arrives:
*"I'm starting an engagement Monday."*

```
┌────────────────────────────────────────────────────────────────────────┐
│  Week one with a new client                                            │
│                                                                        │
│  ▸ Unfamiliar-codebase orientation            wf-0001                  │
│    clone → defensible mental model                                     │
│    ⏱ 9 hrs → 2 hrs      ✅ verified 30 Aug · opus-5, sonnet-5          │
│                                                                        │
│  ▸ When to trust an agent's read of a codebase  dec-0003     [ FREE ]  │
│    the four claim classes that are never safe to ship                  │
│    ⏱ —                  ⚠️ stale since 12 Sep · fix in progress        │
│                                                                        │
│  Reporting to a non-technical founder                                  │
│  ...                                                                   │
└────────────────────────────────────────────────────────────────────────┘
```

**Row anatomy** — four elements, in this priority order:

1. **The job**, in the buyer's words. Not the artifact type.
2. **The measured outcome.** The one sentence a buyer actually reads.
3. **The freshness badge** — `verified <date> · <models>`. This is the differentiated element.
   It is not a small grey timestamp in the corner; it is the second thing the eye lands on.
4. **Status colour**, including `stale` shown openly. **A `stale` badge in public is a feature.**
   A catalogue where nothing is ever stale is a catalogue nobody is checking.

No infinite scroll, no "trending", no view counts, no "new this week". Sort defaults to job,
never to date.

### Screen 2 — the artifact page

Free artifacts render in full. Paid artifacts render: title, job, outcome, the context section,
the freshness block — and then stop, with the price. The trade-off is deliberate: enough to
judge whether it is the right artifact, not enough to use it.

Fixed top block on every artifact page:

```
┌──────────────────────────────────────────────────────────┐
│  STATUS      verified                                    │
│  Verified    30 Aug 2026  ·  opus-5, sonnet-5            │
│  Expires     30 Nov 2026  ·  re-checked monthly          │
│  Outcome     9 hrs → 2 hrs   (measured, not estimated)   │
│  History     v1.2 — 12 Sep: rewritten after opus-5       │
└──────────────────────────────────────────────────────────┘
```

The `History` line links to the commit. **The git history is the maintenance audit trail**, and
exposing it is the cheapest credibility available.

### Screen 3 — the staleness log

The most valuable page on the site, and the least intuitive one to build.

```
  September 2026 — 6 artifacts re-verified, 2 broke

  ⚠️  12 Sep   dec-0003  stale     new frontier model qualifies
                                   absence claims unprompted — the
                                   core claim needs rewriting
      18 Sep   dec-0003  fixed     v2.0, rule narrowed to 2 classes
  ⚠️  12 Sep   cfg-0001  stale     permissions schema changed
      13 Sep   cfg-0001  fixed     v1.1
```

Public, dated, and it names our own failures. Anyone can claim to maintain something; only a
maintainer publishes breakages ([validation.md](validation.md) Gate C). This page is the
argument for the subscription, and it should be linked from the offer page.

### What the portal is not

| Not | Why |
|---|---|
| A feed | Rewards recency and volume; a capped, maintained catalogue would look abandoned |
| A forum or comment system | Phase 4, gated ([ADR-007](decisions/ADR-007-platform-vision.md)) |
| A prompt directory | [ADR-001](decisions/ADR-001-what-we-sell.md). We never use the phrase |
| Search-first | ~40 artifacts. Browsing by job beats search at this size, and search implies volume |
| Accounts | Phase 3.4, and only to check subscription status |
| A place to *use* the artifacts | §0. The filesystem is where they are used |

### URLs — fix them now, they outlive everything

```
/                       the offer (S2)
/catalog                screen 1
/a/<id>                 screen 2 — stable, id-based, never renamed
/changelog              screen 3
/free                   pointer to the public repo
```

`/a/<id>` uses the artifact id, never the title slug. Titles get rewritten; ids never do
([artifact-spec.md](artifact-spec.md): *stable, never reused, never renumbered*).

---

## 6. Build order, and the gates between

| Stage | Build | Gate to start |
|---|---|---|
| **Now** | Nothing. Verify `wf-0001` (Gate A + B) | — |
| **2.1** | Generator script · public repo · 2 free artifacts · 2 issue templates | ≥1 artifact verified |
| **2.3** | Offer page: named task, measured outcome, maintenance promise, one button | A real `outcome:` number exists |
| **2.4** | Polar product · paid zip · `CHANGELOG.md` | Offer page live |
| **3.2** | First changelog email | First Gate C pass done |
| **3.5** | Portal, screens 1–3, static | **10 paying strangers.** Not before |
| **4** | Contribution platform | All four ADR-007 conditions |

**The gate that matters is 3.5.** Building the portal is more pleasant than messaging thirty
strangers, and that is precisely why it comes after them (R2 in [risks.md](risks.md)).

---

## 7. Open questions

- [ ] **Domain and product name.** "KotKot" is the working name; the offer page needs a decision.
      Not blocking until Phase 2.3.
- [ ] **Bundle vs. à la carte.** Currently one $39 bundle ([ADR-003](decisions/ADR-003-pricing.md)).
      If buyers ask for single artifacts, that is a pricing ADR, not a surface change.
- [ ] **Does the buyer want to clone, or to read?** §0 assumes clone. Two unprompted requests to
      read instead reverses [ADR-010](decisions/ADR-010-distribution-surface.md). **Ask this in
      the Gate M3 conversations.**
