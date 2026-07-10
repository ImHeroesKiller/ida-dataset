import { Shell } from "@/components/layout/shell";
import { MissionsClient } from "@/components/shared/missions-client";
import { listContracts, listMissions, listLearningReports } from "@/lib/learning";

export const dynamic = "force-dynamic";

export default function MissionsPage() {
  return (
    <Shell title="Missions">
      <MissionsClient
        missions={listMissions()}
        contracts={listContracts()}
        reports={listLearningReports()}
      />
    </Shell>
  );
}
