# Production Trace

**Generated:** 2026-09-13T23:16:14+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260913-0A047F`
**Session ID:** `SES-20260913-E30D17`
**Started:** 2026-09-13T22:58:16+00:00
**Finished:** 2026-09-13T23:16:14+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6193.6 | 19 | 0 | — |
| document_discovery | completed | 6195.1 | 19 | 0 | — |
| document_download | completed | 333331.1 | 11 | 0 | — |
| extraction | completed | 38.0 | 0 | 5 | — |
| candidate_validation | completed | 21.0 | 0 | 5 | — |
| publish_queue | completed | 21.0 | 0 | 5 | — |
| append_dataset | completed | 10.9 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
