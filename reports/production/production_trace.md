# Production Trace

**Generated:** 2026-07-20T07:06:02+00:00
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Mission ID:** `MIS-20260720-920528`
**Session ID:** `SES-20260720-BDDABA`
**Started:** 2026-07-20T06:49:05+00:00
**Finished:** 2026-07-20T07:06:02+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 93785.0 | 97 | 0 | — |
| document_discovery | completed | 93785.2 | 97 | 0 | — |
| document_download | completed | 186753.3 | 74 | 0 | — |
| extraction | completed | 97.4 | 0 | 5 | — |
| candidate_validation | completed | 11.8 | 0 | 5 | — |
| publish_queue | completed | 11.8 | 0 | 5 | — |
| append_dataset | completed | 45.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **31**
- Documents downloaded: **74**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
