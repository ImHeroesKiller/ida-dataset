# Production Trace

**Generated:** 2026-08-21T15:53:27+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-63522E`
**Session ID:** `SES-20260821-513F5C`
**Started:** 2026-08-21T15:35:28+00:00
**Finished:** 2026-08-21T15:53:27+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6209.5 | 74 | 0 | — |
| document_discovery | completed | 6209.6 | 74 | 0 | — |
| document_download | completed | 315014.2 | 42 | 0 | — |
| extraction | completed | 35.9 | 0 | 5 | — |
| candidate_validation | completed | 17.0 | 0 | 5 | — |
| publish_queue | completed | 17.0 | 0 | 5 | — |
| append_dataset | completed | 23.5 | 0 | 5 | — |
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
