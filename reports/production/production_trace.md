# Production Trace

**Generated:** 2026-08-13T18:11:17+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-255C5C`
**Session ID:** `SES-20260813-081BCE`
**Started:** 2026-08-13T17:58:17+00:00
**Finished:** 2026-08-13T18:11:17+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6152.3 | 77 | 0 | — |
| document_discovery | completed | 6152.5 | 77 | 0 | — |
| document_download | completed | 41044.3 | 42 | 0 | — |
| extraction | completed | 23.9 | 0 | 5 | — |
| candidate_validation | completed | 6.7 | 0 | 5 | — |
| publish_queue | completed | 6.7 | 0 | 5 | — |
| append_dataset | completed | 22.1 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
