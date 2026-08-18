# Production Trace

**Generated:** 2026-08-18T09:02:59+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-103A1B`
**Session ID:** `SES-20260818-62D6B2`
**Started:** 2026-08-18T08:39:14+00:00
**Finished:** 2026-08-18T09:02:59+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6187.4 | 77 | 0 | — |
| document_discovery | completed | 6187.5 | 77 | 0 | — |
| document_download | completed | 690718.5 | 54 | 0 | — |
| extraction | completed | 31.3 | 0 | 5 | — |
| candidate_validation | completed | 12.7 | 0 | 5 | — |
| publish_queue | completed | 12.7 | 0 | 5 | — |
| append_dataset | completed | 26.8 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **54**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
