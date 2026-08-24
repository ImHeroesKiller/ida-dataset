# Production Trace

**Generated:** 2026-08-24T13:11:34+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-3150E5`
**Session ID:** `SES-20260824-F3840C`
**Started:** 2026-08-24T12:53:41+00:00
**Finished:** 2026-08-24T13:11:34+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6221.2 | 46 | 0 | — |
| document_discovery | completed | 6221.4 | 46 | 0 | — |
| document_download | completed | 328229.3 | 31 | 0 | — |
| extraction | completed | 38.7 | 0 | 5 | — |
| candidate_validation | completed | 25.6 | 0 | 5 | — |
| publish_queue | completed | 25.6 | 0 | 5 | — |
| append_dataset | completed | 18.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
