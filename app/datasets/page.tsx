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
      <div className="mx-auto max-w-7xl space-y-6">
        <header>
          <h1 className="text-page-title">Dataset catalog</h1>
          <p className="mt-2 max-w-2xl text-body text-[var(--text-secondary)]">
            Product knowledge libraries for LLM fine-tuning. Coverage is current
            rows versus product target; readiness is a 0–100 quality score.
            Observe only — no in-UI editing.
          </p>
        </header>
        <DatasetsClient datasets={enriched} />
      </div>
    </Shell>
  );
}
