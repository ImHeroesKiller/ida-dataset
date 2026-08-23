# Production Trace

**Generated:** 2026-08-23T10:43:30+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-F59748`
**Session ID:** `SES-20260823-63A60F`
**Started:** 2026-08-23T10:25:54+00:00
**Finished:** 2026-08-23T10:43:30+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 1.9 | 0 | 0 | — |
| connector | completed | 6151.3 | 77 | 0 | — |
| document_discovery | completed | 6151.4 | 77 | 0 | — |
| document_download | completed | 310554.6 | 42 | 0 | — |
| extraction | completed | 22.8 | 0 | 5 | — |
| candidate_validation | completed | 9.9 | 0 | 5 | — |
| publish_queue | completed | 10.0 | 0 | 5 | — |
| append_dataset | completed | 10.6 | 0 | 5 | — |
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
