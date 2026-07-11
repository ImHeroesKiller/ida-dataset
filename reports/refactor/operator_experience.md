# Operator Experience

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Goals

- Fewer screens to operate production  
- Clear source tiers (Preferred / Trusted / Random)  
- Export monitor includes GitHub + Hugging Face  
- Console mirrors acquisition · GHA · HF · export  
- Cadence and discovery policy visible in Settings  

## Operator path

1. **Dashboard** — status, KPIs, live console  
2. **Mission** — start / pause / resume / stop / retry  
3. **Sources** — preferred + trusted health  
4. **Export** — packaging + HF status  
5. **Settings** — cadence + discovery policy visibility  

## Training impact

| Before | After |
|--------|------:|
| 8 nav items | **5** nav items |
| Datasets / Quality / Logs as top-level | Merged / redirected |
| Multi-provider discovery opacity | Tavily-first + max 10 explicit in Settings |

Reduced cognitive load. Redirects preserve old bookmarks.

## Success signals for operators

- Hourly GHA learn runs complete without concurrent writers  
- Tavily searches ≤ 10 per session in discovery analytics  
- Dashboard console shows GitHub / HF / export filters  
- Source tiers populate from health metrics without extra pages  
