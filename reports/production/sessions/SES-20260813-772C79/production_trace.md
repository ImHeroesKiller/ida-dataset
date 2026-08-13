# Production Trace

**Generated:** 2026-08-13T20:57:51+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-5DCFE0`
**Session ID:** `SES-20260813-772C79`
**Started:** 2026-08-13T20:44:46+00:00
**Finished:** 2026-08-13T20:57:51+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6226.3 | 77 | 0 | — |
| document_discovery | completed | 6226.4 | 77 | 0 | — |
| document_download | completed | 37770.8 | 42 | 0 | — |
| extraction | completed | 24.9 | 0 | 5 | — |
| candidate_validation | completed | 7.7 | 0 | 5 | — |
| publish_queue | completed | 7.8 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
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
