# Release Report — Batch-002 Service Dataset

**Mission:** MIS-PRODUCE-SERVICE-DATASET — Produce Service Dataset  
**Standard:** DPS v1.0  
**Version:** knowledge-v2.0-batch-002-service  
**Timestamp:** 2026-07-10T15:28:18.304363+00:00

## Summary

| Metric | Value |
|--------|------:|
| Rows Before (catalog) | 20 |
| Rows Added | 46 |
| Rows Rejected | 0 |
| Rows After (catalog) | 66 |
| Service rows before | 19 |
| Service rows after | 65 |
| Coverage Before | 19 / 2000 (0.9%) |
| Coverage After | 65 / 2000 (3.2%) |
| Average Confidence | 0.89 |
| Freshness | 2026-07-10 (100% of new rows) |
| Duplicates Removed | 0 |
| Duplicate Rate (batch) | 0% |
| Schema Completeness (batch) | 88.9% |
| Quality Score | 91.7 |
| Readiness Score (service lens) | 70.8 |
| Mission Duration | 0s |
| Export Status | ok |
| Build Status | pass |

## Sources Used

- SRC-000001
- SRC-000004
- SRC-000005
- SRC-000006
- SRC-000007
- SRC-000008
- SRC-000009
- SRC-000010
- SRC-000011
- SRC-000012
- SRC-000013
- SRC-000014
- SRC-000015

## Rules Compliance

- Append-only: yes
- Schema unchanged: yes
- Architecture unchanged: yes
- Trusted sources only: yes (registry IDs)
- Confidence threshold ≥ 0.80: yes
- Pain/Solution IDs left empty until those libraries exist (no phantom links)

## Export Artifacts

- `exports/jsonl/product_catalog_20260710T152818Z.jsonl`
- `exports/openai/product_catalog_ft_20260710T152818Z.jsonl`
- `exports/huggingface/product_catalog_20260710T152818Z.json`

## Services Added

- PROD-021: Managed Network Operations Center (NOC) Service
- PROD-022: Application Managed Services (AMS)
- PROD-023: Cloud Migration & Landing Zone Service
- PROD-024: Colocation & Remote Hands Data Center Service
- PROD-025: Managed Endpoint & Device Lifecycle Service
- PROD-026: Identity Governance Administration Service
- PROD-027: Vulnerability Assessment as a Service
- PROD-028: Business Continuity & Disaster Recovery Drill Service
- PROD-029: Third-Party Logistics (3PL) Contract Logistics Service
- PROD-030: Cold Chain Logistics Service
- PROD-031: Customs Clearance & Trade Compliance Service
- PROD-032: Last-Mile Delivery Orchestration Service
- PROD-033: Contact Center Quality Assurance Service
- PROD-034: Content Moderation Operations Service
- PROD-035: Finance & Accounting Outsourcing Service
- PROD-036: Payroll Tax Compliance Support Service
- PROD-037: Recruitment Process Outsourcing (RPO) Service
- PROD-038: Corporate Learning Delivery Service
- PROD-039: ESG Reporting & Sustainability Disclosure Support Service
- PROD-040: Industrial Energy Audit Service
- PROD-041: Occupational Health & Safety (OHS) Managed Service
- PROD-042: Equipment Calibration & Metrology Coordination Service
- PROD-043: Warehouse Operations Outsourcing Service
- PROD-044: Port Agency Support Service
- PROD-045: Agricultural Extension & Agronomy Advisory Service
- PROD-046: Plantation Sustainability Assurance Support Service
- PROD-047: Hospitality Revenue Management Support Service
- PROD-048: Retail Merchandising Execution Service
- PROD-049: Mystery Shopping & Service Audit Service
- PROD-050: Healthcare Revenue Cycle Support Service
- PROD-051: Insurance Policy Administration Support Service
- PROD-052: Claims Processing Support Service
- PROD-053: Digital KYC Operations Support Service
- PROD-054: Payment Operations Support Service
- PROD-055: Public Procurement Bid Support Service
- PROD-056: Business Licensing Process Facilitation Service
- PROD-057: Managed Security Awareness Training Service
- PROD-058: Data Protection Impact Assessment Support Service
- PROD-059: Industrial Maintenance Contract Service
- PROD-060: Software Quality Assurance Testing Service
- PROD-061: IT Service Desk Managed Service
- PROD-062: Managed Print & Document Operations Service
- PROD-063: Environmental Monitoring & Sampling Coordination Service
- PROD-064: Contact Center Overflow / Surge Capacity Service
- PROD-065: Records Digitization & Archival Operations Service
- PROD-066: Vendor Management Office (VMO) Support Service

## Notes

Service Dataset is stored in `product_catalog.csv` with `Product Type = Service` until a dedicated `service_library` schema is version-approved. Coverage uses product target **service_library = 2000** from `automation/config/product_targets.yaml`.
