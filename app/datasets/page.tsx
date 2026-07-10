import { Shell } from "@/components/layout/shell";
import { listDatasets } from "@/lib/repo-data";
import { DatasetsClient } from "@/components/shared/datasets-client";

export const dynamic = "force-dynamic";

export default function DatasetsPage() {
  const datasets = listDatasets();
  return (
    <Shell title="Datasets">
      <div className="mb-3">
        <p className="text-sm text-zinc-300">
          Read-only CSV browser for domain knowledge assets.
        </p>
        <p className="text-xs text-zinc-500">
          No editing from ECC. Mutations only via Review → Publisher path.
        </p>
      </div>
      <DatasetsClient datasets={datasets} />
    </Shell>
  );
}
