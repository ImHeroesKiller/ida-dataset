# Queue Efficiency

**Generated:** 2026-08-13T00:03:57+00:00

## Depths

| Queue | Metric | Value |
|-------|--------|------:|
| Document | incoming | 0 |
| Document | processing | 0 |
| Document | processed | 72 |
| Document | depth | 0 |
| Candidate | pending | 0 |
| Candidate | approved | 40 |
| Candidate | rejected | 0 |
| Publish | depth | 33 |

## Starvation / imbalance

- `publish_queue_backlog`

## Rebalance signals

```json
{
  "prefer_process_incoming": false,
  "prefer_drain_publish": true,
  "prefer_review_pending": false,
  "document_weight": 0.0,
  "candidate_weight": 0.0,
  "publish_weight": 0.4520547945205479
}
```
