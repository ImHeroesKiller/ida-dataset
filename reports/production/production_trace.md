# Production Trace

**Generated:** 2026-08-17T23:37:49+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-15FC24`
**Session ID:** `SES-20260817-F52D30`
**Started:** 2026-08-17T23:24:53+00:00
**Finished:** 2026-08-17T23:37:49+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6193.8 | 77 | 0 | — |
| document_discovery | completed | 6193.8 | 77 | 0 | — |
| document_download | completed | 35506.4 | 42 | 0 | — |
| extraction | completed | 30.3 | 0 | 5 | — |
| candidate_validation | completed | 12.3 | 0 | 5 | — |
| publish_queue | completed | 12.2 | 0 | 5 | — |
| append_dataset | completed | 22.3 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
