# Automation — Dataset Factory

Factory packages:

| Package | Role |
|---------|------|
| `collector/` | Source acquisition (→ connectors) |
| `extractor/` | Extraction / normalize |
| `validator/` | Validation / dedupe |
| `publisher/` | Append datasets |
| `quality/` | Metrics |
| `export/` | Training exports |
| `missions/` | Mission definitions |
| `scheduler/` | Prioritization |
| `ci/` | GHA entrypoints |
| `pipeline/` | Stage implementations |
| `connectors/` | Collector implementation |
| `config/` | YAML configuration |

Official pipeline: see root `ARCHITECTURE.md`.
