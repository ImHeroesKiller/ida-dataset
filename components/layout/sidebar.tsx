"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { NAV_ITEMS, PRODUCT } from "@/lib/nav";
import { cn } from "@/lib/utils";
import { useTheme } from "@/components/theme-provider";
import { Moon, Sun } from "lucide-react";

export function Sidebar() {
  const pathname = usePathname();
  const { theme, toggle } = useTheme();

  return (
    <aside className="flex h-full w-[var(--sidebar-w)] shrink-0 flex-col border-r border-[var(--border)] bg-[var(--sidebar-bg)]">
      {/* Brand — fixed height, no empty placeholder block */}
      <div className="flex h-[var(--topbar-h)] shrink-0 items-center gap-3 border-b border-[var(--border)] px-4">
        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-[var(--text)] text-[11px] font-bold tracking-wide text-[var(--bg)]">
          IDA
        </div>
        <div className="min-w-0">
          <div className="truncate text-sm font-semibold tracking-tight text-[var(--text)]">
            {PRODUCT.short}
          </div>
          <div className="truncate text-[11px] text-[var(--text-faint)]">
            {PRODUCT.tagline}
          </div>
        </div>
      </div>

      {/* Nav — consistent spacing; Dashboard first via NAV_ITEMS */}
      <nav className="flex min-h-0 flex-1 flex-col gap-0.5 overflow-y-auto px-2.5 py-3 scrollbar-thin">
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
                "flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm transition-colors",
                active
                  ? "bg-[var(--sidebar-active-bg)] font-medium text-[var(--sidebar-active-fg)]"
                  : "text-[var(--text-muted)] hover:bg-[var(--panel-2)] hover:text-[var(--text)]"
              )}
            >
              <Icon className="h-4 w-4 shrink-0 opacity-80" />
              <span className="truncate">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      {/* Footer — theme toggle only (no empty white block) */}
      <div className="mt-auto shrink-0 border-t border-[var(--border)] px-3 py-3">
        <button
          type="button"
          onClick={toggle}
          className="flex w-full items-center justify-center gap-2 rounded-xl border border-[var(--border)] bg-[var(--panel)] px-3 py-2 text-xs font-medium text-[var(--text)] transition-colors hover:bg-[var(--panel-2)]"
        >
          {theme === "dark" ? (
            <Sun className="h-3.5 w-3.5" />
          ) : (
            <Moon className="h-3.5 w-3.5" />
          )}
          {theme === "dark" ? "Light mode" : "Dark mode"}
        </button>
      </div>
    </aside>
  );
}
