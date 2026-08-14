# Architecture Audit & Consolidation Index

**Primary audit:** [architecture_audit_and_cleanup_plan.md](./architecture_audit_and_cleanup_plan.md)  
**Consolidation report:** [consolidation_report.md](./consolidation_report.md)  
**Route map:** [route_map.md](./route_map.md)  
**Deployment integrity:** [deployment_integrity_report.md](./deployment_integrity_report.md)

## Contents of the primary report

1. Repository Architecture Report  
2. Route Map  
3. API Map  
4. Component Map  
5. Layout & Design System Audit  
6. Import / Hook Audit  
7. Folder Audit  
8. Dashboard / Page Audit  
9. Functional Audit  
10. Dependency Graphs  
11. Technical Debt Report  
12. Cleanup Plan (KEEP / MERGE / RENAME / REMOVE / REFACTOR)  
13. Risk Assessment  
14. Complexity Report  
15. Reference architecture  

## Related existing docs (not replaced)

| Doc | Topic |
|-----|--------|
| [../architecture.md](../architecture.md) | System architecture narrative |
| [../runtime.md](../runtime.md) | GHA session execution model |
| [../github_actions.md](../github_actions.md) | Workflows |
| [../learning_dashboard.md](../learning_dashboard.md) | Dashboard purpose |
| [../vercel.md](../vercel.md) | Deploy constraints |
| [deployment_integrity_report.md](./deployment_integrity_report.md) | Vercel ChunkLoadError / asset audit |

## Next steps (out of scope for this audit)

1. Cleanup sprint: delete proven orphans (`live-dashboard`, `use-live-learning`, unused APIs).  
2. Fix or remove Inspector provider.  
3. Consolidate polling into a Shell-level provider.  
4. Align missions/review styling to design tokens.  

**No automatic file deletions were performed in this audit.**
