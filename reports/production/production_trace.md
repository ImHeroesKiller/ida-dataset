# Production Trace

**Generated:** 2026-08-18T10:44:22+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-95FAA1`
**Session ID:** `SES-20260818-256193`
**Started:** 2026-08-18T10:31:20+00:00
**Finished:** 2026-08-18T10:44:22+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6224.2 | 77 | 0 | — |
| document_discovery | completed | 6224.4 | 77 | 0 | — |
| document_download | completed | 37429.0 | 42 | 0 | — |
| extraction | completed | 27.0 | 0 | 5 | — |
| candidate_validation | completed | 9.9 | 0 | 5 | — |
| publish_queue | completed | 9.9 | 0 | 5 | — |
| append_dataset | completed | 16.5 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
