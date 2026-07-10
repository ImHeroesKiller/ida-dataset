import { Shell } from "@/components/layout/shell";
import { listDatasets } from "@/lib/repo-data";
import { getFactoryKpis } from "@/lib/factory-kpis";
import { DatasetsClient } from "@/components/shared/datasets-client";

export const dynamic = "force-dynamic";

export default function DatasetsPage() {
  const datasets = listDatasets();
  const kpis = getFactoryKpis();
  const readinessByPath = new Map(
    (kpis.datasets || []).map((d) => [d.relativePath, d])
  );
  const enriched = datasets.map((d) => {
    const r = readinessByPath.get(d.relativePath);
    return {
      ...d,
      readiness: r?.readiness,
      product_target: r?.product_target,
      coverage_pct: r?.coverage_pct,
      coverage_label: r?.coverage_label,
    };
  });
  return (
    <Shell title="Datasets">
      <div className="mb-3">
        <p className="text-sm text-zinc-300">
          Read-only CSV browser for domain knowledge assets.
        </p>
        <p className="text-xs text-zinc-500">
          Coverage = current rows / product target · readiness 0–100 beside each
          dataset. No editing from UI — observe only.
        </p>
      </div>
      <DatasetsClient datasets={enriched} />
    </Shell>
  );
}
