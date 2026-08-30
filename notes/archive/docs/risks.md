# Risks

Ordered by expected damage. Each has an early-warning signal, because a risk you can't detect
in time is just a surprise.

---

## R1 — Free is the competitor *(near-certain, high damage)*

Everything we sell exists free somewhere. We aren't selling content; we're selling curation,
verification and maintenance.

- **Early warning:** buyers say "I found this on GitHub." Copy is describing artifacts instead
  of outcomes.
- **Mitigation:** lead with the measured outcome and the maintenance promise. Never list contents
  as the primary sales argument.
- **Kill signal:** we cannot articulate what a buyer gets that a free repo doesn't. If that
  happens, the product is genuinely undifferentiated and we should stop, not push harder.

## R2 — Distribution, not building, is the hard part *(near-certain, high damage)*

Building is ~10% of this business. The instinct is to spend 90% of the time there because
building is pleasant and outreach is not.

- **Early warning:** more time in the repo than talking to humans. Phase 1 running past 10 days.
- **Mitigation:** ADR-005 (no product before revenue) and the hard step count in Phase 2.6.
- **Note:** this is the most likely cause of failure. It is also the least likely to feel like failure.

## R3 — Model churn rots the inventory *(certain, medium damage)*

Every model release can invalidate part of the catalogue. This is a treadmill, not passive income.

- **Early warning:** Gate C pass finds >30% stale in a month.
- **Mitigation:** the ~40-artifact cap; `expires` on every record; evals written at authoring time.
- **Reframe:** this is also the moat. Competitors won't run the treadmill. If churn ever stops,
  our differentiation goes with it.

## R4 — Vendors ship first-party registries *(plausible, structural)*

Anthropic/OpenAI shipping good maintained skill libraries would eat the middle of the market.

- **Early warning:** official registries appear covering our niche.
- **Mitigation:** stay in the role-specific, opinionated layer they will never staff. A vendor
  will never publish "how solo recruiters should run intake."
- **Kill signal:** first-party coverage of our exact niche at our quality. Then move niche.

## R5 — Maintenance promise becomes a lie *(the one that ends us)*

We promise maintenance, get busy, stop. Six months later we're selling a stale PDF.

- **Early warning:** a Gate C pass slips by more than two weeks.
- **Mitigation:** calendar the monthly pass; publish breakages publicly; cap the catalogue.
- **Honest option:** if we can't maintain it, say so publicly and switch to one-time sales with
  no promise. A smaller honest business beats a fraudulent one.

## R6 — Building for hobbyists *(likely, slow damage)*

The loudest audience — hobbyists and dev teams — engages enthusiastically and pays nothing.

- **Early warning:** engagement metrics green, revenue flat. Audience skewing hobbyist.
- **Mitigation:** metrics separate reach from revenue and are never averaged.

## R7 — Cold-starting the platform too early *(avoidable, fatal if hit)*

Building the community platform before there's demand is a year-consuming way to fail.

- **Early warning:** any platform work before Rung 3.
- **Mitigation:** ADR-007's four unlock conditions.

## R8 — Niche chosen for comfort rather than pain *(likely, medium)*

Picking the segment we like over the one that hurts most.

- **Early warning:** we can't state the recurring >$49/month task in one concrete sentence.
- **Mitigation:** Phase 1.2 forces the sentence before any writing starts.

## R9 — Trust and accuracy in regulated niches *(conditional)*

Only if a legal/medical/financial niche is chosen. AI output in those fields carries real
liability, and "verified" starts to mean something legally.

- **Mitigation:** either avoid these niches, or ship explicit disclaimers and never claim
  professional-grade correctness.

## R11 — The catalogue has one load-bearing artifact *(certain, medium damage)*

Seven of the Phase 1 twelve depend on `wf-0001` (codebase orientation) upstream, and two of the
four decisions are directly model-dependent. When the orientation pass breaks against a new
model, most of the catalogue goes stale in the same week — not gradually, all at once.

- **Early warning:** a single Gate C run flipping >3 artifacts to `stale` at the same time.
- **Mitigation:** `dec-0002` and `dec-0003` are re-run against **every new frontier model on
  release**, ahead of the monthly cycle. They are the leading indicators for the rest.
- **Reframe:** a correlated failure is also a correlated fix, and publishing "six artifacts went
  stale on model X's release day, here is the updated pass" is the most convincing changelog
  email we will ever send. See [validation.md](validation.md) Gate C.
- **Accepted deliberately.** A wedge product is supposed to be concentrated; diversifying the
  dependency graph would mean diluting the wedge, which is a worse trade.

## R10 — Solo-operator bus factor *(structural, accepted)*

One part-time person is the entire company: author, maintainer, marketer, support.

- **Mitigation:** the catalogue cap, and the ADR-007 platform path — which is, ultimately, the
  plan for making maintenance survive one person's attention.
