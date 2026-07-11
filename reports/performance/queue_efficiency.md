# Queue Efficiency

**Generated:** 2026-07-11T14:47:54+00:00

## Depths

| Queue | Metric | Value |
|-------|--------|------:|
| Document | incoming | 0 |
| Document | processing | 0 |
| Document | processed | 92 |
| Document | depth | 0 |
| Candidate | pending | 6 |
| Candidate | approved | 0 |
| Candidate | rejected | 0 |
| Publish | depth | 6 |

## Starvation / imbalance

- None detected

## Rebalance signals

```json
{
  "prefer_process_incoming": false,
  "prefer_drain_publish": true,
  "prefer_review_pending": true,
  "document_weight": 0.0,
  "candidate_weight": 0.5,
  "publish_weight": 0.5
}
```
