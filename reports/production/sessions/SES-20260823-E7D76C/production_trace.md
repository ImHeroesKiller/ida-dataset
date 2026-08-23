# Production Trace

**Generated:** 2026-08-23T15:42:51+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-8DF91D`
**Session ID:** `SES-20260823-E7D76C`
**Started:** 2026-08-23T15:24:51+00:00
**Finished:** 2026-08-23T15:42:51+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6208.9 | 77 | 0 | — |
| document_discovery | completed | 6209.0 | 77 | 0 | — |
| document_download | completed | 333604.7 | 42 | 0 | — |
| extraction | completed | 39.1 | 0 | 5 | — |
| candidate_validation | completed | 20.3 | 0 | 5 | — |
| publish_queue | completed | 20.4 | 0 | 5 | — |
| append_dataset | completed | 22.3 | 0 | 5 | — |
| export | skipped | 0.7 | 0 | 0 | — |
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
