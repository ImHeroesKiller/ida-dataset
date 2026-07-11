# Pipeline Loss Analysis

**Generated:** 2026-07-11T13:39:39+00:00

## Ranked stage losses (traces)

| Rank | Transition | From | To | Lost | Loss % |
|-----:|------------|-----:|---:|-----:|-------:|
| 1 | Discovery → Publish (E2E) | 346 | 110 | 236 | 68.21% |
| 2 | Discovery → Download | 346 | 206 | 140 | 40.46% |
| 3 | Download → Extraction (candidates) | 206 | 130 | 76 | 36.89% |
| 4 | Extraction → Validation | 130 | 116 | 14 | 10.77% |
| 5 | Validation → Publish | 116 | 110 | 6 | 5.17% |
| 6 | Download → Parsed (proxy=downloaded) | 206 | 206 | 0 | 0.0% |

## Corpus losses

| Loss | N | % docs |
|------|--:|-------:|
| No candidates | 57 | 54.29% |
| Single-dataset only | 45 | 42.86% |
| Thin text chars&lt;500 | 105 | 100.0% |
| JSON API body | 80 | 76.19% |
| HTML shell | 6 | 5.71% |

## Impact ranking

| Rank | Bottleneck | Score | Evidence |
|-----:|------------|------:|----------|
| 1 | Pre-download duplicate document skips | 156 | 156 |
| 2 | Discovery→Download drop (trace aggregate) | 140 | 346→206 |
| 3 | Single-dataset mapping (missed multi-library rows) | 135 | 45 single-ds docs ×3 |
| 4 | Thin content (chars<500) | 105 | 105/105 |
| 5 | Documents with zero candidates extracted | 57 | 57/105 |

## Largest stage loss

**Discovery → Publish (E2E)** — **68.21%** (346 → 110)
