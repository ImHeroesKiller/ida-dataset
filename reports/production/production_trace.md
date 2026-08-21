# Production Trace

**Generated:** 2026-08-21T04:57:51+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-A83EED`
**Session ID:** `SES-20260821-268A8B`
**Started:** 2026-08-21T04:40:00+00:00
**Finished:** 2026-08-21T04:57:51+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6207.3 | 77 | 0 | — |
| document_discovery | completed | 6207.4 | 77 | 0 | — |
| document_download | completed | 321678.5 | 42 | 0 | — |
| extraction | completed | 36.3 | 0 | 5 | — |
| candidate_validation | completed | 17.6 | 0 | 5 | — |
| publish_queue | completed | 17.6 | 0 | 5 | — |
| append_dataset | completed | 24.5 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
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
