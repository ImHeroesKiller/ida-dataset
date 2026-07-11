# Queue Efficiency

**Generated:** 2026-07-11T05:52:55+00:00

## Depths

| Queue | Metric | Value |
|-------|--------|------:|
| Document | incoming | 13 |
| Document | processing | 0 |
| Document | processed | 20 |
| Document | depth | 13 |
| Candidate | pending | 0 |
| Candidate | approved | 18 |
| Candidate | rejected | 0 |
| Publish | depth | 0 |

## Starvation / imbalance

- `document_queue_idle_workers`
- `publish_queue_starved_of_approved`

## Rebalance signals

```json
{
  "prefer_process_incoming": true,
  "prefer_drain_publish": false,
  "prefer_review_pending": false,
  "document_weight": 0.3939393939393939,
  "candidate_weight": 0.0,
  "publish_weight": 0.0
}
```
