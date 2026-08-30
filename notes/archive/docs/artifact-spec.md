# What we distribute, and what we save

This is the content model. It is deliberately designed to be three things at once:
a **file format** now, a **database schema** in Phase 3, and a **contribution schema** in
Phase 4 if the platform ever happens. Getting it right now costs an afternoon; getting it wrong
costs a migration later.

---

## 1. The unit types

Six types. They compose: a Workflow references Decisions and Skills; a Skill may embed Prompts.

| Type | What it is | Why it exists | Sellable alone? |
|---|---|---|---|
| **Decision** | *"When X, choose Y, because Z"* — a choice point with trade-offs, evidence and an expiry | **The differentiator.** Nobody else sells this. It is what makes us a *decisions* vault and not another prompt site. | ✅ Yes |
| **Workflow** | An ordered procedure that reaches a named outcome | This is what buyers think they're buying | ✅ Yes |
| **Skill** | A packaged agent capability (`SKILL.md` + frontmatter, Claude Code / agent-skill format) | Directly loadable, zero setup | ✅ Yes |
| **Prompt** | A single reusable instruction | Only ever a *component*. Never sold standalone — see ADR-001 | ❌ Never |
| **Config** | MCP server configs, subagent definitions, settings snippets | High pain, low supply, rots fastest | ⚠️ Bundled |
| **Eval** | The test that proves an artifact still works | **The machinery of the moat.** Without evals, "maintained" is a marketing claim | ❌ Internal |

### Why "Decision" is the flagship type

A prompt is an artifact — copyable, commoditised, worth nothing.
A decision is *judgement* — it captures what someone learned by trying the alternatives and
watching three of them fail. That does not commoditise, it does not appear on GitHub in a
useful form, and it is exactly what a consultant is paying to skip.

It is also the only unit type that gets **more** valuable as the ecosystem changes, because
every model release creates new decision points. Prompts rot; decisions accumulate.

---

## 2. The record schema

Every artifact is a Markdown file with YAML frontmatter. Same schema for all six types.

```yaml
---
id: dec-0042                      # stable, never reused, never renumbered
type: decision                    # decision | workflow | skill | prompt | config | eval
title: "Subagent vs. single long context for multi-file refactors"
version: 1.2.0                    # semver: major = behaviour change, minor = improvement, patch = typo

# --- who it's for -------------------------------------------------------
segments: [solo-consultant, dev-team]
job: "Refactor a codebase across 20+ files without losing coherence"
                                  # the NAMED recurring task. If this is vague, the artifact is unsellable.

# --- the promise --------------------------------------------------------
outcome: "3 hrs -> 25 min"        # MEASURED, not estimated. See validation.md Gate B.
evidence: examples/dec-0042.md    # the worked example. No example = not shipped.

# --- freshness (this is the moat) ---------------------------------------
status: verified                  # draft | verified | stale | retired
verified_on: 2026-08-30
verified_against: [claude-opus-5, claude-sonnet-5]
expires: 2026-11-30               # forces re-verification. Non-negotiable field.
eval: evals/dec-0042.md           # how to re-check it

# --- graph --------------------------------------------------------------
requires: [skill-0007]
supersedes: dec-0031
superseded_by: null
tags: [refactoring, context-management]

# --- provenance (matters from Phase 4 onward) ---------------------------
tier: paid                        # free | paid
author: kotkot
license: proprietary
---
```

### Required body sections, by type

**Decision** — the flagship format:
1. **Context** — the situation that forces a choice
2. **Options** — each with its real trade-off, not a strawman
3. **The call** — what to choose, stated unambiguously
4. **Why** — the reasoning, including what we tried that failed
5. **When this is wrong** — the conditions under which the opposite call is correct
6. **Expiry trigger** — what change in the world invalidates this

Section 5 is what separates a decision from an opinion. Section 6 is what makes it maintainable.

**Workflow:** Goal → Preconditions → Steps → Worked example → Failure modes → Time saved
**Skill:** standard `SKILL.md` frontmatter + body, plus our frontmatter block above
**Config:** What it wires up → the config → verification command → known breakages

---

## 3. Where it lives

```
catalog/
  decisions/   dec-NNNN.md
  workflows/   wf-NNNN.md
  skills/      skill-NNNN/SKILL.md
  configs/     cfg-NNNN.md
  evals/       <id>.md
  examples/    <id>.md          # worked examples — the proof, shipped with the product
index.json                       # generated from frontmatter; becomes the DB in Phase 3
```

**Rules:**
- Flat files, git-versioned. Git history *is* the maintenance audit trail — and it's the
  receipt when a customer asks "do you actually update this?"
- `index.json` is generated, never hand-edited.
- Free artifacts live in a separate public repo, generated from the same source. One
  source of truth, two distributions (see ADR-004).

---

## 4. What we deliberately do NOT save

- **Anything without a worked example.** It isn't verified, so it isn't inventory.
- **Model-specific hacks with no stated expiry.** Guaranteed future embarrassment.
- **Anything we can't re-test.** If there's no eval, we cannot honour the maintenance promise
  on it, and the promise is the whole business.
- **Volume for its own sake.** The catalogue is capped at what one person can re-verify
  monthly. Current working cap: **~40 artifacts.** The cap is a feature.
