"use client";

import { useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useInspector } from "@/components/layout/inspector-context";

type Row = {
  entityId: string;
  entityName: string;
  entityType: string;
  category: string;
  confidence: number;
  approvalMode: string;
  reviewRequired: boolean;
  crawlingEnabled: boolean;
  extractionEnabled: boolean;
  publishingEnabled: boolean;
  allowedSources: string[];
  forbiddenSources: string[];
};

export function PolicyClient({
  rows,
  rawPolicies,
  sourcesSummary,
}: {
  rows: Row[];
  rawPolicies: Record<string, unknown>;
  sourcesSummary: { allowed: string[]; forbidden: string[] };
}) {
  const { inspect } = useInspector();
  const [drafts, setDrafts] = useState<Record<string, Partial<Row>>>({});
  const [msg, setMsg] = useState<string | null>(null);
  const [q, setQ] = useState("");

  const filtered = useMemo(() => {
    const needle = q.trim().toLowerCase();
    if (!needle) return rows;
    return rows.filter(
      (r) =>
        r.entityName.toLowerCase().includes(needle) ||
        r.entityType.toLowerCase().includes(needle) ||
        r.category.toLowerCase().includes(needle)
    );
  }, [rows, q]);

  function update(id: string, patch: Partial<Row>) {
    setDrafts((d) => ({ ...d, [id]: { ...d[id], ...patch } }));
  }

  function merged(row: Row): Row {
    return { ...row, ...(drafts[row.entityId] ?? {}) };
  }

  function validateAll() {
    const issues: string[] = [];
    for (const row of rows) {
      const m = merged(row);
      if (m.confidence < 0 || m.confidence > 1) {
        issues.push(`${m.entityName}: confidence must be 0–1`);
      }
      if (!["manual", "semi_automatic", "automatic"].includes(m.approvalMode)) {
        issues.push(`${m.entityName}: invalid approval mode`);
      }
    }
    if (issues.length) {
      setMsg(`Validation failed: ${issues.slice(0, 3).join("; ")}`);
    } else {
      setMsg("Validation OK — drafts are local only (policy source remains YAML).");
    }
  }

  function saveDrafts() {
    // ECC is orchestration UI — does not write production policy files directly.
    setMsg(
      "Save recorded as local draft intent. Persist via config PR / policy workflow — never bypass Policy Engine files."
    );
  }

  return (
    <div>
      <div className="flex flex-wrap items-center gap-2 border-b border-zinc-800 px-3 py-2">
        <Input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Filter entities…"
          className="max-w-xs"
        />
        <Button size="sm" variant="secondary" onClick={validateAll}>
          Validate
        </Button>
        <Button size="sm" onClick={saveDrafts}>
          Save draft
        </Button>
        {msg ? <span className="text-[11px] text-zinc-400">{msg}</span> : null}
      </div>
      <div className="overflow-x-auto">
        <table className="w-full min-w-[1000px] text-left text-xs">
          <thead className="border-b border-zinc-800 text-[10px] uppercase tracking-wide text-zinc-500">
            <tr>
              <th className="px-3 py-2">Entity</th>
              <th className="px-3 py-2">Type</th>
              <th className="px-3 py-2">Confidence</th>
              <th className="px-3 py-2">Approval</th>
              <th className="px-3 py-2">Allowed sources</th>
              <th className="px-3 py-2">Forbidden sources</th>
              <th className="px-3 py-2">Features</th>
              <th className="px-3 py-2">Edit</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((row) => {
              const m = merged(row);
              return (
                <tr
                  key={row.entityId}
                  className="border-b border-zinc-900/80 hover:bg-zinc-900/40"
                >
                  <td className="px-3 py-2">
                    <button
                      className="text-left font-medium text-zinc-100 hover:underline"
                      onClick={() =>
                        inspect({
                          kind: "policy",
                          title: m.entityName,
                          subtitle: m.entityId,
                          meta: {
                            Type: m.entityType,
                            Confidence: String(m.confidence),
                            Approval: m.approvalMode,
                            Review: String(m.reviewRequired),
                          },
                          body: JSON.stringify(
                            {
                              allowedSources: m.allowedSources,
                              forbiddenSources: m.forbiddenSources,
                              features: {
                                crawling: m.crawlingEnabled,
                                extraction: m.extractionEnabled,
                                publishing: m.publishingEnabled,
                              },
                              raw: rawPolicies.features,
                              sourcesSummary,
                            },
                            null,
                            2
                          ),
                        })
                      }
                    >
                      {m.entityName}
                    </button>
                  </td>
                  <td className="px-3 py-2 text-zinc-400">{m.entityType}</td>
                  <td className="px-3 py-2">
                    <Input
                      type="number"
                      step="0.05"
                      min={0}
                      max={1}
                      value={m.confidence}
                      onChange={(e) =>
                        update(row.entityId, {
                          confidence: Number(e.target.value),
                        })
                      }
                      className="h-7 w-20"
                    />
                  </td>
                  <td className="px-3 py-2">
                    <select
                      className="h-7 rounded-md border border-zinc-800 bg-zinc-950 px-1 text-xs"
                      value={m.approvalMode}
                      onChange={(e) =>
                        update(row.entityId, { approvalMode: e.target.value })
                      }
                    >
                      <option value="manual">manual</option>
                      <option value="semi_automatic">semi_automatic</option>
                      <option value="automatic">automatic</option>
                    </select>
                  </td>
                  <td className="max-w-[180px] truncate px-3 py-2 text-zinc-500">
                    {m.allowedSources.join(", ") || "—"}
                  </td>
                  <td className="max-w-[180px] truncate px-3 py-2 text-zinc-500">
                    {m.forbiddenSources.join(", ") || "—"}
                  </td>
                  <td className="px-3 py-2 text-[10px] text-zinc-500">
                    c:{String(m.crawlingEnabled)} e:
                    {String(m.extractionEnabled)} p:
                    {String(m.publishingEnabled)}
                  </td>
                  <td className="px-3 py-2">
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() =>
                        update(row.entityId, {
                          confidence: row.confidence,
                          approvalMode: row.approvalMode,
                        })
                      }
                    >
                      Reset
                    </Button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
