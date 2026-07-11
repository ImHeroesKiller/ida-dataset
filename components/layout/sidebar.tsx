"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { NAV_ITEMS, PRODUCT } from "@/lib/nav";
import { cn } from "@/lib/utils";
import { useTheme } from "@/components/theme-provider";
import { useLearning } from "@/hooks/learning-provider";
import { Moon, Sun, Activity } from "lucide-react";
import { RoleBadge } from "@/components/ui/badge";

export function Sidebar() {
  const pathname = usePathname();
  const { theme, toggle } = useTheme();
  const { dashboard, activity } = useLearning();
  const [rowsToday, setRowsToday] = useState<number | null>(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const res = await fetch("/api/factory/status", { cache: "no-store" });
        if (!res.ok) return;
        const data = await res.json();
        if (alive && data?.kpis?.rows_added_today != null) {
          setRowsToday(Number(data.kpis.rows_added_today));
        }
      } catch {
        /* ignore */
      }
    })();
    return () => {
      alive = false;
    };
  }, [dashboard.status, activity.updated_at]);

  const running = Boolean(dashboard.github_actions?.running);
  const statusLabel = running
    ? "running"
    : String(activity.status || "").includes("error")
      ? "error"
      : "idle";

  return (
    <aside className="hidden h-full w-[var(--sidebar-w)] shrink-0 flex-col border-r border-[var(--border)] bg-[var(--sidebar-bg)] md:flex">
      <div className="flex h-[var(--topbar-h)] shrink-0 items-center gap-2 border-b border-[var(--border)] px-3">
        <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-[var(--radius-md)] bg-[var(--blue)] text-[10px] font-bold tracking-wide text-white">
          IDA
        </div>
        <div className="min-w-0">
          <div className="truncate text-xs font-semibold tracking-tight text-[var(--text)]">
            {PRODUCT.short}
          </div>
          <div className="truncate text-[10px] text-[var(--text-muted)]">
            Operator
          </div>
        </div>
      </div>

      <nav
        className="flex min-h-0 flex-1 flex-col gap-0.5 overflow-y-auto px-2 py-2 scrollbar-thin"
        aria-label="Primary"
      >
        {NAV_ITEMS.map((item) => {
          const active =
            item.href === "/"
              ? pathname === "/"
              : pathname === item.href || pathname.startsWith(`${item.href}/`);
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "relative flex items-center gap-2 rounded-[var(--radius-md)] px-2.5 py-1.5 text-xs font-medium transition-colors",
                active
                  ? "bg-[var(--sidebar-active-bg)] text-[var(--sidebar-active-fg)]"
                  : "text-[var(--text-secondary)] hover:bg-[var(--panel-2)] hover:text-[var(--text)]"
              )}
              aria-current={active ? "page" : undefined}
            >
              {active ? (
                <span
                  className="absolute top-1/2 left-0 h-4 w-0.5 -translate-y-1/2 rounded-r bg-[var(--sidebar-active-bar)]"
                  aria-hidden
                />
              ) : null}
              <Icon className="h-3.5 w-3.5 shrink-0 opacity-90" aria-hidden />
              <span className="truncate">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="shrink-0 border-t border-[var(--border)] px-2 py-2">
        <div className="rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel-2)] p-2">
          <div className="mb-1.5 flex items-center gap-1.5 text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
            <Activity className="h-3 w-3" aria-hidden />
            Status
          </div>
          <div className="space-y-1.5">
            <div className="flex items-center justify-between gap-2">
              <span className="text-[11px] text-[var(--text-secondary)]">
                Learning
              </span>
              <RoleBadge
                role={
                  statusLabel === "running"
                    ? "running"
                    : statusLabel === "error"
                      ? "error"
                      : "idle"
                }
              />
            </div>
            <div className="flex items-center justify-between gap-2 text-[11px]">
              <span className="text-[var(--text-secondary)]">Rows today</span>
              <span className="font-semibold tabular-nums text-[var(--text)]">
                {rowsToday != null ? `+${rowsToday}` : "—"}
              </span>
            </div>
          </div>
        </div>

        <button
          type="button"
          onClick={toggle}
          className="mt-2 flex w-full items-center justify-center gap-1.5 rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel)] px-2 py-1.5 text-[11px] font-semibold text-[var(--text)] transition-colors hover:bg-[var(--panel-2)]"
        >
          {theme === "dark" ? (
            <Sun className="h-3.5 w-3.5" aria-hidden />
          ) : (
            <Moon className="h-3.5 w-3.5" aria-hidden />
          )}
          {theme === "dark" ? "Light" : "Dark"}
        </button>
      </div>
    </aside>
  );
}
