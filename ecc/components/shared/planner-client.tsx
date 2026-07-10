"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useInspector } from "@/components/layout/inspector-context";
import { cn } from "@/lib/utils";

type Plan = {
  dataset: string;
  domain: string;
  path: string;
  rows: number;
  targetRows: number;
  coverage: number;
  gap: number;
  priority: number;
  isPlaceholder: boolean;
  suggestedAction: string;
};

type Decision = "approved" | "rejected" | "pending";

export function PlannerClient({ plans }: { plans: Plan[] }) {
  const { inspect } = useInspector();
  const [decisions, setDecisions] = useState<Record<string, Decision>>({});

  function setDecision(path: string, d: Decision) {
    setDecisions((prev) => ({ ...prev, [path]: d }));
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[880px] text-left text-xs">
        <thead className="border-b border-zinc-800 bg-zinc-950/80 text-[10px] uppercase tracking-wide text-zinc-500">
          <tr>
            <th className="px-3 py-2 font-medium">Dataset</th>
            <th className="px-3 py-2 font-medium">Domain</th>
            <th className="px-3 py-2 font-medium">Rows</th>
            <th className="px-3 py-2 font-medium">Target</th>
            <th className="px-3 py-2 font-medium">Coverage</th>
            <th className="px-3 py-2 font-medium">Gap</th>
            <th className="px-3 py-2 font-medium">Priority</th>
            <th className="px-3 py-2 font-medium">Plan</th>
            <th className="px-3 py-2 font-medium">Decision</th>
          </tr>
        </thead>
        <tbody>
          {plans.map((p) => {
            const decision = decisions[p.path] ?? "pending";
            return (
              <tr
                key={p.path}
                className="border-b border-zinc-900/80 hover:bg-zinc-900/40"
              >
                <td className="px-3 py-2">
                  <button
                    className="text-left font-medium text-zinc-100 hover:underline"
                    onClick={() =>
                      inspect({
                        kind: "plan",
                        title: p.dataset,
                        subtitle: p.path,
                        meta: {
                          Domain: p.domain,
                          Rows: String(p.rows),
                          Target: String(p.targetRows),
                          Coverage: `${p.coverage}%`,
                          Gap: String(p.gap),
                          Priority: String(p.priority),
                          Decision: decision,
                        },
                        body: p.suggestedAction,
                      })
                    }
                  >
                    {p.dataset}
                  </button>
                </td>
                <td className="px-3 py-2 text-zinc-400">{p.domain}</td>
                <td className="px-3 py-2 text-zinc-300">{p.rows}</td>
                <td className="px-3 py-2 text-zinc-300">{p.targetRows}</td>
                <td className="px-3 py-2">
                  <div className="flex items-center gap-2">
                    <div className="h-1 w-16 overflow-hidden rounded bg-zinc-900">
                      <div
                        className="h-full bg-zinc-400"
                        style={{ width: `${Math.min(100, p.coverage)}%` }}
                      />
                    </div>
                    <span className="text-zinc-400">{p.coverage}%</span>
                  </div>
                </td>
                <td className="px-3 py-2 text-zinc-300">{p.gap}</td>
                <td className="px-3 py-2 text-zinc-300">{p.priority}</td>
                <td className="max-w-[220px] truncate px-3 py-2 text-zinc-500">
                  {p.suggestedAction}
                </td>
                <td className="px-3 py-2">
                  <div className="flex flex-wrap gap-1">
                    <Button
                      size="sm"
                      variant={decision === "approved" ? "default" : "outline"}
                      onClick={() => setDecision(p.path, "approved")}
                    >
                      Approve
                    </Button>
                    <Button
                      size="sm"
                      variant={decision === "rejected" ? "danger" : "ghost"}
                      onClick={() => setDecision(p.path, "rejected")}
                    >
                      Reject
                    </Button>
                    <span
                      className={cn(
                        "self-center text-[10px]",
                        decision === "approved" && "text-emerald-400",
                        decision === "rejected" && "text-red-400",
                        decision === "pending" && "text-zinc-600"
                      )}
                    >
                      {decision}
                    </span>
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="border-t border-zinc-800 px-3 py-2 text-[10px] text-zinc-500">
        Dry-run uses existing planner module via Dashboard actions. Approvals
        here are ECC human intent markers — they do not auto-publish.
      </div>
    </div>
  );
}
