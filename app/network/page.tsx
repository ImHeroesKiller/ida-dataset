import { Shell } from "@/components/layout/shell";
import { NetworkClient } from "@/components/shared/network-client";
import { getNetworkDashboard } from "@/lib/network";

export const dynamic = "force-dynamic";

export default function NetworkPage() {
  const dash = getNetworkDashboard();
  return (
    <Shell title="Knowledge Network">
      <NetworkClient initial={dash as Record<string, unknown>} />
    </Shell>
  );
}
