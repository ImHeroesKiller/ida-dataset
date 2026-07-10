"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { NAV_ITEMS } from "@/lib/nav";
import { cn } from "@/lib/utils";

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="flex h-full w-[var(--sidebar-w)] shrink-0 flex-col border-r border-zinc-800/90 bg-[#0b0b0d]">
      <div className="flex h-[var(--topbar-h)] items-center gap-2 border-b border-zinc-800/90 px-4">
        <div className="flex h-6 w-6 items-center justify-center rounded-md border border-zinc-700 bg-zinc-900 text-[10px] font-semibold tracking-wide text-zinc-100">
          IDA
        </div>
        <div className="min-w-0">
          <div className="truncate text-xs font-semibold tracking-tight text-zinc-100">
            Executive Control
          </div>
          <div className="truncate text-[10px] text-zinc-500">
            Knowledge Platform
          </div>
        </div>
      </div>

      <nav className="flex-1 space-y-0.5 overflow-y-auto p-2 scrollbar-thin">
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
                "flex items-center gap-2 rounded-md px-2.5 py-1.5 text-xs transition-colors",
                active
                  ? "bg-zinc-900 text-zinc-50 ring-1 ring-zinc-800"
                  : "text-zinc-400 hover:bg-zinc-900/70 hover:text-zinc-200"
              )}
            >
              <Icon className="h-3.5 w-3.5 shrink-0 opacity-80" />
              <span className="truncate">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="border-t border-zinc-800/90 p-3">
        <div className="rounded-md border border-zinc-800 bg-zinc-950/80 p-2.5">
          <div className="text-[10px] font-medium uppercase tracking-wider text-zinc-500">
            Control model
          </div>
          <p className="mt-1 text-[11px] leading-relaxed text-zinc-400">
            Planner proposes. Policy governs. Human decides. Pipeline executes.
            Publisher publishes.
          </p>
        </div>
      </div>
    </aside>
  );
}
