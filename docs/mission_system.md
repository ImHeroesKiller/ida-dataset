# Mission System

## Purpose

Directed Learning missions assigned by humans.

## Status: Active (Sprint 4)

## Storage

```text
automation/missions/
  missions/       # active
  templates/
  history/
  attachments/
  contracts/      # learning contracts
```

## Schema fields

Mission ID, Title, Description, Priority, Requester, Created At, Due Date, Status, Knowledge Targets, Allowed Sources, Policies, Estimated Effort, Resource Allocation, Progress, Confidence, Result, Executive Summary, Related Datasets.

## Statuses

Draft · Queued · Running · Waiting Review · Completed · Paused · Cancelled · Archived

## Priorities

| Code | Label |
| --- | --- |
| P0 | Critical |
| P1 | High |
| P2 | Medium |
| P3 | Low |
| P4 | Background |

## Natural language intake

Examples mapped without LLM heuristics:

- “Learn everything about SAP ERP.”  
- “Prepare for tomorrow's meeting with Telkom.”  
- “Study all Indonesian mining companies.”  
- “Focus on cyber security regulations.”  

Free text still becomes a structured mission with a Learning Contract.
