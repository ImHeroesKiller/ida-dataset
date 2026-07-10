# Resource Allocation

## Purpose

Describe how the scheduler shares capacity between Continuous and Directed learning.

## Status: Active (Sprint 4)

## Config location

`automation/config/learning.yaml` → `allocation`

## Default profiles

| Profile | Continuous | Directed | When |
| --- | ---: | ---: | --- |
| `default` | 70% | 30% | Normal directed load |
| `critical_mission` | 20% | 80% | Any P0 active |
| `high_mission` | 40% | 55% | P1 active, no P0 |
| `idle` | 85% | 0% | No directed missions |

Maintenance / ontology / policy slices are configurable in the same profiles.

## Rules

1. Continuous Learning never drops to zero while enabled (`never_stop`)  
2. Ratios are normalized to 100%  
3. No hardcoded percentages in Python — only config defaults as fallback  
4. Directed Learning cannot bypass Policy or Review regardless of allocation  
