# Production Trace

**Generated:** 2026-08-15T23:34:59+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-872FA0`
**Session ID:** `SES-20260815-2D9E15`
**Started:** 2026-08-15T23:22:01+00:00
**Finished:** 2026-08-15T23:34:59+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6193.1 | 77 | 0 | — |
| document_discovery | completed | 6193.3 | 77 | 0 | — |
| document_download | completed | 38541.7 | 42 | 0 | — |
| extraction | completed | 26.7 | 0 | 5 | — |
| candidate_validation | completed | 9.3 | 0 | 5 | — |
| publish_queue | completed | 9.3 | 0 | 5 | — |
| append_dataset | completed | 22.9 | 0 | 5 | — |
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
