import { Shell } from "@/components/layout/shell";
import { MissionsClient } from "@/features/missions/missions-client";
import { listContracts, listMissions, listLearningReports } from "@/lib/learning";

export const dynamic = "force-dynamic";

export default function MissionsPage() {
  return (
    <Shell title="Missions">
      <div className="mx-auto max-w-6xl space-y-6">
        <header>
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-50">
            Missions
          </h1>
          <p className="mt-2 text-base text-zinc-400">
            Direct what IDA should learn next.
          </p>
        </header>
        <MissionsClient
          missions={listMissions()}
          contracts={listContracts()}
          reports={listLearningReports()}
        />
      </div>
    </Shell>
  );
}
