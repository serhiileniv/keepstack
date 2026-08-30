# Roadmap — how we actually do this

**Target: 10 paying users / $100+.** Phases end on **exit criteria**, not on dates. The day
counts are effort estimates for a part-time operator, not deadlines.

---

## ✅ RESOLVED — niche locked

**Technical consultants & fractional CTOs.** See [ADR-008](decisions/ADR-008-niche.md) and the
[niche brief](customers/niche-fractional-cto.md).

**The wedge task:** *week one with a new client — orient in an unfamiliar codebase and produce
a written assessment credible enough to justify the rate.* Expensive, largely unbillable,
recurs every engagement, determines renewal, and highly amenable to agentic tooling.

---

## Phase 0 — Foundation ✅

- [x] Decision vault created (this repo)
- [x] North star, market read, segments, ADRs 001–007
- [x] Artifact schema and validation gates defined

**Exit:** done.

---

## Phase 1 — Inventory *(~5–7 days of effort)*

Build the thing. No selling yet, no site yet.

- [x] **1.1** Niche resolved — [ADR-008](decisions/ADR-008-niche.md)
- [x] **1.2** Qualifying task named — see the [niche brief](customers/niche-fractional-cto.md)
- [ ] **1.3** Edit the 15 seed candidates in the niche brief against **your own recall**. Cut what
      you haven't personally done; add what's missing. Recalled, not researched.
- [ ] **1.4** Cut to the 12 with the highest `outcome` (time saved × frequency).
- [ ] **1.5** Write all 12 to the [artifact spec](artifact-spec.md), starting from the templates
      in `catalog/`. Mix: **4 decisions,
      5 workflows, 3 skills/configs.** The decisions are the differentiator — do not let them
      get squeezed out because workflows are easier to write.
- [ ] **1.6** Run **Gate A** on all 12: fresh session, two models, worked example committed.
- [ ] **1.7** Run **Gate B** on all 12: measure baseline, measure with-artifact, record the real number.
- [ ] **1.8** Write evals for all 12 so Gate C is possible in month two.
- [ ] **1.9** Cut anything that fails a gate. **Shipping 8 verified beats 12 with 4 unproven.**

**Exit criteria:** ≥ 8 artifacts at `status: verified`, each with a worked example and a
measured outcome.

**Failure mode to watch:** writing 30 mediocre artifacts instead of 8 verified ones. Volume
feels like progress and is the most comfortable way to avoid Phase 2.

---

## Phase 2 — First revenue *(~7–10 days of effort)* ← **the phase that matters**

- [ ] **2.1** Pick the 2 best artifacts. Release them **free and ungated**. These are the ad.
- [ ] **2.2** Publish them where the dev audience is (GitHub + X/HN/Reddit/Discord). This is
      **reach**, per [ADR-004](decisions/ADR-004-distribution.md) — measure reach, not sales.
- [ ] **2.3** Landing page: one page, one offer, one price ($39), one button.
      Above the fold: **the named task**, the **measured outcome**, the **maintenance promise**.
- [ ] **2.4** Polar or Gumroad. Product, price, file delivery. *(under 1 hour)*
- [ ] **2.5** **Gate M3 — the part everyone skips.** Build a list of 30 named people in the
      niche who have publicly complained about the target task. Actual names, actual links.
- [ ] **2.6** Message all 30 individually. Not a pitch:
      *"I built this for [task]. Want it free for feedback?"*
      Expect ~10 replies, ~5 yes, ~1–2 who then pay or refer.
- [ ] **2.7** Ship free copies to everyone who says yes. **Ask each one: what would make this
      worth $39?** These answers are worth more than the sales.
- [ ] **2.8** Fix what they tell you is missing. Ship v1.1.
- [ ] **2.9** Second outreach round of 30, now with testimonials and a fixed product.
- [ ] **2.10** Ask every free recipient who used it for **one referral**. This is where most of
      the 10 will come from.

**Exit criteria:** **10 paying strangers, ≥$100 collected.**

**Kill criteria (be honest):** <3 sales after both outreach rounds → the **segment or the offer**
is wrong, not the content. Go back to [ADR-002](decisions/ADR-002-target-customers.md). Do not
respond by writing more artifacts.

---

## Phase 3 — Prove the moat *(gated on Phase 2)*

Product work unlocks here, and only against requests from people who paid.

- [ ] **3.1** Run the **first monthly Gate C pass.** Publish what broke, publicly.
- [ ] **3.2** Send the first changelog email. This email *is* the product renewing itself.
- [ ] **3.3** Grow to ~25 verified artifacts, driven by customer requests only.
- [ ] **3.4** Introduce the subscription (~$9–15/mo) — framed as *maintenance*, never as *access*.
- [ ] **3.5** Only now: consider a real site (search, accounts). Stack is pre-decided in
      [ADR-006](decisions/ADR-006-stack.md) so it isn't re-debated.

**Exit criteria:** 5 of the first 10 return — renew or buy again. **This is the real proof**,
harder and more meaningful than the first 10 sales.

---

## Phase 4 — Platform *(hard-gated — see [ADR-007](decisions/ADR-007-platform-vision.md))*

Stack Overflow / Hugging Face for AI decisions. Do not start until **all four** unlock
conditions in ADR-007 are met — especially condition 3: *three people have contributed
something good, unprompted.* If nobody contributes without a mechanism, building the mechanism
won't create the desire.

---

## The one-week version

If everything above feels like too much, this is the irreducible core:

1. Pick the niche. *(30 min)*
2. Write 8 artifacts you already know work, with worked examples. *(3 days)*
3. Give 2 away publicly. *(1 hour)*
4. Message 30 real people individually. *(2 days)*
5. Charge $39.

Steps 1 and 4 are where this succeeds or fails. Steps 2, 3 and 5 are the easy part, which is
exactly why the temptation is to spend all the time there.
