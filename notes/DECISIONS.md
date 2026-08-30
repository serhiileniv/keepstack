# Decisions

Append-only. New calls go at the bottom. Never edit a past entry — supersede it.

The startup-era decision log (12 ADRs, one file each) is in
[archive/docs/decisions/](archive/docs/decisions/). That weight was wrong for a pet project;
this is one flat file.

---

## D1 — It's a pet project, not a startup *(2026-08-30)*

One person, spare weekends, ~$12/yr budget. Goals are **helpful** and **reputation**, with money
a distant third.

Everything built before this — revenue phases, customer segments, pricing, outreach to 30 named
strangers — is archived. It was designed for a business, and the weight of the planning exceeded
the weight of the thing being planned.

**Why:** the earlier plan assumed the operator was a practising fractional CTO, writing artifacts
from professional recall. He isn't. Once that premise fell, the honest version was much smaller.

---

## D2 — Audience: developers using agentic coding tools *(2026-08-30)*

Claude Code, Cursor, Codex, agent CLIs, MCP servers.

**Why:** it's what I use every day. The content becomes a by-product of a normal working day
rather than a research project — which is the only structure a no-schedule, one-person project
survives.

---

## D3 — The unit is a dated entry, not an article *(2026-08-30)*

Every entry carries `last_checked` and `checked_against` (tool + model versions).

**Why:** the gap on the internet isn't a shortage of recommendations — it's that none of them
tell you whether they still hold. Every `awesome-*` list is undated and therefore worthless
within months.

**The second-order benefit, which is the real reason:** a visible date makes irregular
maintenance *honest*. "Last checked 3 months ago" is a fact the reader can weigh. That removes
any need to promise a cadence — and a missed cadence would be public failure at the one thing
the project claims to do.

---

## D4 — Three buckets, and "dropped" is the point *(2026-08-30)*

`mine` · `using` · `dropped`.

**Why:** everyone publishes recommendations. Almost nobody publishes what they tried and
abandoned, because it feels unhelpful. It's the opposite — it's the most useful and least
available information in the category, and it costs nothing to write because the trying already
happened.

---

## D5 — GitHub for the repo, Cloudflare Pages for the site *(2026-08-30)*

Both free. Repo on GitHub because that's where stars, issues and `git clone` live, and for this
audience the repo *is* the product. Site deployed from the same repo to Cloudflare Pages.

**Why Cloudflare over GitHub Pages** (both $0): unlimited bandwidth vs a 100GB soft cap; Workers
on the free tier if anything dynamic is ever wanted; and domains at cost price with no
second-year markup.

**Domain deferred** until there's traction. A repo needs no domain.

---

## D6 — Costs must never scale with users *(2026-08-30)*

No LLM calls on behalf of visitors. No accounts, no database, no backend. Static, or
client-side with the visitor's own key.

**Why:** at a $12/yr budget, one front-page day on a project that pays per-visitor inference is
a bill, not a success. This rules out most "AI website" ideas and it rules them out on purpose.

---

## D7 — No promised cadence *(2026-08-30)*

Time available is "bursts — nothing, then a whole weekend." So: no weekly post, no newsletter
schedule, no "updated every Monday."

**Why:** an earlier draft of this plan was built on a weekly *"what broke this week"* post. With
burst availability that would be missed, publicly, while claiming to be the project that keeps
things current. The dates on entries (D3) do the same job with no promise attached.

**Instead:** `build.py --stale` lists what's overdue whenever a free weekend appears.

---

## D8 — Cap at 15–30 entries *(2026-08-30)*

**Why:** the cap is what makes re-checking possible, and re-checking is the entire claim. Neura
Market has 27,000 workflows *because* nothing there is ever checked. Volume and verification are
opposites; this project picks verification.

---

## D9 — Nothing gets published that I haven't personally run *(2026-08-30)*

Including anything drafted with AI assistance. Drafts live in `hub/drafts/` until they've been
used for real.

**Why:** the whole value is "I tried this." A fabricated verdict — even a plausible one — makes
every other entry worthless, and it's undetectable from outside, which is exactly why the rule
has to be absolute rather than a judgement call.

---

## D10 — It's a hub, not a classifier. Supersedes D4 *(2026-08-30)*

No verdicts. The `using` / `dropped` / `watching` buckets are gone. Entries are grouped by the
moment you'd reach for the thing — **planning · writing & review · working in a codebase ·
terminal · connected services** — and nothing is ranked.

**Why:** the buckets made the site a judgement of other people's work, and the reading experience
was "here is my shelf, sorted." A hub is the opposite: everything on it is there because it's
good, and the reader's question is *which of these do I need*, not *which does he like most*.
Grouping by the moment of use answers that question; a verdict column doesn't.

**What this costs, stated plainly:** D4 argued the `dropped` list was the differentiator — the
one thing nobody else publishes. That's now gone, and with it the strongest SEO asset ("why I
stopped using X" is a query with volume and almost no honest answers). Milestone 0 in `PLAN.md`
required ≥3 dropped entries and no longer means anything.

**What survives, and is now the whole claim:** `last_checked` and `checked_against`. The date
was never a ranking, so removing the ranking doesn't touch it. Every entry still says the day I
personally confirmed it works, and no automation ever writes that date.

**Consequence for entries:** the `verdict` field is replaced by `group`, and `build.py --check`
now rejects a thin body on *any* entry rather than only on a dropped one — under a hub, an entry
that doesn't say why it's worth an afternoon has no reason to exist.

---

