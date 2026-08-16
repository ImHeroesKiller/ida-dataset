# Production Trace

**Generated:** 2026-08-16T04:51:27+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-73A87B`
**Session ID:** `SES-20260816-DABAF6`
**Started:** 2026-08-16T04:37:22+00:00
**Finished:** 2026-08-16T04:51:27+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6247.7 | 27 | 0 | — |
| document_discovery | completed | 6247.8 | 27 | 0 | — |
| document_download | completed | 97417.2 | 11 | 0 | — |
| extraction | completed | 30.1 | 0 | 5 | — |
| candidate_validation | completed | 49.6 | 0 | 5 | — |
| publish_queue | completed | 49.8 | 0 | 5 | — |
| append_dataset | completed | 5.8 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
