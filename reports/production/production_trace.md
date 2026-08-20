# Production Trace

**Generated:** 2026-08-20T11:46:34+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-879948`
**Session ID:** `SES-20260820-C5DDF7`
**Started:** 2026-08-20T11:28:52+00:00
**Finished:** 2026-08-20T11:46:34+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6184.3 | 77 | 0 | — |
| document_discovery | completed | 6184.4 | 77 | 0 | — |
| document_download | completed | 311565.6 | 42 | 0 | — |
| extraction | completed | 33.4 | 0 | 5 | — |
| candidate_validation | completed | 15.6 | 0 | 5 | — |
| publish_queue | completed | 15.6 | 0 | 5 | — |
| append_dataset | completed | 22.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
