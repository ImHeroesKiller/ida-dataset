# Production Trace

**Generated:** 2026-08-14T02:18:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-AF2100`
**Session ID:** `SES-20260814-ECD042`
**Started:** 2026-08-14T02:04:16+00:00
**Finished:** 2026-08-14T02:18:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6229.2 | 77 | 0 | — |
| document_discovery | completed | 6229.4 | 77 | 0 | — |
| document_download | completed | 81816.7 | 42 | 0 | — |
| extraction | completed | 18.3 | 0 | 5 | — |
| candidate_validation | completed | 4.3 | 0 | 5 | — |
| publish_queue | completed | 4.3 | 0 | 5 | — |
| append_dataset | completed | 12.5 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
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
