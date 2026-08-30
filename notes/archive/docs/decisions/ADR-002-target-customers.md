# ADR-002 — Four segments, worked in strict sequence

**Status:** Accepted
**Date:** 2026-08-30

## Context

Four segments were chosen as targets: solo consultants, small agencies, SMB marketing managers,
and small dev teams. All four are plausible. The risk is not choosing badly — it is trying to
serve all four at once with one operator.

## Decision

All four segments are in scope. **They are worked in strict sequence, not in parallel:**

1. Solo consultants
2. Small agencies (2–15)
3. SMB marketing managers
4. Small dev teams — **as a distribution channel, not a revenue line**

A segment opens only when the previous one has produced paying strangers.

## Reasoning

- Each segment needs different vocabulary, different packaging and different channels.
  Writing four sets of messaging in parallel means writing four bad ones.
- Solo consultants come first because they have the shortest distance between pain and payment:
  high hourly rate, no approval chain, own the budget, expense it without thinking.
- Agencies are second because they are the same economics multiplied by headcount, and they
  are the first segment where per-seat recurring revenue is honest.
- Marketing managers are third because serving them properly requires a **non-technical
  product surface** — effectively a second front-end. That's an investment the first two
  segments should fund.
- Dev teams are last for revenue despite being easiest to reach: they can build it themselves,
  expect open source, and argue about price publicly. Their value is amplification.

## Alternatives rejected

| Option | Why not |
|---|---|
| Pick one segment only, drop the rest | Throws away real optionality; dev teams are too useful as a channel. |
| All four in parallel | Guarantees four mediocre positionings. One operator can't do it. |
| Start with dev teams (easiest to reach) | Cheapest audience, lowest revenue. Would show engagement and no money — the classic trap. |

## Consequences

- Segments 2–4 are **explicitly parked**. Ideas for them get written down, not acted on.
- Marketing effort aimed at dev teams is measured as **reach**, never as conversion. Engagement
  from this segment must not be read as traction.
- We accept that the fastest-growing audience may be the one that pays least. That is by design.

## What would reverse this

- Inbound demand arrives unprompted and concentrated from a segment other than #1. Follow the
  money — reorder and write a new ADR.
- Segment 1 fails to produce a paying stranger after a full, honest outreach cycle. That is a
  signal about the segment or the offer, and both need re-examining before continuing down the list.
