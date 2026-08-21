# Production Trace

**Generated:** 2026-08-21T09:56:16+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-F55BA6`
**Session ID:** `SES-20260821-DA157D`
**Started:** 2026-08-21T09:38:23+00:00
**Finished:** 2026-08-21T09:56:16+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6209.9 | 77 | 0 | — |
| document_discovery | completed | 6210.0 | 77 | 0 | — |
| document_download | completed | 323867.9 | 42 | 0 | — |
| extraction | completed | 35.5 | 0 | 5 | — |
| candidate_validation | completed | 16.9 | 0 | 5 | — |
| publish_queue | completed | 16.8 | 0 | 5 | — |
| append_dataset | completed | 23.8 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.6 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
