# Learning Dashboard (ECC)

## Purpose

Visualize how IDA is learning — a **realtime monitor of GitHub Actions learning sessions**, not a host for the learning runtime.

## Status: Active

## Execution model

```text
GitHub Actions → Learning Session → Repo update → Dashboard refresh
```

- No long-lived Python process on the dashboard host  
- No server-side SSE runtime tailer  
- Safe on Vercel  

## Routes

| Route | Content |
| --- | --- |
| `/` | Learning Sessions dashboard |
| `/learning` | Full Learning Brain cockpit |
| `/missions` | Mission + contract management |

## Sections

| Section | Content |
| --- | --- |
| Current status | Idle · Running · Completed · Failed |
| Next scheduled run | Hourly / daily cron |
| Last successful run | From session files |
| Current mission | Instruction / mission text |
| Knowledge counters | Added · Updated · Rejected |
| Session duration | From session record |
| Learning history | Today · Week · Month · Total · success rate · growth · avg duration |
| Session journal | Real logs (console) |
| Replay | Ordered events with timestamps |

## Manual learning

**Start Learning** → `POST /api/live/start` → GitHub `workflow_dispatch` on `learning.yml`.

No local Python execution.

## Console

**Learning Session Journal** — current/previous session logs, knowledge events, mission events. Replay loads stored session files. No fake streaming.

## APIs

| API | Role |
| --- | --- |
| `GET /api/sessions` | Dashboard aggregate + GHA status |
| `GET /api/sessions?session_id=` | Full session + events |
| `POST /api/live/start` | Dispatch learning.yml |
| `GET /api/live/replay` | Session list / events |
| `GET /api/learning` | Scheduler brain dashboard (file fallback on Vercel) |

## Config for dispatch (Vercel)

```text
IDA_GITHUB_TOKEN
GITHUB_REPOSITORY   # or VERCEL_GIT_REPO_OWNER + VERCEL_GIT_REPO_SLUG
```
