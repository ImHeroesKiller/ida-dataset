# Production Trace

**Generated:** 2026-08-21T03:22:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-98FE30`
**Session ID:** `SES-20260821-C88EA1`
**Started:** 2026-08-21T03:04:44+00:00
**Finished:** 2026-08-21T03:22:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.6 | 77 | 0 | — |
| document_discovery | completed | 6199.7 | 77 | 0 | — |
| document_download | completed | 337035.9 | 42 | 0 | — |
| extraction | completed | 34.3 | 0 | 5 | — |
| candidate_validation | completed | 16.6 | 0 | 5 | — |
| publish_queue | completed | 16.6 | 0 | 5 | — |
| append_dataset | completed | 21.8 | 0 | 5 | — |
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
