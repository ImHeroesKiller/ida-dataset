# Knowledge Atom Design

**Milestone:** 2 — Knowledge Graph Manufacturing Engine  
**Date:** 2026-07-12  
**Status:** Implemented (atomize + persistent store)  
**Constraint:** Additive only — no dataset row generation

## Pipeline shift

```text
Before:  Document → Extraction → Dataset row
Now:     Document → Knowledge Atoms  (this commit)
Later:   Atoms → Entities → Graph → Multi-dataset manufacturing
```

## Atom types

| Type | Detection |
|------|-----------|
| heading | Markdown `#`, numbered sections, ALL-CAPS titles |
| paragraph | Prose blocks between blanks |
| section | Longer paragraph groups under a heading |
| table | `|...|` or multi-tab rows |
| bullet | `-`, `*`, `•`, numbered lists |
| faq | `Q:` / `A:` pairs |
| caption | Figure/Table/Chart captions |
| metadata | title, abstract, snippet from document record |

## Atom schema

| Field | Description |
|-------|-------------|
| atom_id | `ATOM-{sha1-12}` stable per doc+order+type+text |
| document_id | Source document |
| atom_type | One of the types above |
| text | Atom body |
| source | source_id / connector |
| source_url | Original URL |
| section | Current heading context |
| heading_path | Trail of headings |
| order | Sequence in document |
| timestamp | Atomization time |
| confidence | From trust_score / base |
| provenance | source_id, url, mission, version |
| metadata | Type-specific extras |

## Persistence

```text
automation/knowledge/store/atoms/{document_id}.json
automation/knowledge/store/atoms/_index.json
```

Runtime artifacts (gitignored except structure). No external DB.

## API

```python
from automation.knowledge.atoms import atomize_document
from automation.knowledge.atom_store import atomize_and_persist_document, load_atoms_for_document

atoms = atomize_document(doc_dict)
summary = atomize_and_persist_document(doc_dict)
loaded = load_atoms_for_document("DOC-…")
```

## Non-goals (this commit)

- Entity extraction  
- Relationships  
- Dataset row writes  
- Pipeline stage rewrites  

## Compatibility

Scheduler, GHA, dashboard, queues, missions, CSV schemas, export, HF — **unchanged**.
