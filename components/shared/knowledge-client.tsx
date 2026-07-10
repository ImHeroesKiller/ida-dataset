"use client";

import { useState } from "react";
import { Card, CardBody } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

type Category = {
  id: string;
  label: string;
  description: string;
  rows: number;
  populated: boolean;
  datasets: { name: string; path: string; rows: number; domain: string }[];
};

export function KnowledgeClient({ categories }: { categories: Category[] }) {
  const [openId, setOpenId] = useState<string | null>(null);
  const [detail, setDetail] = useState<{
    tables: {
      name: string;
      path: string;
      headers: string[];
      rows: Record<string, string>[];
      rowCount: number;
    }[];
  } | null>(null);
  const [loading, setLoading] = useState(false);

  async function openCategory(id: string) {
    if (openId === id) {
      setOpenId(null);
      setDetail(null);
      return;
    }
    setOpenId(id);
    setLoading(true);
    try {
      const res = await fetch(`/api/knowledge?category=${encodeURIComponent(id)}`);
      const data = await res.json();
      setDetail({ tables: data.tables || [] });
    } catch {
      setDetail({ tables: [] });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <header>
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-50">
          Knowledge
        </h1>
        <p className="mt-2 text-base text-zinc-400">
          Explore what IDA knows — industry, pain points, solutions, and more.
        </p>
      </header>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {categories.map((cat) => (
          <button
            key={cat.id}
            type="button"
            onClick={() => openCategory(cat.id)}
            className="text-left"
          >
            <Card
              className={cn(
                "border-zinc-800/50 bg-zinc-950/40 transition-all hover:border-zinc-700",
                openId === cat.id && "border-sky-500/40 ring-1 ring-sky-500/20"
              )}
            >
              <CardBody className="p-5">
                <div className="flex items-start justify-between gap-2">
                  <h2 className="text-lg font-medium text-zinc-50">
                    {cat.label}
                  </h2>
                  <span
                    className={cn(
                      "rounded-full px-2 py-0.5 text-[11px]",
                      cat.populated
                        ? "bg-emerald-500/15 text-emerald-300"
                        : "bg-zinc-800 text-zinc-500"
                    )}
                  >
                    {cat.rows} rows
                  </span>
                </div>
                <p className="mt-2 text-sm text-zinc-500">{cat.description}</p>
              </CardBody>
            </Card>
          </button>
        ))}
      </div>

      {openId ? (
        <Card className="border-zinc-800/50 bg-zinc-950/40">
          <CardBody className="space-y-4 p-6">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-medium text-zinc-100">
                {categories.find((c) => c.id === openId)?.label} detail
              </h3>
              <Button size="sm" variant="ghost" onClick={() => setOpenId(null)}>
                Close
              </Button>
            </div>
            {loading ? (
              <p className="text-sm text-zinc-500">Loading…</p>
            ) : !detail?.tables?.length ? (
              <p className="text-sm text-zinc-500">No data yet in this category.</p>
            ) : (
              detail.tables.map((table) => (
                <div key={table.path} className="space-y-2">
                  <p className="text-xs text-zinc-500">
                    {table.name} · {table.rowCount} rows
                  </p>
                  <div className="overflow-x-auto rounded-xl border border-zinc-800/60">
                    <table className="w-full min-w-[640px] text-left text-xs">
                      <thead className="bg-zinc-900/50 text-[10px] uppercase tracking-wider text-zinc-500">
                        <tr>
                          {table.headers.slice(0, 8).map((h) => (
                            <th key={h} className="px-3 py-2 font-medium">
                              {h}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {table.rows.length === 0 ? (
                          <tr>
                            <td
                              colSpan={Math.min(8, table.headers.length || 1)}
                              className="px-3 py-6 text-zinc-500"
                            >
                              Empty dataset
                            </td>
                          </tr>
                        ) : (
                          table.rows.map((row, i) => (
                            <tr
                              key={i}
                              className="border-t border-zinc-900/80 text-zinc-300"
                            >
                              {table.headers.slice(0, 8).map((h) => (
                                <td
                                  key={h}
                                  className="max-w-[12rem] truncate px-3 py-2"
                                >
                                  {row[h] || "—"}
                                </td>
                              ))}
                            </tr>
                          ))
                        )}
                      </tbody>
                    </table>
                  </div>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      ) : null}
    </div>
  );
}
