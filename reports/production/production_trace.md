# Production Trace

**Generated:** 2026-08-23T20:42:54+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-48C8F8`
**Session ID:** `SES-20260823-5585E4`
**Started:** 2026-08-23T20:25:19+00:00
**Finished:** 2026-08-23T20:42:54+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6193.9 | 77 | 0 | — |
| document_discovery | completed | 6194.1 | 77 | 0 | — |
| document_download | completed | 307341.3 | 42 | 0 | — |
| extraction | completed | 38.9 | 0 | 5 | — |
| candidate_validation | completed | 20.0 | 0 | 5 | — |
| publish_queue | completed | 20.1 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
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
