# Catalog

The inventory. Schema and rules: [../docs/artifact-spec.md](../docs/artifact-spec.md).
Validation gates: [../docs/validation.md](../docs/validation.md).

```
decisions/   dec-NNNN.md      "when X, choose Y, because Z"  ← the differentiator
workflows/   wf-NNNN.md       ordered procedure to an outcome
skills/      skill-NNNN/      SKILL.md + assets
configs/     cfg-NNNN.md      MCP / subagent / settings
evals/       <id>.md          how to re-verify — required before status: verified
examples/    <id>.md          the worked example — no example, no artifact
_templates/  start here
```

## Two rules that are not negotiable

1. **No worked example → the artifact does not exist.** Not `verified`, not shipped, not sold.
2. **`outcome:` is measured, never estimated.** Time the task without, time it with, record both.
   That number is the single sentence a buyer actually reads.

## Status lifecycle

```
draft ──Gate A──▶ (has worked example) ──Gate B──▶ verified
                                                      │
                                          expires ────┤
                                                      ▼
                                          Gate C ──▶ stale ──▶ fixed → verified
                                                            └─▶ retired
```

`stale` is set **the day an eval fails**, not the day it's fixed — and published. Publishing our
own breakages is what makes the maintenance claim credible. Anyone can claim to maintain
something; only a maintainer publishes failures.

## Phase 1 target mix (12 artifacts)

| Type | Count | Note |
|---|---|---|
| Decision | **4** | Hardest to write, the actual differentiator. Do these first, not last. |
| Workflow | 5 | What buyers think they're buying |
| Skill / Config | 3 | Zero-setup, directly loadable |

Catalogue cap: **~40**. That's the ceiling on what one person can re-verify monthly. The cap
is a feature — see [ADR-001](../docs/decisions/ADR-001-what-we-sell.md).
