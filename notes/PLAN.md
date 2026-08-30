# The plan

One page. If it grows past that, it's turning into the thing in `archive/`.

## What it is

A public GitHub repo + a static site: the AI tooling I actually use, what I tried and
recommend, and what I tried and dropped. Every entry carries the date it was last checked and
the model/tool versions it was checked against.

## Who it's for

Developers using agentic coding tools — Claude Code, Cursor, Codex, agent CLIs, MCP servers.
Same tools I use daily, which is the only reason I can write it.

## The three buckets

| Bucket | What | Who else publishes it |
|---|---|---|
| **Mine** | Tools and workflows I built and use | Some people |
| **Using** | Third-party, tried, kept | Lots of people |
| **Dropped** | Tried, abandoned, and why | **Almost nobody** ← the valuable one |

The dropped list is the differentiator. It's free content — the trying already happened — and
it's what readers actually want and can't find anywhere.

## The one mechanic that matters

**Every entry shows when it was last checked.**

That's the whole product. Not a recommendation — a *dated* recommendation. It's also what makes
irregular maintenance honest instead of embarrassing: "last checked 3 months ago" is a fact the
reader can weigh, and it still beats an undated list. No cadence is ever promised.

When there's a free weekend: `python3 build.py --stale` lists what's gone quiet, re-check a
batch, bump the dates.

## Hosting

- **GitHub** — the repo. Where stars, issues and `git clone` happen. The repo *is* the product.
- **Cloudflare Pages** — the site, built from the same repo on push. Free, unlimited bandwidth,
  and Workers on the free tier if anything dynamic is ever needed.
- **Domain** — register at Cloudflare, ~$12/yr at cost with no renewal markup. **Not yet.**
  A repo first; the domain when there's traction.

## Scope

- **15–30 entries.** Not 40+. The cap is what makes re-checking possible at all.
- No accounts, no database, no backend, no LLM calls on behalf of visitors. **Costs must never
  scale with users** — one front-page day would otherwise be a bill.
- No contributions yet. Issues are open; that's enough to find out if anyone cares.

## Milestones — no dates, because the schedule is "bursts"

| # | Milestone | Proves |
|---|---|---|
| 0 | 10 entries published, all dated, including ≥3 in **dropped** | The format works |
| 1 | Site live on Cloudflare Pages | It's real and shareable |
| 2 | Posted once, somewhere it belongs (HN / Reddit / a Discord) | Anyone outside my head cares |
| 3 | One full re-check pass, dates bumped, published | The dating claim is true, not decorative |
| 4 | Someone I don't know opens an issue or PR | It's useful to a stranger |
| 5 | GitHub Sponsors enabled, or a first paid thing | It earns something |

**Milestone 3 is the real one.** Anyone can publish a list. The re-check is the whole claim, and
it's where every similar project quietly dies.

## What money looks like, honestly

$0–200/month in year one, if anything. Realistic paths, in order:

1. **Reputation → career.** The main one. Rates, offers, credibility. Not project revenue.
2. **GitHub Sponsors**, once there's traction.
3. **A paid kit** — everything installable in one command, kept current — only if people ask.

If money matters more than reputation, this is the wrong project; a $15 starter kit on Gumroad
would earn faster and build nothing lasting.

## How it dies

- **It becomes another dead list.** The default outcome. Only defense: milestone 3, repeatedly.
- **Promising a cadence and missing it.** Publicly failing at the exact thing being sold. So:
  never promise one.
- **Scope creep into the thing in `archive/`.** If a roadmap with phases appears, stop.
