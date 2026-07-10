"use client";

import { useMemo, useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { useInspector } from "@/components/layout/inspector-context";
import { cn } from "@/lib/utils";

type Row = Record<string, string>;

export function OntologyClient({
  entities,
  relationships,
  entityTypes,
}: {
  entities: Row[];
  relationships: Row[];
  entityTypes: Row[];
}) {
  const { inspect } = useInspector();
  const [q, setQ] = useState("");
  const [typeFilter, setTypeFilter] = useState("all");
  const [selectedId, setSelectedId] = useState<string | null>(
    entities[0]?.["Entity ID"] ?? null
  );

  const filteredEntities = useMemo(() => {
    return entities.filter((e) => {
      const matchType =
        typeFilter === "all" || e["Entity Type"] === typeFilter;
      const blob = `${e["Entity Name"]} ${e["Entity ID"]} ${e["Description"]}`.toLowerCase();
      return matchType && blob.includes(q.trim().toLowerCase());
    });
  }, [entities, q, typeFilter]);

  const selected = entities.find((e) => e["Entity ID"] === selectedId) ?? null;

  const related = useMemo(() => {
    if (!selected) return [] as Row[];
    const name = selected["Entity Name"];
    return relationships.filter(
      (r) => r["Source Entity"] === name || r["Target Entity"] === name
    );
  }, [relationships, selected]);

  // Lightweight graph layout: place nodes on a circle, draw edges as SVG lines
  const graph = useMemo(() => {
    const names = Array.from(
      new Set(
        relationships.flatMap((r) => [r["Source Entity"], r["Target Entity"]])
      )
    ).filter(Boolean);
    const focus = selected?.["Entity Name"];
    const subset = focus
      ? names.filter(
          (n) =>
            n === focus ||
            relationships.some(
              (r) =>
                (r["Source Entity"] === focus && r["Target Entity"] === n) ||
                (r["Target Entity"] === focus && r["Source Entity"] === n)
            )
        )
      : names.slice(0, 18);

    const w = 640;
    const h = 360;
    const cx = w / 2;
    const cy = h / 2;
    const radius = Math.min(w, h) * 0.38;
    const nodes = subset.map((name, i) => {
      const angle = (i / Math.max(subset.length, 1)) * Math.PI * 2 - Math.PI / 2;
      return {
        name,
        x: cx + radius * Math.cos(angle),
        y: cy + radius * Math.sin(angle),
      };
    });
    const pos = Object.fromEntries(nodes.map((n) => [n.name, n]));
    const edges = relationships
      .filter(
        (r) => pos[r["Source Entity"]] && pos[r["Target Entity"]]
      )
      .map((r) => ({
        id: r["Relationship ID"],
        label: r["Relationship"],
        x1: pos[r["Source Entity"]].x,
        y1: pos[r["Source Entity"]].y,
        x2: pos[r["Target Entity"]].x,
        y2: pos[r["Target Entity"]].y,
      }));
    return { w, h, nodes, edges };
  }, [relationships, selected]);

  return (
    <div className="grid gap-3 xl:grid-cols-[280px_1fr]">
      <Card className="min-h-[480px]">
        <CardHeader title="Entity browser" description="Search & filter" />
        <CardBody className="space-y-2">
          <Input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search entities…"
          />
          <select
            className="h-8 w-full rounded-md border border-zinc-800 bg-zinc-950 px-2 text-xs"
            value={typeFilter}
            onChange={(e) => setTypeFilter(e.target.value)}
          >
            <option value="all">All types</option>
            {entityTypes.map((t) => (
              <option
                key={t["Entity Type ID"]}
                value={t["Entity Type Name"]}
              >
                {t["Entity Type Name"]}
              </option>
            ))}
          </select>
          <div className="max-h-[420px] space-y-0.5 overflow-y-auto scrollbar-thin">
            {filteredEntities.map((e) => (
              <button
                key={e["Entity ID"]}
                className={cn(
                  "flex w-full flex-col rounded-md px-2 py-1.5 text-left hover:bg-zinc-900",
                  selectedId === e["Entity ID"] && "bg-zinc-900 ring-1 ring-zinc-700"
                )}
                onClick={() => {
                  setSelectedId(e["Entity ID"]);
                  inspect({
                    kind: "entity",
                    title: e["Entity Name"],
                    subtitle: e["Entity ID"],
                    meta: {
                      Type: e["Entity Type"],
                      Category: e["Category"],
                      Parent: e["Parent Entity"] || "—",
                      Status: e["Status"],
                      Version: e["Version"],
                    },
                    body: e["Description"],
                  });
                }}
              >
                <span className="text-xs text-zinc-100">{e["Entity Name"]}</span>
                <span className="text-[10px] text-zinc-500">
                  {e["Entity Type"]} · {e["Category"]}
                </span>
              </button>
            ))}
          </div>
        </CardBody>
      </Card>

      <div className="space-y-3">
        <Card>
          <CardHeader
            title="Relationship graph"
            description="SVG projection from relationships.csv (focus neighborhood)"
          />
          <CardBody className="overflow-x-auto">
            <svg
              viewBox={`0 0 ${graph.w} ${graph.h}`}
              className="h-[360px] w-full rounded-md border border-zinc-900 bg-[#08080a]"
            >
              {graph.edges.map((e) => (
                <g key={e.id}>
                  <line
                    x1={e.x1}
                    y1={e.y1}
                    x2={e.x2}
                    y2={e.y2}
                    stroke="#3f3f46"
                    strokeWidth="1"
                  />
                </g>
              ))}
              {graph.nodes.map((n) => (
                <g
                  key={n.name}
                  className="cursor-pointer"
                  onClick={() => {
                    const ent = entities.find((e) => e["Entity Name"] === n.name);
                    if (ent) {
                      setSelectedId(ent["Entity ID"]);
                      inspect({
                        kind: "entity",
                        title: ent["Entity Name"],
                        subtitle: ent["Entity ID"],
                        meta: {
                          Type: ent["Entity Type"],
                          Category: ent["Category"],
                        },
                        body: ent["Description"],
                      });
                    }
                  }}
                >
                  <circle
                    cx={n.x}
                    cy={n.y}
                    r={selected?.["Entity Name"] === n.name ? 8 : 5}
                    fill={
                      selected?.["Entity Name"] === n.name ? "#e4e4e7" : "#52525b"
                    }
                  />
                  <text
                    x={n.x}
                    y={n.y + 16}
                    textAnchor="middle"
                    className="fill-zinc-400"
                    style={{ fontSize: 10 }}
                  >
                    {n.name}
                  </text>
                </g>
              ))}
            </svg>
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Relationships"
            description={
              selected
                ? `Edges involving ${selected["Entity Name"]}`
                : "Select an entity"
            }
          />
          <CardBody className="space-y-1">
            {related.length === 0 ? (
              <p className="text-xs text-zinc-500">No relationships in view.</p>
            ) : (
              related.map((r) => (
                <button
                  key={r["Relationship ID"]}
                  className="flex w-full items-center justify-between rounded-md border border-zinc-900 px-2 py-1.5 text-left text-xs hover:bg-zinc-900"
                  onClick={() =>
                    inspect({
                      kind: "relationship",
                      title: `${r["Source Entity"]} ${r["Relationship"]} ${r["Target Entity"]}`,
                      subtitle: r["Relationship ID"],
                      meta: {
                        Direction: r["Direction"],
                        Status: r["Status"],
                        TypeId: r["Relationship Type ID"],
                      },
                      body: r["Description"],
                    })
                  }
                >
                  <span className="text-zinc-200">
                    <span className="text-zinc-400">{r["Source Entity"]}</span>{" "}
                    <span className="text-zinc-100">{r["Relationship"]}</span>{" "}
                    <span className="text-zinc-400">{r["Target Entity"]}</span>
                  </span>
                  <span className="text-[10px] text-zinc-600">
                    {r["Direction"]}
                  </span>
                </button>
              ))
            )}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}
