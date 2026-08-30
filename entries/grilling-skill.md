---
name: "grilling"
url: "https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling"
what: "Asks you every open question about a plan, in rounds, before it writes a line of code"
kind: skill
group: planning
mine: false
last_checked: 2026-08-30
upstream_pushed: 2026-08-24
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [claude-code, skill, planning]
---

## Why

If you've ever had an agent build the wrong thing correctly, this is the fix.

The failure isn't bad code. It's code written against an assumption nobody asked you to confirm
— the agent hit a gap, filled it silently, and you find out three files later.

`grilling` inverts that. It maps your plan as a design tree and works it in **rounds**: every
question whose prerequisites are already settled gets asked at once, each with a recommended
answer, then it stops and waits for you. Your answers reshape the tree and push the frontier
outward. It's done when the frontier is empty — every branch visited, nothing silently assumed.

The clause that makes it work is the one most people would leave out: *finding facts is the
agent's job, never yours.* When a question needs something from your filesystem, it dispatches a
sub-agent instead of asking you — and doesn't block, so the rest of the round still gets asked.
Without that line it degenerates into a quiz about your own repo, and you stop using it by day
three.

Pair it with `grill-me` from the same directory — a one-line skill with
`disable-model-invocation: true` that gives you `/grill-me` as an explicit command, so it fires
when you decide, not when the model guesses.

## Setup

```bash
git clone https://github.com/mattpocock/skills
cp -r skills/skills/productivity/grilling ~/.claude/skills/grilling
cp -r skills/skills/productivity/grill-me ~/.claude/skills/grill-me
```

## Watch out for

It is genuinely relentless — that's the point, and it makes it the wrong tool for work you've
already decided on. Reach for it at the decision, not at the implementation.
