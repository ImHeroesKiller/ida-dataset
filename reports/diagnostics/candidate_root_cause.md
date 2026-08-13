# Candidate Root Cause

**Generated:** 2026-08-13T00:05:11+00:00
**Session:** `SESSION-20260812-299AA2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000011`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **40**
- Integrity blocked: **40**
- Blocked by primary reason: **40**

## What evidence proves it?

- `session_id=SESSION-20260812-299AA2`
- `dry_run=False`
- `candidates_analyzed=40`
- `integrity_blocked=40`
- `top_family=duplicate_id count=40`
- `family_histogram={'duplicate_id': 40}`
- `reason_histogram={'duplicate_id:IND-000011': 3, 'duplicate_id:IND-000008': 3, 'duplicate_id:IND-000002': 3, 'duplicate_id:IND-000006': 3, 'duplicate_id:IND-000010': 3, 'duplicate_id:IND-000012': 3, 'duplicate_id:IND-000005': 3, 'duplicate_id:IND-000014': 2, 'duplicate_id:IND-000007': 3, 'duplicate_id:IND-000009': 3, 'duplicate_id:IND-000013': 2, 'duplicate_id:IND-000004': 3, 'duplicate_id:IND-000003': 3, 'duplicate_id:IND-000001': 3}`
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
- `candidate CAND-80C2AC135F36 entity_id=IND-000009 reason=duplicate_id:IND-000009 conf=0.836`
- `candidate CAND-DB2E39200CB1 entity_id=IND-000013 reason=duplicate_id:IND-000013 conf=0.8075`
- `candidate CAND-8FB7605FB916 entity_id=IND-000010 reason=duplicate_id:IND-000010 conf=0.836`
- `candidate CAND-7AFBC514D015 entity_id=IND-000011 reason=duplicate_id:IND-000011 conf=0.8075`
- `candidate CAND-4055AA2F2F4E entity_id=IND-000005 reason=duplicate_id:IND-000005 conf=0.836`
- `candidate CAND-5D1B69EBA921 entity_id=IND-000003 reason=duplicate_id:IND-000003 conf=0.836`
- `candidate CAND-02826646AA38 entity_id=IND-000006 reason=duplicate_id:IND-000006 conf=0.92`
- `candidate CAND-6E7840687EAE entity_id=IND-000001 reason=duplicate_id:IND-000001 conf=0.92`
- `candidate CAND-7E3C4B387591 entity_id=IND-000007 reason=duplicate_id:IND-000007 conf=0.836`
- `candidate CAND-91FFA6E6591A entity_id=IND-000014 reason=duplicate_id:IND-000014 conf=0.8075`
- `candidate CAND-DF3529FA1AA8 entity_id=IND-000012 reason=duplicate_id:IND-000012 conf=0.8075`
- `candidate CAND-8270A7788088 entity_id=IND-000002 reason=duplicate_id:IND-000002 conf=0.92`
- `candidate CAND-31BF7E48BB67 entity_id=IND-000004 reason=duplicate_id:IND-000004 conf=0.836`
- `candidate CAND-2D17B6521F4F entity_id=IND-000008 reason=duplicate_id:IND-000008 conf=0.92`

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
| CAND-C0DEF0FB996B | industry_library | 0.855 | False | duplicate_id:IND-000008 | Rejected |
| CAND-6ACEF72974C4 | industry_library | 0.874 | False | duplicate_id:IND-000009 | Rejected |
| CAND-59B49A1A8F1F | industry_library | 0.874 | False | duplicate_id:IND-000007 | Rejected |
| CAND-8B66153B6B79 | industry_library | 0.92 | False | duplicate_id:IND-000013 | Rejected |
| CAND-EFE423B30DA3 | industry_library | 0.855 | False | duplicate_id:IND-000004 | Rejected |
| CAND-A794C3DE0ED1 | industry_library | 0.855 | False | duplicate_id:IND-000002 | Rejected |
| CAND-924C6F41A07B | industry_library | 0.92 | False | duplicate_id:IND-000004 | Rejected |
| CAND-29E5FA722096 | industry_library | 0.855 | False | duplicate_id:IND-000003 | Rejected |
| CAND-4D7BD598AB16 | industry_library | 0.855 | False | duplicate_id:IND-000001 | Rejected |
| CAND-21EFE6035AB9 | industry_library | 0.855 | False | duplicate_id:IND-000003 | Rejected |
| CAND-9DFB1CD280F2 | industry_library | 0.92 | False | duplicate_id:IND-000001 | Rejected |
| CAND-933FD0411EAD | industry_library | 0.855 | False | duplicate_id:IND-000009 | Rejected |
| CAND-6A30FDEFF5EF | industry_library | 0.92 | False | duplicate_id:IND-000012 | Rejected |
| CAND-80C2AC135F36 | industry_library | 0.836 | False | duplicate_id:IND-000009 | Rejected |
| CAND-DB2E39200CB1 | industry_library | 0.8075 | False | duplicate_id:IND-000013 | Rejected |
| CAND-8FB7605FB916 | industry_library | 0.836 | False | duplicate_id:IND-000010 | Rejected |
| CAND-7AFBC514D015 | industry_library | 0.8075 | False | duplicate_id:IND-000011 | Rejected |
| CAND-4055AA2F2F4E | industry_library | 0.836 | False | duplicate_id:IND-000005 | Rejected |
| CAND-5D1B69EBA921 | industry_library | 0.836 | False | duplicate_id:IND-000003 | Rejected |
| CAND-02826646AA38 | industry_library | 0.92 | False | duplicate_id:IND-000006 | Rejected |
| CAND-6E7840687EAE | industry_library | 0.92 | False | duplicate_id:IND-000001 | Rejected |
| CAND-7E3C4B387591 | industry_library | 0.836 | False | duplicate_id:IND-000007 | Rejected |
| CAND-91FFA6E6591A | industry_library | 0.8075 | False | duplicate_id:IND-000014 | Rejected |
| CAND-DF3529FA1AA8 | industry_library | 0.8075 | False | duplicate_id:IND-000012 | Rejected |
| CAND-8270A7788088 | industry_library | 0.92 | False | duplicate_id:IND-000002 | Rejected |
| CAND-31BF7E48BB67 | industry_library | 0.836 | False | duplicate_id:IND-000004 | Rejected |
| CAND-2D17B6521F4F | industry_library | 0.92 | False | duplicate_id:IND-000008 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000011` were satisfied for 40/40 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
