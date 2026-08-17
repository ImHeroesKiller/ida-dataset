# Production Trace

**Generated:** 2026-08-17T20:42:12+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-144B8F`
**Session ID:** `SES-20260817-7A5800`
**Started:** 2026-08-17T20:29:12+00:00
**Finished:** 2026-08-17T20:42:12+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6240.5 | 77 | 0 | — |
| document_discovery | completed | 6240.6 | 77 | 0 | — |
| document_download | completed | 39739.9 | 42 | 0 | — |
| extraction | completed | 157.8 | 0 | 5 | — |
| candidate_validation | completed | 8.1 | 0 | 5 | — |
| publish_queue | completed | 8.1 | 0 | 5 | — |
| append_dataset | completed | 15.5 | 0 | 5 | — |
| export | skipped | 3.9 | 0 | 0 | — |
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
