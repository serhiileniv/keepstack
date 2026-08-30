---
name: "no-ai-slop"
url: "https://github.com/petergyang/no-ai-slop"
what: "Strips 20+ named patterns out of AI prose — the ones you can point at, not a vibe"
sync: false
kind: skill
group: writing
mine: false
last_checked: 2026-08-30
upstream_pushed: 2026-08-06
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [claude-code, skill, writing, codex]
---

## Why

It names the patterns instead of asking for "more human", and that's the whole difference. Binary
contrasts ("It's not X. It's Y"), throat-clearing openers, faux-insight setups, colon reveals,
dramatic one-line fragments, importance puffery, synonym cycling, fake-profound endings — twenty
or so, each one a thing you can point at in a draft. A named pattern is checkable. "Sounds like
AI" is a feeling, and you can't edit against a feeling.

Three modes matter in practice: it edits and tells you what it removed, it detects without
editing, and it will deliberately generate slop if you want to see the patterns exaggerated.

**Newest thing in the hub** — added on the strength of the method, not yet on a piece I've
published.

## Watch out for

A pattern-stripper is only as good as its false-positive rate. Several of these patterns are
fine prose when you meant them; the risk is flattened voice, not slop.
