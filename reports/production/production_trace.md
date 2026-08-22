# Production Trace

**Generated:** 2026-08-22T13:51:14+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-E3D065`
**Session ID:** `SES-20260822-0DA431`
**Started:** 2026-08-22T13:33:47+00:00
**Finished:** 2026-08-22T13:51:14+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6192.2 | 77 | 0 | — |
| document_discovery | completed | 6192.3 | 77 | 0 | — |
| document_download | completed | 308694.9 | 42 | 0 | — |
| extraction | completed | 37.0 | 0 | 5 | — |
| candidate_validation | completed | 17.6 | 0 | 5 | — |
| publish_queue | completed | 17.7 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
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
