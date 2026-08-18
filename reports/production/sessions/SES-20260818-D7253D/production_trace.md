# Production Trace

**Generated:** 2026-08-18T11:38:42+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-AE4E6B`
**Session ID:** `SES-20260818-D7253D`
**Started:** 2026-08-18T11:27:34+00:00
**Finished:** 2026-08-18T11:38:42+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6150.6 | 79 | 0 | — |
| document_discovery | completed | 6150.7 | 79 | 0 | — |
| document_download | completed | 39808.8 | 42 | 0 | — |
| extraction | completed | 51.7 | 0 | 5 | — |
| candidate_validation | completed | 9.9 | 0 | 5 | — |
| publish_queue | completed | 9.9 | 0 | 5 | — |
| append_dataset | completed | 12.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
