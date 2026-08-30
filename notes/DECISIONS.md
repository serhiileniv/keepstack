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
