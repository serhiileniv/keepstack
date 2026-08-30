# Market

> **Confidence note:** this is a reasoned read of the space, not a researched report. No
> market-size figures are cited because I have not verified any. Treat everything here as a
> hypothesis to be killed by customer conversations, not as data.

## What is dead

**Prompt marketplaces.** PromptBase and its clones peaked around 2023 and collapsed. Three
causes, all still true and getting worse:

1. **Models got good enough.** Prompt craft used to be scarce skill; now a mediocre prompt to
   a 2026-class model beats a brilliant 2023 prompt. The value of the artifact itself decayed.
2. **Infinite free supply.** GitHub, Reddit, X, Discord. Anything we sell exists free somewhere.
3. **Zero switching cost, zero lock-in.** A buyer uses a prompt once and never returns.

**Generic "500 prompts" packs and Notion prompt templates.** Same problem, plus they get
screenshotted and reshared within a week of launch.

## What is live

**Agent skills, Claude Code skills, MCP server configs, subagent definitions.**
This layer is roughly 18 months old, changes monthly, and is badly documented. That is real,
recurring pain. Important caveat: the default distribution here is a free GitHub repo, so the
competitor is $0 and we must be clearly better than free.

**Curation plus maintenance.** The scarce good is not the artifact. It is the sentence
*"this one works, on the current model, and I updated it when the API changed."* Nobody
wants to sell maintenance because it is boring and never ends. That is exactly why it is a moat.

**Role-shaped bundles.** "AI workflows for X" outperforms "AI workflows." A specific role
lets the buyer see themselves in the product and justifies a higher price. The narrower the
role, the higher the willingness to pay per unit of audience.

## Who we actually compete with

Ranked by how much damage they do to us:

| Competitor | Threat | Our answer |
|---|---|---|
| **Free GitHub repos** | Highest. Same content, $0. | Curation + verified examples + we maintain it. Their repo is stale in 3 months. |
| **The buyer's own inertia** | Very high. They don't buy anything. | Sell against a named, painful, recurring task — not against "AI productivity." |
| **Official vendor registries** (Anthropic/OpenAI shipping their own skill libraries) | Structural. Could eat the middle of the market. | Stay in the role-specific, opinionated layer they will never staff. |
| **Generic prompt sites** | Low. Already dying. | Don't position anywhere near them. Never use the word "prompt pack." |
| **Consultants doing it bespoke** | Low, different price point | We are the $49 version of their $5,000 engagement. |

## The window, and why it closes

The opportunity exists because agentic tooling is new, fragmented and undocumented. That
condition is temporary. It closes when either (a) the vendors ship good first-party libraries,
or (b) the tooling stabilises enough that documentation catches up. Estimate: 12–24 months,
unverifiable. Implication: **speed matters more than polish**, and the durable asset we should
be accumulating is the audience and the brand, not the content.

## The uncomfortable truth

Building is roughly 10% of this. Distribution is 90%. Anyone reading this doc who feels the urge
to go design a database schema should reread that sentence.
