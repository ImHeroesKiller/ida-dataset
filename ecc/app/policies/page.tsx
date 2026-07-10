import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getPolicies, getSources, getOntologyBundle } from "@/lib/repo-data";
import { PolicyClient } from "@/components/shared/policy-client";

export const dynamic = "force-dynamic";

export default function PoliciesPage() {
  const policies = getPolicies();
  const sources = getSources();
  const ontology = getOntologyBundle();
  const entities = ontology.tables["entities.csv"]?.rows ?? [];
  const data = (policies.data ?? {}) as Record<string, unknown>;
  const features = (data.features ?? {}) as Record<string, boolean>;
  const confidence = Number(data.confidence_threshold ?? 0.8);
  const approvalMode = String(data.approval_mode ?? "manual");
  const reviewRequired = Boolean(data.review_required ?? true);

  const sourceList = Array.isArray(
    (sources.data as { sources?: unknown[] } | null)?.sources
  )
    ? ((sources.data as { sources: Record<string, unknown>[] }).sources ?? [])
    : [];

  const allowed = sourceList
    .filter((s) => s.allowed === true || s.allowed === "true")
    .map((s) => String(s.name ?? s.source_id ?? "source"));
  const forbidden = sourceList
    .filter((s) => s.allowed === false || s.allowed === "false")
    .map((s) => String(s.name ?? s.source_id ?? "source"));

  const entityPolicies = entities.map((e) => ({
    entityId: e["Entity ID"] ?? "",
    entityName: e["Entity Name"] ?? "",
    entityType: e["Entity Type"] ?? "",
    category: e["Category"] ?? "",
    confidence,
    approvalMode,
    reviewRequired,
    crawlingEnabled: Boolean(features.crawling_enabled),
    extractionEnabled: Boolean(features.extraction_enabled),
    publishingEnabled: Boolean(features.publishing_enabled),
    allowedSources: allowed,
    forbiddenSources: forbidden,
  }));

  return (
    <Shell title="Knowledge Policies">
      <div className="mb-4 space-y-2">
        <p className="text-sm text-zinc-300">
          Policy Engine governs every plan before pipeline execution.
        </p>
        <div className="flex flex-wrap gap-1.5">
          <Badge>approval={approvalMode}</Badge>
          <Badge>review_required={String(reviewRequired)}</Badge>
          <Badge>confidence≥{confidence}</Badge>
          <Badge>
            crawl={String(Boolean(features.crawling_enabled))} extract=
            {String(Boolean(features.extraction_enabled))} publish=
            {String(Boolean(features.publishing_enabled))}
          </Badge>
        </div>
        {!policies.exists ? (
          <p className="text-xs text-amber-300">
            Waiting for first execution — policies file missing
          </p>
        ) : null}
      </div>

      <Card>
        <CardHeader
          title="Entity Policy Matrix"
          description="Read from automation/config/policies.yaml + ontology entities. Edit is local draft only until saved via config workflow."
        />
        <CardBody className="p-0">
          <PolicyClient
            rows={entityPolicies}
            rawPolicies={data}
            sourcesSummary={{ allowed, forbidden }}
          />
        </CardBody>
      </Card>
    </Shell>
  );
}
