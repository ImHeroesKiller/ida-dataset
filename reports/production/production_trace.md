# Production Trace

**Generated:** 2026-08-24T01:40:59+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-5CC7B2`
**Session ID:** `SES-20260824-2C17DC`
**Started:** 2026-08-24T01:23:15+00:00
**Finished:** 2026-08-24T01:40:59+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6222.7 | 77 | 0 | — |
| document_discovery | completed | 6222.8 | 77 | 0 | — |
| document_download | completed | 323121.9 | 42 | 0 | — |
| extraction | completed | 38.6 | 0 | 5 | — |
| candidate_validation | completed | 20.0 | 0 | 5 | — |
| publish_queue | completed | 20.1 | 0 | 5 | — |
| append_dataset | completed | 23.6 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
