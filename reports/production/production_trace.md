# Production Trace

**Generated:** 2026-08-16T13:47:01+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-ABADD8`
**Session ID:** `SES-20260816-BA694E`
**Started:** 2026-08-16T13:33:16+00:00
**Finished:** 2026-08-16T13:47:01+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 15524.8 | 77 | 0 | — |
| document_discovery | completed | 15524.9 | 77 | 0 | — |
| document_download | completed | 190225.2 | 42 | 0 | — |
| extraction | completed | 27.8 | 0 | 5 | — |
| candidate_validation | completed | 10.3 | 0 | 5 | — |
| publish_queue | completed | 10.3 | 0 | 5 | — |
| append_dataset | completed | 23.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
