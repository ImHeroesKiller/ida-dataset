# IDA Knowledge Network (IKN)

## Purpose

Controlled knowledge acquisition network. Internet is only one source class.

## Status: Active (Sprint 5)

## Flow

```text
Scheduler → Planner → Policy → Connector Manager → Connectors
→ Document Queue → Pipeline → Review → Publisher → Telemetry
```

- Planner decides  
- Policy validates  
- Connector Manager executes  
- Connectors **never** write datasets  
- Connectors **never** extract knowledge  

## CLI

```bash
python -m automation.connectors list
python -m automation.connectors health
python -m automation.connectors search "query" --acquire
python -m automation.search "Indonesian manufacturing" --limit 5
```

## Config

`automation/config/connectors.yaml`
