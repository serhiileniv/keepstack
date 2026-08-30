---
name: "caveman"
url: "https://github.com/JuliusBrussee/caveman"
what: "Makes the agent answer in compressed, telegraphic English — same information, far fewer tokens"
sync: false
kind: skill
group: terminal
mine: false
last_checked: 2026-08-30
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [tokens, context, cost, skill]
---

## Why

*"Why use many token when few token do trick."*

The joke is doing real work. An agent's default register is padded — hedges, restatements, a
preamble before the answer — and you pay for every word of it twice, once in output and again
when it re-reads the transcript next turn. This strips the register and keeps the content:

> **Normal, 69 tokens:** "The reason your React component is re-rendering is likely because you're
> creating a new object reference on each render cycle. When you pass an inline object as a prop,
> React's shallow comparison sees it as a different object every time, which triggers a re-render.
> I'd recommend using useMemo to memoize the object."
>
> **caveman, 19 tokens:** "New object ref each render. Inline object prop = new ref = re-render.
> Wrap in `useMemo`."

Nothing was lost. The second one is arguably the better answer.

Version 2 goes after the other half of the bill — what the agent *reads* — with a proxy that
compresses context before the provider call and restores it byte-exactly. The repo reports 33.2%
fewer provider-counted input tokens on a pinned benchmark, which is the number worth checking
against your own usage rather than taking on faith.

## Setup

The skill on its own, which is the part that needs no proxy and no account:

```bash
git clone https://github.com/JuliusBrussee/caveman
cp -r caveman/skills/caveman ~/.claude/skills/caveman
```

Or both halves, including the input-side proxy:

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude
```

## Watch out for

**Licensing is split** — MIT on the CLI, BSL-1.1 on the proxy runtime. If you're putting this
anywhere near work code, read which half you're actually running.

**It changes the register everywhere, including where you don't want it.** Compressed prose is
right for a diagnosis and wrong for a commit message, a PR description, or anything a colleague
reads. Turn it off before you generate text that leaves your terminal.
