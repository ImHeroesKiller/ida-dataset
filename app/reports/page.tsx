import { Shell } from "@/components/layout/shell";
import { ReportsClient } from "@/components/shared/reports-client";
import {
  computeHistory,
  listSessions,
} from "@/lib/sessions";

export const dynamic = "force-dynamic";

export default function ReportsPage() {
  const sessions = listSessions({ limit: 200 });
  const history = computeHistory(sessions);
  return (
    <Shell title="Reports">
      <ReportsClient initialHistory={history} initialSessions={sessions} />
    </Shell>
  );
}
