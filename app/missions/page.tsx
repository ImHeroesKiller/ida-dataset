import { Shell } from "@/components/layout/shell";
import { MissionsClient } from "@/features/missions/missions-client";
import {
  listContracts,
  listMissions,
  listLearningReports,
  enrichLearningReports,
} from "@/lib/learning";

export const dynamic = "force-dynamic";

export default function MissionsPage() {
  const missions = listMissions();
  const contracts = listContracts();
  const reports = enrichLearningReports(listLearningReports());

  return (
    <Shell title="Missions">
      <div className="mx-auto max-w-6xl space-y-6">
        <header>
          <h1 className="text-3xl font-semibold tracking-tight text-[var(--text)]">
            Missions
          </h1>
          <p className="mt-2 text-base text-[var(--text-muted)]">
            Direct autonomous production — queue the next dataset the factory should grow.
          </p>
        </header>
        <MissionsClient
          missions={missions}
          contracts={contracts}
          reports={reports}
        />
      </div>
    </Shell>
  );
}
