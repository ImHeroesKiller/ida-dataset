import { Shell } from "@/components/layout/shell";
import { MissionsClient } from "@/features/missions/missions-client";
import { listMissions } from "@/lib/learning";

export const dynamic = "force-dynamic";

export default function MissionsPage() {
  const missions = listMissions();

  return (
    <Shell title="Mission">
      <MissionsClient missions={missions} />
    </Shell>
  );
}
