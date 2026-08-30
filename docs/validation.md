# How we validate

Two different things need validating, and conflating them is a classic way to fail slowly:

- **Artifact validation** — does this thing work? (Gates A–C)
- **Market validation** — does anyone want it? (Gate M)

An artifact can pass every technical gate and still be worthless. Gate M is the one that
decides whether the business exists.

---

## Gate A — Does it work at all? *(author gate)*

Runs before an artifact leaves `draft`.

- [ ] Executed from a **fresh session**, no prior context, no author hand-holding.
- [ ] Run against **at least two models** (one frontier, one cheaper) — record both in
      `verified_against`.
- [ ] Produces a **worked example** committed to `examples/<id>.md`. This is not optional
      and not a screenshot; it's the actual input and output.
- [ ] A person who is not the author can follow it without asking a question.

**No worked example → the artifact does not exist.** This single rule is what keeps the
catalogue honest, and it's the rule that will feel most annoying to follow.

---

## Gate B — Is it worth money? *(outcome gate)*

Runs before an artifact is marked `verified` and priced.

- [ ] **Baseline measured:** how long does this task take without the artifact? Time it once,
      for real. Don't estimate.
- [ ] **With-artifact measured:** time it again.
- [ ] The `outcome:` field states the measured pair, e.g. `"45 min -> 5 min"`.
- [ ] The saving clears the bar: **≥ 20 minutes saved per use, or ≥ 1 use per week.**
      Below that, the buyer won't change their habits and won't renew.

Estimated numbers in `outcome:` are forbidden. The one sentence a buyer actually reads is that
number, and if it's invented, the product is a lie and the maintenance promise is worthless.

---

## Gate C — Does it *still* work? *(freshness gate — this is the moat)*

The recurring pass. **Monthly**, non-negotiable, calendared.

1. List every artifact where `expires` is within 30 days.
2. Re-run its `eval`.
3. Outcome:
   - **Passes** → bump `verified_on`, push `expires` out 90 days.
   - **Fails** → flip `status: stale` **immediately and publicly**, then fix or retire it.

**A stale artifact is marked stale on the day it fails, not on the day it's fixed.** Publishing
our own failures is counterintuitive and is precisely what makes the maintenance claim credible
— anyone can claim to maintain something; only a maintainer publishes breakages.

Every fix goes into a monthly changelog email to customers. That email is the product renewing
itself: it is the single most valuable thing we send, because it is proof.

---

## Gate M — Does anyone want it? *(market gate)*

This one decides whether to continue. Validate in this order, cheapest first:

| Step | Test | Cost | Kill signal |
|---|---|---|---|
| M1 | Post 2 artifacts free. Do strangers use them? | Hours | No engagement from anyone outside your network |
| M2 | Landing page with a price + "notify me". Do people click through to checkout? | 1 day | Traffic, zero checkout starts |
| M3 | Ask 20 qualified people directly. Do ≥3 say "yes, send it"? | Days | Fewer than 3 |
| M4 | **Do 10 strangers pay?** ← Rung 2 | Weeks | <3 sales after a full outreach cycle |

**Rules for Gate M:**
- Only strangers count. A friend buying is a favour, and reading it as data is how people
  spend a year building for an audience of one.
- "This is great!" is not validation. A card charge is validation.
- If M4 fails, the failure is almost always the **segment or the offer**, not the content.
  Re-examine [ADR-002](decisions/ADR-002-target-customers.md) before writing more artifacts.
  Producing more inventory is the most comfortable way to avoid this conclusion.

---

## Gate D — Community validation *(Phase 4 only, not now)*

If the platform in [ADR-007](decisions/ADR-007-platform-vision.md) ever unlocks, contributed
artifacts need validation we don't do by hand. The mechanic, recorded so it isn't reinvented:

- Every contribution requires a worked example. Same rule as Gate A, enforced by the form.
- Readers mark **"worked for me" / "didn't work for me"** against a specific model + date.
  This is the Stack Overflow mechanic and the reason that model works: reputation attaches to
  reproducibility, not to opinion.
- Artifacts auto-flip to `stale` when recent reports skew negative — **freshness becomes
  crowd-sourced.** This is the only known way the maintenance moat scales past one operator,
  and it is the strongest argument for the platform eventually existing.
- Contributor reputation is earned from artifacts that stay verified over time, not from volume.
