# Production Trace

**Generated:** 2026-08-18T13:54:55+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-6B7A5A`
**Session ID:** `SES-20260818-499BC4`
**Started:** 2026-08-18T13:44:21+00:00
**Finished:** 2026-08-18T13:54:55+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6179.9 | 23 | 0 | — |
| document_discovery | completed | 6180.1 | 23 | 0 | — |
| document_download | completed | 61948.8 | 11 | 0 | — |
| extraction | completed | 27.9 | 0 | 5 | — |
| candidate_validation | completed | 12.8 | 0 | 5 | — |
| publish_queue | completed | 12.8 | 0 | 5 | — |
| append_dataset | completed | 10.3 | 0 | 5 | — |
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
