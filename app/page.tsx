import { Shell } from "@/components/layout/shell";
import { FactoryDashboard } from "@/features/dashboard/factory-dashboard";
import { getFactoryKpis } from "@/lib/factory-kpis";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const kpis = getFactoryKpis();
  return (
    <Shell title="Dashboard">
      <FactoryDashboard kpis={kpis} />
    </Shell>
  );
}
