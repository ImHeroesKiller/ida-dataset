/**
 * GET /api/search?q=… — lightweight knowledge search over existing repo data.
 * Restores topbar search (was 404). No new architecture.
 */

import { NextRequest, NextResponse } from "next/server";
import { listDatasets } from "@/lib/repo-data";
import { listMissions } from "@/lib/learning";
import { getSessionsDashboard } from "@/lib/sessions";
import { getSourceHealthDashboard } from "@/lib/source-health";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

export async function GET(req: NextRequest) {
  const q = (req.nextUrl.searchParams.get("q") || "").trim().toLowerCase();
  if (!q) {
    return NextResponse.json({ results: [] });
  }

  const results: Array<{
    type: string;
    id: string;
    title: string;
    subtitle?: string;
    href: string;
  }> = [];

  try {
    for (const d of listDatasets()) {
      const blob = `${d.name} ${d.domain} ${d.relativePath}`.toLowerCase();
      if (!blob.includes(q)) continue;
      results.push({
        type: "dataset",
        id: d.id || d.relativePath,
        title: d.name,
        subtitle: `${d.domain} · ${d.rowCount} rows`,
        href: "/datasets",
      });
      if (results.length >= 20) break;
    }
  } catch {
    /* ignore */
  }

  try {
    for (const m of listMissions()) {
      const id = String(m.mission_id || m.id || "");
      const title = String(m.title || m.mission_title || id);
      const blob = `${id} ${title} ${m.status || ""}`.toLowerCase();
      if (!blob.includes(q)) continue;
      results.push({
        type: "mission",
        id: id || title,
        title,
        subtitle: String(m.status || ""),
        href: "/missions",
      });
      if (results.length >= 30) break;
    }
  } catch {
    /* ignore */
  }

  try {
    const dash = getSessionsDashboard();
    for (const s of dash.sessions || []) {
      const blob = `${s.session_id} ${s.mission || ""} ${s.status || ""}`.toLowerCase();
      if (!blob.includes(q)) continue;
      results.push({
        type: "session",
        id: s.session_id,
        title: s.session_id,
        subtitle: String(s.mission || s.status || ""),
        href: "/",
      });
      if (results.length >= 40) break;
    }
  } catch {
    /* ignore */
  }

  try {
    const dash = getSourceHealthDashboard();
    for (const raw of dash.sources || []) {
      const name = String(raw.name || "");
      const id = String(raw.source_id || name);
      const blob = `${id} ${name} ${raw.category || ""}`.toLowerCase();
      if (!blob.includes(q)) continue;
      results.push({
        type: "source",
        id,
        title: name || id,
        subtitle: String(raw.health_status || raw.status || ""),
        href: "/sources",
      });
      if (results.length >= 50) break;
    }
  } catch {
    /* ignore */
  }

  return NextResponse.json({ results: results.slice(0, 40) });
}
