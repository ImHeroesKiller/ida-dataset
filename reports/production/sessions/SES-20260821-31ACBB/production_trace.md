# Production Trace

**Generated:** 2026-08-21T10:50:26+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-3B0E20`
**Session ID:** `SES-20260821-31ACBB`
**Started:** 2026-08-21T10:32:40+00:00
**Finished:** 2026-08-21T10:50:26+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.3 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6173.3 | 73 | 0 | — |
| document_discovery | completed | 6173.3 | 73 | 0 | — |
| document_download | completed | 314172.1 | 42 | 0 | — |
| extraction | completed | 35.4 | 0 | 5 | — |
| candidate_validation | completed | 16.8 | 0 | 5 | — |
| publish_queue | completed | 16.8 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
