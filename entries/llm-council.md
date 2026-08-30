---
name: "llm-council"
url: "https://github.com/aiwithremy/claude-skills-llm-council"
what: "Runs a decision past five advisors with different lenses, has them peer-review, then a chairman gives the verdict"
sync: false
kind: skill
group: planning
mine: false
last_checked: 2026-08-30
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [decisions, planning, review, skill]
---

## Why

Ask one model a question and you get one answer. It might be excellent. You have no way to tell,
because you only saw one.

This runs the question past five advisors who each think from a deliberately different angle, has
them peer-review each other anonymously, then a chairman synthesises the lot — telling you where
they agreed, where they clashed, and what to actually do. It's Karpathy's LLM Council method, but
where he dispatches to five different *models*, this uses sub-agents with five different *lenses*
inside Claude. No API keys, no second provider, no cost beyond the tokens.

The disagreement is the product. A single answer reads as confident whether or not it should; five
that split three-two tell you the decision is genuinely close, which is the thing you actually
needed to know.

It's honest about its own scope, which is rare — the skill's own description refuses to fire on
factual lookups, creation tasks or a "should I" with no real tradeoff. Reach for it when being
wrong is expensive and you're weighing options, not when you want a second opinion on a one-liner.

Pairs with [grilling](../grilling-skill/): grilling finds the questions you haven't answered,
this one argues about the answer once you have it.

## Setup

One file, no terminal:

```bash
mkdir -p ~/.claude/skills/llm-council
curl -o ~/.claude/skills/llm-council/SKILL.md \
  https://raw.githubusercontent.com/aiwithremy/claude-skills-llm-council/main/SKILL.md
```

Trigger it with "council this", "pressure-test this", or "war room this".

## Watch out for

**No licence file.** The repo has none, which means default copyright — you can read it, but you
have no granted right to redistribute or adapt it. Fine for personal use, a problem if you were
going to fork it into something you ship.

**Five advisors plus peer review plus synthesis is a lot of tokens** for one question. That's the
correct trade for a real decision and a waste on anything else, which is exactly why the trigger
list is written as narrowly as it is.
