# Production Trace

**Generated:** 2026-08-18T07:52:31+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-053586`
**Session ID:** `SES-20260818-7D69D0`
**Started:** 2026-08-18T07:39:31+00:00
**Finished:** 2026-08-18T07:52:31+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.4 | 0 | 0 | — |
| connector | completed | 6159.9 | 77 | 0 | — |
| document_discovery | completed | 6160.0 | 77 | 0 | — |
| document_download | completed | 37171.5 | 42 | 0 | — |
| extraction | completed | 23.5 | 0 | 5 | — |
| candidate_validation | completed | 9.7 | 0 | 5 | — |
| publish_queue | completed | 9.7 | 0 | 5 | — |
| append_dataset | completed | 16.9 | 0 | 5 | — |
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
