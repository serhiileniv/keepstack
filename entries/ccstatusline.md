---
name: "ccstatusline"
url: "https://github.com/sirmalloc/ccstatusline"
what: "The everything status line — widgets, powerline, themes, usage meters, git and CI, all configured in a TUI"
sync: false
kind: tool
group: terminal
mine: false
last_checked: 2026-08-30
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [claude-code, statusline, terminal]
---

## Why

This is the status line most people should start with, and the reason is the TUI: you run it, you
see every widget rendered live, you drag them into the order you want, and you're done. No config
file to learn.

What it puts on the line goes well past model and context — token counts, session and weekly usage
against your limits, git branch, PR and CI state, powerline separators, themes. Context length
resets correctly straight after a `/compact` rather than showing the pre-compaction number, which
is the kind of detail you only get from a project that's been maintained hard.

The one thing to know before installing: Claude Code runs the status line command **on every
assistant message** and cancels the one still in flight when the next update lands. So every
render pays your runtime's startup, and a status line that does more work has more to lose in that
race. That cost is the whole reason [ctxline](../ctxline/) exists — it does one thing so it can be
a ~3ms binary. If you want widgets, this is the right trade; if you only ever look at the context
number, it isn't.

## Setup

```bash
bunx ccstatusline@latest      # or npx ccstatusline@latest
```

Opens the configurator and writes `~/.claude/settings.json` for you. Restart Claude Code
afterwards — `settings.json` is read at startup.

## Watch out for

It writes your `statusLine` entry in `settings.json`, so it will replace whatever was there.
Back that file up first if you already had one configured.
