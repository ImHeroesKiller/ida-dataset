# Timezone Standardization

**Generated:** 2026-07-10T16:19:42.965420+00:00

## Policy

| Layer | Zone |
|-------|------|
| Storage / GHA / internal | UTC ISO |
| **User-visible UI** | **Asia/Jakarta (WIB, UTC+7)** |

## Format

```
11 Jul 2026 08:15:32 WIB
```

Helper: `lib/time-wib.ts` → `formatWib`, `formatWibTime`, `formatWibDate`

## Applied surfaces

- Dashboard (next run, knowledge feed, heartbeat, replay)
- Journal (collapsed + expanded)
- Logs page
- Sources page timestamps

## Not converted (internal only)

- JSON reports, session files, daily_*.json keys (UTC dates for filesystems)
- GitHub Actions cron (UTC by platform)

## Rule

Never display bare UTC `Z` timestamps to end users.
