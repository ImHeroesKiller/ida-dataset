# Queue Efficiency

**Generated:** 2026-07-17T21:15:37+00:00

## Depths

| Queue | Metric | Value |
|-------|--------|------:|
| Document | incoming | 0 |
| Document | processing | 0 |
| Document | processed | 72 |
| Document | depth | 0 |
| Candidate | pending | 0 |
| Candidate | approved | 5 |
| Candidate | rejected | 0 |
| Publish | depth | 7 |

## Starvation / imbalance

- None detected

## Rebalance signals

```json
{
  "prefer_process_incoming": false,
  "prefer_drain_publish": true,
  "prefer_review_pending": false,
  "document_weight": 0.0,
  "candidate_weight": 0.0,
  "publish_weight": 0.5833333333333334
}
```
