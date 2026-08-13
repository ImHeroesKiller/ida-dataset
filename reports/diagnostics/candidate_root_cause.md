# Candidate Root Cause

**Generated:** 2026-08-13T00:38:59+00:00
**Session:** `SESSION-20260813-EFF8A4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000011`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **33**
- Integrity blocked: **26**
- Blocked by primary reason: **26**

## What evidence proves it?

- `session_id=SESSION-20260813-EFF8A4`
- `dry_run=False`
- `candidates_analyzed=33`
- `integrity_blocked=26`
- `top_family=duplicate_id count=26`
- `family_histogram={'duplicate_id': 26}`
- `reason_histogram={'duplicate_id:IND-000011': 2, 'duplicate_id:IND-000008': 2, 'duplicate_id:IND-000002': 2, 'duplicate_id:IND-000006': 2, 'duplicate_id:IND-000010': 2, 'duplicate_id:IND-000012': 2, 'duplicate_id:IND-000005': 2, 'duplicate_id:IND-000014': 1, 'duplicate_id:IND-000007': 2, 'duplicate_id:IND-000009': 2, 'duplicate_id:IND-000013': 1, 'duplicate_id:IND-000004': 2, 'duplicate_id:IND-000003': 2, 'duplicate_id:IND-000001': 2}`
- `candidate CAND-FD9FB8F20088 entity_id=IND-000011 reason=duplicate_id:IND-000011 conf=0.92`
- `candidate CAND-4D31A7BF92F6 entity_id=IND-000008 reason=duplicate_id:IND-000008 conf=0.92`
- `candidate CAND-E1882A3C114F entity_id=IND-000002 reason=duplicate_id:IND-000002 conf=0.92`
- `candidate CAND-4AF10225EB6B entity_id=IND-000006 reason=duplicate_id:IND-000006 conf=0.92`
- `candidate CAND-6ADD53D8E489 entity_id=IND-000010 reason=duplicate_id:IND-000010 conf=0.92`
- `candidate CAND-AB49E874BE64 entity_id=IND-000012 reason=duplicate_id:IND-000012 conf=0.92`
- `candidate CAND-BA8A78824279 entity_id=IND-000005 reason=duplicate_id:IND-000005 conf=0.855`
- `candidate CAND-61FC37838342 entity_id=IND-000011 reason=duplicate_id:IND-000011 conf=0.92`
- `candidate CAND-7DDE5E598B3B entity_id=IND-000010 reason=duplicate_id:IND-000010 conf=0.92`
- `candidate CAND-198A3C192524 entity_id=IND-000014 reason=duplicate_id:IND-000014 conf=0.92`
- `candidate CAND-64F739498BDB entity_id=IND-000007 reason=duplicate_id:IND-000007 conf=0.855`
- `candidate CAND-14C0396A9DC4 entity_id=IND-000005 reason=duplicate_id:IND-000005 conf=0.855`
- `candidate CAND-8E0287DD32BE entity_id=IND-000006 reason=duplicate_id:IND-000006 conf=0.874`
- `candidate CAND-C0DEF0FB996B entity_id=IND-000008 reason=duplicate_id:IND-000008 conf=0.855`
- `candidate CAND-6ACEF72974C4 entity_id=IND-000009 reason=duplicate_id:IND-000009 conf=0.874`
- `candidate CAND-59B49A1A8F1F entity_id=IND-000007 reason=duplicate_id:IND-000007 conf=0.874`
- `candidate CAND-8B66153B6B79 entity_id=IND-000013 reason=duplicate_id:IND-000013 conf=0.92`
- `candidate CAND-EFE423B30DA3 entity_id=IND-000004 reason=duplicate_id:IND-000004 conf=0.855`
- `candidate CAND-A794C3DE0ED1 entity_id=IND-000002 reason=duplicate_id:IND-000002 conf=0.855`
- `candidate CAND-924C6F41A07B entity_id=IND-000004 reason=duplicate_id:IND-000004 conf=0.92`
- `candidate CAND-29E5FA722096 entity_id=IND-000003 reason=duplicate_id:IND-000003 conf=0.855`
- `candidate CAND-4D7BD598AB16 entity_id=IND-000001 reason=duplicate_id:IND-000001 conf=0.855`
- `candidate CAND-21EFE6035AB9 entity_id=IND-000003 reason=duplicate_id:IND-000003 conf=0.855`
- `candidate CAND-9DFB1CD280F2 entity_id=IND-000001 reason=duplicate_id:IND-000001 conf=0.92`
- `candidate CAND-933FD0411EAD entity_id=IND-000009 reason=duplicate_id:IND-000009 conf=0.855`
- `candidate CAND-6A30FDEFF5EF entity_id=IND-000012 reason=duplicate_id:IND-000012 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FD9FB8F20088 | industry_library | 0.92 | False | duplicate_id:IND-000011 | Rejected |
| CAND-4D31A7BF92F6 | industry_library | 0.92 | False | duplicate_id:IND-000008 | Rejected |
| CAND-E1882A3C114F | industry_library | 0.92 | False | duplicate_id:IND-000002 | Rejected |
| CAND-4AF10225EB6B | industry_library | 0.92 | False | duplicate_id:IND-000006 | Rejected |
| CAND-6ADD53D8E489 | industry_library | 0.92 | False | duplicate_id:IND-000010 | Rejected |
| CAND-AB49E874BE64 | industry_library | 0.92 | False | duplicate_id:IND-000012 | Rejected |
| CAND-BA8A78824279 | industry_library | 0.855 | False | duplicate_id:IND-000005 | Rejected |
| CAND-61FC37838342 | industry_library | 0.92 | False | duplicate_id:IND-000011 | Rejected |
| CAND-7DDE5E598B3B | industry_library | 0.92 | False | duplicate_id:IND-000010 | Rejected |
| CAND-198A3C192524 | industry_library | 0.92 | False | duplicate_id:IND-000014 | Rejected |
| CAND-64F739498BDB | industry_library | 0.855 | False | duplicate_id:IND-000007 | Rejected |
| CAND-14C0396A9DC4 | industry_library | 0.855 | False | duplicate_id:IND-000005 | Rejected |
| CAND-8E0287DD32BE | industry_library | 0.874 | False | duplicate_id:IND-000006 | Rejected |
| CAND-AB5E38F39855 | business_signal_library | 0.9 | True | ok | Queued |
| CAND-C0DEF0FB996B | industry_library | 0.855 | False | duplicate_id:IND-000008 | Rejected |
| CAND-95C824E2F514 | business_signal_library | 0.92 | True | ok | Queued |
| CAND-7528E4183942 | business_signal_library | 0.92 | True | ok | Queued |
| CAND-E9B6307893CE | industry_library | 0.92 | True | ok | Queued |
| CAND-6ACEF72974C4 | industry_library | 0.874 | False | duplicate_id:IND-000009 | Rejected |
| CAND-59B49A1A8F1F | industry_library | 0.874 | False | duplicate_id:IND-000007 | Rejected |
| CAND-8B66153B6B79 | industry_library | 0.92 | False | duplicate_id:IND-000013 | Rejected |
| CAND-EFE423B30DA3 | industry_library | 0.855 | False | duplicate_id:IND-000004 | Rejected |
| CAND-94B9A207CDEE | business_signal_library | 0.88 | True | ok | Queued |
| CAND-D03DE2F0A439 | business_signal_library | 0.9 | True | ok | Queued |
| CAND-A794C3DE0ED1 | industry_library | 0.855 | False | duplicate_id:IND-000002 | Rejected |
| CAND-924C6F41A07B | industry_library | 0.92 | False | duplicate_id:IND-000004 | Rejected |
| CAND-29E5FA722096 | industry_library | 0.855 | False | duplicate_id:IND-000003 | Rejected |
| CAND-4D7BD598AB16 | industry_library | 0.855 | False | duplicate_id:IND-000001 | Rejected |
| CAND-21EFE6035AB9 | industry_library | 0.855 | False | duplicate_id:IND-000003 | Rejected |
| CAND-9DFB1CD280F2 | industry_library | 0.92 | False | duplicate_id:IND-000001 | Rejected |
| CAND-933FD0411EAD | industry_library | 0.855 | False | duplicate_id:IND-000009 | Rejected |
| CAND-F04B1DEAECD0 | business_signal_library | 0.88 | True | ok | Queued |
| CAND-6A30FDEFF5EF | industry_library | 0.92 | False | duplicate_id:IND-000012 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000011` were satisfied for 26/33 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
