# Library

The actual files — the things people copy. An entry in `entries/` points here with
`source: library/...`, and `build.py` renders the contents on that entry's page so a visitor
can read and copy without cloning.

```
skills/     <name>/SKILL.md        agent skills, loadable as-is
workflows/  <name>.md              ordered procedures with real commands
configs/    <name>/                MCP configs, settings, permissions, subagents
```

**Rules:**

- **It has to be the version you actually run.** Not a cleaned-up teaching version. If your real
  one has a weird workaround in it, that workaround is the most valuable line in the file.
- **Strip secrets before committing.** Paths, tokens, client names, internal hostnames.
  Check twice — this repo is public.
- **One directory per thing**, so it can be copied wholesale.
- Files rendered on the site: `.md .json .yaml .yml .toml .sh .py`. Anything else is ignored by
  the builder — it will still be in the repo, just not on the page.
