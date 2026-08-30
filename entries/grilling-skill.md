---
name: "grilling — a skill that interviews you before it builds"
url: "https://github.com/serhiileniv/skills/tree/main/skills/grilling"
what: "Claude Code skill that stress-tests a plan by asking every open question in rounds before writing any code"
kind: skill
verdict: using
mine: true
last_checked: 2026-08-30
upstream_pushed: 2026-08-07
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [claude-code, skill, planning]
---

## Why

The failure mode I kept hitting wasn't bad code — it was code built correctly against an
assumption I was never asked to confirm. Agents fill gaps silently, and you find out three files
later.

This skill inverts that. It models the plan as a design tree and works it in **rounds**: every
question whose prerequisites are already settled gets asked at once, each with a recommended
answer, then it stops and waits. Answers reshape the tree and push the frontier outward. It's
done when the frontier is empty — every branch visited, nothing silently assumed.

The clause that makes it worth keeping is the last one: *finding facts is the agent's job, never
mine.* If a question needs something from the filesystem or a tool, it dispatches a sub-agent
rather than asking me — and doesn't block on it, so the rest of the round still gets asked.
Without that line the round degenerates into a quiz about my own repo.

## Setup

```bash
cp -r skills/grilling ~/.claude/skills/grilling
```

A second one-line skill with `disable-model-invocation: true` whose body is just
`Run a /grilling session.` gives you `/grill-me` as an explicit slash command.

## Watch out for

It's genuinely relentless — that's the point, but it makes it the wrong skill for a task you've
already decided. Invoke it for the decision, not for the implementation.
