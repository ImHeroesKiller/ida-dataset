# Production Trace

**Generated:** 2026-08-14T10:18:04+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-804E39`
**Session ID:** `SES-20260814-3D16CB`
**Started:** 2026-08-14T10:04:30+00:00
**Finished:** 2026-08-14T10:18:04+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6179.3 | 47 | 0 | — |
| document_discovery | completed | 6179.4 | 47 | 0 | — |
| document_download | completed | 67984.4 | 31 | 0 | — |
| extraction | completed | 22.0 | 0 | 5 | — |
| candidate_validation | completed | 6.1 | 0 | 5 | — |
| publish_queue | completed | 6.2 | 0 | 5 | — |
| append_dataset | completed | 13.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
