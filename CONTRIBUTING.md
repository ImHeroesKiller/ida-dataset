# Contributing — IDA Dataset Factory

## Production freeze (v2.0)

Core architecture is **frozen**. See [PRODUCTION_FREEZE.md](./PRODUCTION_FREEZE.md).

**Allowed:** new connectors, dataset expansion, source registry config, production bug fixes, documentation.  
**Forbidden:** architecture/schema/queue redesign, RAG, agents, decision/reasoning engines.

## Rule

Every change must answer **yes**:

> Does this help generate better datasets?

If no, it does not belong here.

## Local

```bash
npm install
npm run dev
npm run health
```

## Datasets

- Append-only  
- Preserve schema headers  
- Include provenance  

## PRs

- Prefer small, factory-aligned PRs  
- Do not reintroduce ECC / brain / ontology / network UI  
- Keep the 8 factory routes only  
