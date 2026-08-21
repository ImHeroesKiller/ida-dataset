# Production Trace

**Generated:** 2026-08-21T20:45:38+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-CB4F24`
**Session ID:** `SES-20260821-460CC8`
**Started:** 2026-08-21T20:27:50+00:00
**Finished:** 2026-08-21T20:45:38+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6196.1 | 74 | 0 | — |
| document_discovery | completed | 6196.2 | 74 | 0 | — |
| document_download | completed | 317470.1 | 42 | 0 | — |
| extraction | completed | 41.5 | 0 | 5 | — |
| candidate_validation | completed | 17.5 | 0 | 5 | — |
| publish_queue | completed | 17.6 | 0 | 5 | — |
| append_dataset | completed | 22.0 | 0 | 5 | — |
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