## D11 — Space Black, borrowed structure *(2026-08-30)*

The site is dark: `#0a0a0a` ground, `#111`/`#141414` cards, `#1f1f1f`→`#333` borders, 8px radii,
Montserrat + Inter + JetBrains Mono. The structure is Neura Market's, matched deliberately.

**Why:** it's the look I want, and their token set was worth copying rather than re-deriving.
The one substitution is the accent — their violet `#7c3aed` for my Muted Blue `#6F9EAA`.

**Note for the brand kit:** `~/.claude/skills/brand` is light-mode only *by design*, and says a
dark treatment is a decision for me rather than a value to derive. This is that decision, and it
currently lives only in `site/style.css`. `#6F9EAA` is banned as text there (2.71:1 on off-white)
but clears 7.4:1 on `#0a0a0a` — going dark is what makes the brand accent usable as type. If this
sticks, it belongs back in the kit as an agreed dark set.

---

## D12 — Two stones: emerald and ruby. Supersedes the palette half of D11 *(2026-08-30)*

The mark is an emerald and a ruby overlapping. **Emerald `#2ECC94` is the accent everywhere.
Ruby `#C4304A` is reserved for entries I built** — the rare stones — so the second colour carries
a meaning rather than decorating.

**Why:** the hub is a stash of things worth keeping, and gems say that in one shape. Giving ruby
a job (`mine`) rather than a mood is what stops it being a second colour for its own sake.

**Two constraints that shaped it, both measured rather than guessed:**

- **Ruby cannot be text.** `#C4304A` is 3.65:1 on `#0a0a0a` and `#D93C57` is 4.46:1 — both fail
  AA — and every red that passes stops reading as ruby. So ruby is a **fill** (white on it is
  5.43:1, which is what the `mine` pill is), and `--ruby-tx #E85C75` (5.86:1) is held back for
  the rare case it must be type.
- **Red and green is the pair colour-blind readers lose first.** Safe here only because the two
  never encode the same axis: emerald is chrome, ruby means *mine*, and the `mine` pill carries
  the word as well as the colour. If ruby ever becomes the sole signal for something, this breaks.

Stale dates moved from Soft Brown to amber `#E0A33E` (8.94:1), because a brown-red warning beside
a ruby-red badge was two reds meaning two different things.

**This departs from the brand kit.** `~/.claude/skills/brand` is a light palette built on Muted
Blue `#6F9EAA`, and D11 carried that one value across. This doesn't. The kit is untouched and
still governs everything else; emerald and ruby are the *site's* palette, not the brand's. If the
site becomes the public face, that's a conversation about the kit, not a thing to fix quietly.

**Still open:** the name. `AI Hub` is a category label rather than a name — `Stash` was the
strongest alternative and matches the metaphor — but renaming touches the repo, canonical URLs
and the deployed domain, so it stays until decided deliberately.

---

## D13 — Renamed to Keepstack *(2026-08-30)*

`AI Hub` → **Keepstack**. Repo, site, Pages project, and every canonical URL.

**Why:** "AI Hub" is a category label, not a name. Thousands of pages could carry it, it says
nothing about what's here, and it was never going to be available as a domain. Keepstack says the
thing in one word — the stack I keep — and it's a compound nobody else is using: `.me`, `.dev`,
`.sh`, `.io` and `.tools` were all unregistered when checked.

**Why not the prettier options:** `twostones` names the mark exactly and is the most ownable, but
it's mute — someone seeing it in a link has no idea whether it's tooling or landscaping. `carat`
is the most elegant single word and carries the gem metaphor, but sits one letter from `caret`,
which in a developer audience is a typo waiting to happen. The gem metaphor stays where it works,
which is the logo: visual and instant, no explaining. A name that needs decoding is the problem
being solved here, not the solution.

**Domain, undecided and deliberately not blocking:** `keepstack.me` is free for a year through the
GitHub Student Pack, then ~$20–30/yr. `keepstack.dev` is ~$12–15/yr at Cloudflare cost, forever,
and is on the HSTS preload list. Cheapest complete answer is to take the free `.me` *and* register
`.dev` for ~$12, make `.dev` canonical and 301 the `.me` at it — because moving domains after
traffic arrives costs far more than the registration ever does. Until then the site runs on
`keepstack.pages.dev`.

**Migration:** GitHub redirects `serhiileniv/ai-hub` to the new name indefinitely, so old repo
links and existing clones keep working. The old Pages project keeps serving until it's pointed at
the new one; nothing was indexed under it long enough to matter.

---

## D14 — It's a stash, not a personal rotation. Narrows D9 *(2026-08-30)*

The site collects **good** agent tooling. It does not claim every entry is in daily use.

**Why:** D9 said nothing gets published that I haven't personally run, and D10 replaced verdicts
with "if it's here, I use it". Together those made the hub a list of what one person happens to
have installed this month — which is both smaller and less useful than what it should be. The
value is the curation: finding the good ones and saying what they're for.

**What still holds from D9:** no fabricated experience. An entry describes what a tool does and
what to watch out for, drawn from the tool itself. It never invents an anecdote about using it,
never claims a result I didn't see, and never dresses up a guess as a verdict.

**What changes:** an entry no longer implies daily use, so no copy on the site says it does. The
hero says *tools, skills and workflows worth keeping*, and that's the claim — worth keeping, not
currently in my terminal.

**The dates still mean what they always meant:** the day I last confirmed the entry is accurate,
against the named versions. That's a claim about the entry, not about my habits, so it survives
this unchanged.
