# Production Trace

**Generated:** 2026-08-15T20:36:46+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-E3E012`
**Session ID:** `SES-20260815-D103E4`
**Started:** 2026-08-15T20:23:42+00:00
**Finished:** 2026-08-15T20:36:46+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6226.7 | 47 | 0 | — |
| document_discovery | completed | 6226.8 | 47 | 0 | — |
| document_download | completed | 35489.6 | 31 | 0 | — |
| extraction | completed | 25.4 | 0 | 5 | — |
| candidate_validation | completed | 9.1 | 0 | 5 | — |
| publish_queue | completed | 9.1 | 0 | 5 | — |
| append_dataset | completed | 17.6 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
