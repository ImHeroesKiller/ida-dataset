# Production Trace

**Generated:** 2026-08-21T05:52:12+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-9EAEF0`
**Session ID:** `SES-20260821-D64798`
**Started:** 2026-08-21T05:34:29+00:00
**Finished:** 2026-08-21T05:52:12+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6146.3 | 47 | 0 | — |
| document_discovery | completed | 6146.4 | 47 | 0 | — |
| document_download | completed | 317336.4 | 31 | 0 | — |
| extraction | completed | 34.3 | 0 | 5 | — |
| candidate_validation | completed | 16.5 | 0 | 5 | — |
| publish_queue | completed | 16.6 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
