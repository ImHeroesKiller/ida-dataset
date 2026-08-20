# Production Trace

**Generated:** 2026-08-20T04:11:04+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-EA8F6A`
**Session ID:** `SES-20260820-A34333`
**Started:** 2026-08-20T03:53:01+00:00
**Finished:** 2026-08-20T04:11:04+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6238.5 | 77 | 0 | — |
| document_discovery | completed | 6238.6 | 77 | 0 | — |
| document_download | completed | 315614.0 | 42 | 0 | — |
| extraction | completed | 33.3 | 0 | 5 | — |
| candidate_validation | completed | 15.0 | 0 | 5 | — |
| publish_queue | completed | 15.1 | 0 | 5 | — |
| append_dataset | completed | 22.2 | 0 | 5 | — |
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
