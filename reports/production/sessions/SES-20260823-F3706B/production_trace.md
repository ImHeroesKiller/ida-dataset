# Production Trace

**Generated:** 2026-08-23T13:00:01+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-443CEE`
**Session ID:** `SES-20260823-F3706B`
**Started:** 2026-08-23T12:42:32+00:00
**Finished:** 2026-08-23T13:00:01+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6213.4 | 77 | 0 | — |
| document_discovery | completed | 6213.5 | 77 | 0 | — |
| document_download | completed | 308191.0 | 42 | 0 | — |
| extraction | completed | 29.7 | 0 | 5 | — |
| candidate_validation | completed | 14.3 | 0 | 5 | — |
| publish_queue | completed | 14.5 | 0 | 5 | — |
| append_dataset | completed | 12.6 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
