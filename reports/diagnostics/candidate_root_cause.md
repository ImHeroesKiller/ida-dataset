# Candidate Root Cause

**Generated:** 2026-07-27T08:49:50+00:00
**Session:** `SESSION-20260727-2FE166`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000942`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-2FE166`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000942': 1, 'duplicate_id:SIG-000944': 1, 'duplicate_id:SIG-000941': 1, 'duplicate_id:SIG-000940': 1, 'duplicate_id:SIG-000943': 1}`
- `candidate CAND-34CB8A37543B entity_id=SIG-000942 reason=duplicate_id:SIG-000942 conf=0.88`
- `candidate CAND-6685A6F605EC entity_id=SIG-000944 reason=duplicate_id:SIG-000944 conf=0.92`
- `candidate CAND-C9455B88736E entity_id=SIG-000941 reason=duplicate_id:SIG-000941 conf=0.92`
- `candidate CAND-179F9C19D4BC entity_id=SIG-000940 reason=duplicate_id:SIG-000940 conf=0.9`
- `candidate CAND-4A6472DD0E65 entity_id=SIG-000943 reason=duplicate_id:SIG-000943 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-34CB8A37543B | business_signal_library | 0.88 | False | duplicate_id:SIG-000942 | Rejected |
| CAND-6685A6F605EC | business_signal_library | 0.92 | False | duplicate_id:SIG-000944 | Rejected |
| CAND-C9455B88736E | business_signal_library | 0.92 | False | duplicate_id:SIG-000941 | Rejected |
| CAND-179F9C19D4BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000940 | Rejected |
| CAND-4A6472DD0E65 | business_signal_library | 0.9 | False | duplicate_id:SIG-000943 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000942` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
