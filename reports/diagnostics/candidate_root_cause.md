# Candidate Root Cause

**Generated:** 2026-08-23T21:41:25+00:00
**Session:** `SESSION-20260823-D26FCB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001168`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-D26FCB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001168': 1, 'duplicate_id:SIG-001170': 1, 'duplicate_id:SIG-001169': 1, 'duplicate_id:SIG-001166': 1, 'duplicate_id:SIG-001167': 1}`
- `candidate CAND-DA8F83E03EB2 entity_id=SIG-001168 reason=duplicate_id:SIG-001168 conf=0.9`
- `candidate CAND-2944EBEE9B20 entity_id=SIG-001170 reason=duplicate_id:SIG-001170 conf=0.9`
- `candidate CAND-2013254CFDD0 entity_id=SIG-001169 reason=duplicate_id:SIG-001169 conf=0.9`
- `candidate CAND-95ACF31C51EE entity_id=SIG-001166 reason=duplicate_id:SIG-001166 conf=0.92`
- `candidate CAND-969EF978A202 entity_id=SIG-001167 reason=duplicate_id:SIG-001167 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DA8F83E03EB2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001168 | Rejected |
| CAND-2944EBEE9B20 | business_signal_library | 0.9 | False | duplicate_id:SIG-001170 | Rejected |
| CAND-2013254CFDD0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001169 | Rejected |
| CAND-95ACF31C51EE | business_signal_library | 0.92 | False | duplicate_id:SIG-001166 | Rejected |
| CAND-969EF978A202 | business_signal_library | 0.9 | False | duplicate_id:SIG-001167 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001168` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
