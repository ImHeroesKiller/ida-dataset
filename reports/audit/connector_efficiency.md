# Connector Efficiency

**Generated:** 2026-07-11T13:39:39+00:00

| Connector | Docs | Trace found | Trace DL | Trace skip | Cands | Pub est | Cand/doc | Pub/doc | Usable | JSON | HTML shell |
|-----------|-----:|------------:|---------:|-----------:|------:|--------:|---------:|--------:|-------:|-----:|-----------:|
| CONN-CROSSREF-001 | 80 | 0 | 0 | 4 | 76 | 76 | 0.95 | 0.95 | 0 | 80 | 0 |
| CONN-WB-001 | 13 | 0 | 0 | 2 | 12 | 12 | 0.923 | 0.923 | 0 | 0 | 2 |
| CONN-OPENALEX-001 | 4 | 0 | 0 | 25 | 7 | 7 | 1.75 | 1.75 | 0 | 0 | 4 |
| CONN-OECD-001 | 3 | 0 | 0 | 1 | 1 | 1 | 0.333 | 0.333 | 0 | 0 | 0 |
| CONN-BPS-001 | 3 | 0 | 0 | 0 | 1 | 1 | 0.333 | 0.333 | 0 | 0 | 0 |
| CONN-INT-001 | 2 | 0 | 0 | 0 | 1 | 1 | 0.5 | 0.5 | 0 | 0 | 0 |
| unknown | 0 | 0 | 0 | 0 | 8 | 2 | 0 | 0 | 0 | 0 | 0 |
| CONN-ADB-001 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CONN-KEMENPERIN-001 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Named checklist

| Name | In corpus |
|------|-----------|
| World Bank | True |
| Crossref | True |
| OpenAlex | True |
| OECD | True |
| ADB | True |
| BPS | True |
| DISC-LAYER | False |

## Finding

Connectors differ, but globally yield is capped by **metadata-sized payloads** and **~1 candidate/document**.
