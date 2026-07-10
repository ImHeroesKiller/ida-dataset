# Publish Flow Call Graph

**Generated for:** Git Reliability & Atomic Production sprint  
**Rule:** Exactly **one** publish execution path per learning session.

## Call graph (learning session)

```text
GitHub Actions learn.yml
  └─ python automation/ci/learning_session.py
        ├─ ContinuousLearningScheduler.tick (dry, no publish)
        ├─ run_live_session (automation/learning/live_runtime.py)
        │     └─ run_acquisition (automation/acquisition/pipeline.py)
        │           ├─ filter_append_rows (integrity_guard)  [validate]
        │           └─ append_csv_rows                      [PUBLISH #1 — sole path]
        ├─ progressive_publish.py
        │     └─ ONLY if publish queue non-empty AND knowledge_added == 0
        │           └─ append_csv_rows                      [PUBLISH #2 — gated, rare]
        └─ growth.snapshot_today / session finalize (no dataset publish)
```

## Double-publish elimination

| Path | When | Status |
|------|------|--------|
| Acquisition `append_csv_rows` | Normal production session | **Primary** |
| `progressive_publish.py` | Residual queue after review-only sessions | **Gated** |
| GHA publish.yml | Separate scheduled job | Independent concurrency group |

### Gate (learning_session.py)

```text
if queue has *.json AND not already_published_in_session:
    run progressive_publish
else:
    skip (telemetry publish_once.progressive_publish_skipped=true)
```

This removes the noisy `published=0 empty queue` second invocation after a successful acquisition publish.

## Empty queue message

`progressive_publish.py` prints `{"published":0,"message":"empty queue"}` when the queue is empty.
After the gate, that path is **not** entered when acquisition already published.

## Certification

- [x] Single primary publish path in acquisition
- [x] Progressive publish cannot re-run after in-session publish
- [x] No force-push in publish path
