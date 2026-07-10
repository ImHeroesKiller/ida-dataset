# Learning Dashboard (ECC)

## Purpose

Visualize how IDA is learning — not an administration panel.

## Status: Active (Sprint 4)

## Routes

| Route | Content |
| --- | --- |
| `/` | Learning-first home dashboard |
| `/learning` | Full Learning Brain cockpit |
| `/missions` | Mission + contract management |

## Sections

Brain Health · Knowledge Growth · Learning Allocation · Current Mission · Mission Queue · Continuous Learning Queue · Learning Timeline · Knowledge Feed · Brain Activity · Learning History · Knowledge / Domain Coverage · Confidence · Reasoning/Decision placeholders

## Live console

Bottom ECC console streams scheduler events when ticks/missions run (Planner selected, mission dispatched, continuous resumed, etc.).

## APIs

- `GET/POST /api/learning` — dashboard, tick, mission create  
- `GET /api/missions` — missions, contracts, learning reports  

## Runtime note

On Vercel, Python scheduler CLI may be unavailable; dashboard falls back to state files. Full orchestration runs locally or via CI.
