---
name: "own-this"
url: "https://github.com/serhiileniv/skills/tree/main/skills/own-this"
what: "Turns a shipped PR into a study guide, ending with the questions a reviewer will ask"
kind: skill
group: writing
mine: true
last_checked: 2026-08-30
upstream_pushed: 2026-08-07
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [review, learning, pr, skill]
caveman: "ROBOT WRITE CODE. THIS MAKE YOU UNDERSTAND CODE. NOW YOU DEFEND."
---

## Why

Shipping with an agent leaves a specific gap: the work is correct and you can't fully explain it.
That's fine until a reviewer asks, or an interviewer does.

`/own-this` closes it by writing a self-contained HTML study guide for a finished piece of work,
structured on how people actually retain things rather than how a diff is ordered: the concepts
and system map you need *before* the story, context through one analogy, the fix stated in one
sentence before any detail, the hardest subtlety told as a story, guided code reading with
plain-English translations, a mini-glossary, and a **"defend it"** part — self-check questions
with hidden answers, the challenges a reviewer is likely to raise, and a speakable 30-second
answer.

It's user-invocable only (`disable-model-invocation: true`). It should never fire on its own —
it's something you reach for after the work is done.

## Setup

```bash
cp -r skills/own-this ~/.claude/skills/own-this
```

Restart the session, then `/own-this`. Takes an optional target (PR URL, commit range, topic —
defaults to the session's main work) and `lang: uk` for a Ukrainian guide.

## Watch out for

The skill is a directory, not one file: `SKILL.md` plus `STYLE.md`, `template.html` and
`example.html` that it loads on demand. Copy the whole directory or the output loses its shape.
