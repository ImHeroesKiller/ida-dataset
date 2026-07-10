# Autonomous Production Checklist

**Generated:** 2026-07-10T15:51:42.662478+00:00  

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Continue missions automatically | PARTIAL | Hourly learn continues; mission text is industry-default |
| Resume after workflow completion | YES | Next cron starts new session |
| Update KPIs | YES | daily_*.json + journal when sessions write state |
| Update dashboard metrics | YES | Dashboard reads live state/KPIs on request |
| Generate reports | YES | reports/learning session files |
| Append datasets | PARTIAL | When live_runtime publish path succeeds and not dry-run |
| Generate exports | NO/WEAK | export.yml not scheduled |
| Respect DPS | YES | Confidence/source/dupe gates in policies + runtime |
| Respect append-only | YES | Publisher append_only |
| Respect trusted sources | YES | require_trusted_source |
| Reject invalid rows | YES | validator rejects |
| Maintain provenance | YES | Notes/Data Sources conventions + provenance fields policy |
| Maintain confidence | YES | threshold 0.80 |
| Maintain freshness | PARTIAL | Last Updated set on new rows; no forced recrawl of all rows overnight |
| No manual intervention required | NO | Push conflicts, publish blocked, permission issues need humans |

---

## Overnight go / no-go

| Mode | Go? | Why |
|------|-----|-----|
| Continuous Industry learning (default GHA) | **CONDITIONAL GO** | Works historically; accept push-conflict residual risk |
| Full multi-batch autonomous factory (002–015) | **NO-GO** | Default mission, export gap, policy gates, integrity debt |
| Batch-009 persona overnight without dispatch | **NO-GO** | Mission not configured for personas |

---

## Human actions before true unattended multi-batch (optional, not done in this audit)

1. Ensure Actions can push to main (permissions).  
2. Prefer no human pushes during overnight window.  
3. Optionally dispatch learn with explicit Batch-009 mission.  
4. Monitor first 2 hourly runs after leaving.

This audit does **not** change workflows.
