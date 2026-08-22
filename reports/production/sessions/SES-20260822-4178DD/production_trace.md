# Production Trace

**Generated:** 2026-08-22T20:42:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-19955E`
**Session ID:** `SES-20260822-4178DD`
**Started:** 2026-08-22T20:25:03+00:00
**Finished:** 2026-08-22T20:42:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6210.0 | 77 | 0 | — |
| document_discovery | completed | 6210.1 | 77 | 0 | — |
| document_download | completed | 311114.1 | 42 | 0 | — |
| extraction | completed | 39.2 | 0 | 5 | — |
| candidate_validation | completed | 18.8 | 0 | 5 | — |
| publish_queue | completed | 18.9 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.6 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
