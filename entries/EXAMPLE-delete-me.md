---
name: "Example Entry (delete this file)"
url: "https://example.com"
what: "Shows the entry format — replace with something real"
kind: tool
verdict: dropped
mine: false
last_checked: 2026-08-30
checked_against: ["claude-code 2.x", "opus-5"]
tags: [example]
---

## Why

This file exists so `build.py` has something to render on the first run. **Delete it before
publishing anything.**

A real `dropped` entry says what actually went wrong and how long it took to find out — for
example: *"Used it for two weeks. The indexing step re-ran on every session start and added
~40s before the agent did anything. Fine on a small repo, unusable on a large one. Switched
back to plain ripgrep."*

That paragraph is the whole value of the entry. Vague dismissals ("not for me", "didn't click")
are worth nothing to a reader and make the rest of the hub look unserious.

## Watch out for

Publishing a verdict on something you haven't actually run. See D9 in `../../DECISIONS.md` —
one fabricated entry makes every other entry unverifiable.
