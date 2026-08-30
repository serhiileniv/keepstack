---
name: "ctxline"
url: "https://github.com/serhiileniv/ctxline"
what: "Model and context size in your Claude Code status line. Nothing else."
kind: tool
verdict: using
mine: true
last_checked: 2026-08-30
upstream_pushed: 2026-08-21
checked_against: ["claude-code 2.1.251", "opus-5"]
tags: [claude-code, statusline, rust, context]
---

## Why

I wrote it because every status line I saw either printed nothing I needed or printed ten things
I didn't. The one fact that changes what I do next is how full the context window is, so that's
the only number on the line:

```
Opus 5 · 40k/1M
```

The count is colored by pressure — green normally, yellow past 60%, bold rose past 85%. The model
name is deliberately the quietest thing there: it changes at most once a session, so color on the
line means exactly one thing, which is how much room is left.

It's Rust for one reason. Claude Code **cancels an in-flight status line script** when a new update
arrives, so startup time is the only property that matters — a Node or Python script pays its
interpreter boot on every assistant message and loses the race. The binary is ~330KB and runs in
about 3ms. Claude Code already pipes a JSON payload containing a `context_window` object, so this
is a pure `stdin → stdout` filter: no transcript parsing, no subprocesses, no I/O of its own.

## Setup

```bash
curl -fsSL https://raw.githubusercontent.com/serhiileniv/ctxline/main/install.sh | sh
```

Downloads the binary into `~/.local/bin`, points `~/.claude/settings.json` at it, and backs that
file up first if it already existed.

## Watch out for

`settings.json` is read at **startup**. Restart Claude Code after installing or the line won't
change.
