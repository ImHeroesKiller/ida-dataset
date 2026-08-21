# Production Trace

**Generated:** 2026-08-21T08:01:37+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-07860A`
**Session ID:** `SES-20260821-C043E3`
**Started:** 2026-08-21T07:44:11+00:00
**Finished:** 2026-08-21T08:01:37+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6212.7 | 23 | 0 | — |
| document_discovery | completed | 6212.8 | 23 | 0 | — |
| document_download | completed | 309863.5 | 11 | 0 | — |
| extraction | completed | 32.5 | 0 | 5 | — |
| candidate_validation | completed | 16.4 | 0 | 5 | — |
| publish_queue | completed | 16.4 | 0 | 5 | — |
| append_dataset | completed | 10.3 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
