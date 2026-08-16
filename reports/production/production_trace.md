# Production Trace

**Generated:** 2026-08-16T05:44:18+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-A6C01C`
**Session ID:** `SES-20260816-E55B12`
**Started:** 2026-08-16T05:30:06+00:00
**Finished:** 2026-08-16T05:44:18+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6191.4 | 27 | 0 | — |
| document_discovery | completed | 6191.6 | 27 | 0 | — |
| document_download | completed | 109143.8 | 11 | 0 | — |
| extraction | completed | 25.0 | 0 | 5 | — |
| candidate_validation | completed | 10.3 | 0 | 5 | — |
| publish_queue | completed | 10.3 | 0 | 5 | — |
| append_dataset | completed | 10.4 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
