# Production Trace

**Generated:** 2026-08-23T19:41:21+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-50AB29`
**Session ID:** `SES-20260823-DE1108`
**Started:** 2026-08-23T19:23:39+00:00
**Finished:** 2026-08-23T19:41:21+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6193.9 | 27 | 0 | — |
| document_discovery | completed | 6194.0 | 27 | 0 | — |
| document_download | completed | 307463.5 | 11 | 0 | — |
| extraction | completed | 36.6 | 0 | 5 | — |
| candidate_validation | completed | 20.1 | 0 | 5 | — |
| publish_queue | completed | 20.1 | 0 | 5 | — |
| append_dataset | completed | 10.5 | 0 | 5 | — |
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
