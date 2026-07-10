"use client";

import { StatusBadge } from "@/components/ui/badge";
import { Card, CardBody } from "@/components/ui/card";
import type { ModuleStatus } from "@/lib/status";
import { useInspector } from "@/components/layout/inspector-context";

export function StatusCard({
  label,
  status,
  detail,
}: {
  label: string;
  status: ModuleStatus;
  detail: string;
}) {
  const { inspect } = useInspector();
  return (
    <button
      className="w-full text-left"
      onClick={() =>
        inspect({
          kind: "status",
          title: label,
          subtitle: status,
          meta: { Status: status, Detail: detail },
          body: detail,
        })
      }
    >
      <Card className="h-full transition-colors hover:border-zinc-700">
        <CardBody className="space-y-2">
          <div className="flex items-start justify-between gap-2">
            <div className="text-xs font-medium text-zinc-200">{label}</div>
            <StatusBadge status={status} />
          </div>
          <p className="text-[11px] leading-relaxed text-zinc-500">{detail}</p>
        </CardBody>
      </Card>
    </button>
  );
}
