import { Shell } from "@/components/layout/shell";
import { getOntologyBundle } from "@/lib/repo-data";
import { OntologyClient } from "@/components/shared/ontology-client";

export const dynamic = "force-dynamic";

export default function OntologyPage() {
  const bundle = getOntologyBundle();
  const entities = bundle.tables["entities.csv"]?.rows ?? [];
  const relationships = bundle.tables["relationships.csv"]?.rows ?? [];
  const types = bundle.tables["entity_types.csv"]?.rows ?? [];
  const version = bundle.version as { version?: string } | null;

  return (
    <Shell title="Ontology">
      <div className="mb-3 space-y-1">
        <p className="text-sm text-zinc-300">
          Interactive browser over KOE CSV ontology — no Neo4j required.
        </p>
        <p className="text-xs text-zinc-500">
          Version {version?.version ?? "—"} · {entities.length} entities ·{" "}
          {relationships.length} relationships
        </p>
      </div>
      <OntologyClient
        entities={entities}
        relationships={relationships}
        entityTypes={types}
      />
    </Shell>
  );
}
