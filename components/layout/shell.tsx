"use client";

import { Sidebar } from "@/components/layout/sidebar";
import { Topbar } from "@/components/layout/topbar";
import { BottomConsole } from "@/components/console/bottom-console";
import { InspectorProvider } from "@/components/layout/inspector-context";

/**
 * Application shell — chrome only (sidebar, topbar, main, console).
 * LearningProvider lives in RootLayout so page components and shell
 * children share one context during SSR/prerender and client navigation.
 * InspectorProvider: restores inspect() for internal operator pages.
 */
export function Shell({
  title,
  children,
}: {
  title?: string;
  children: React.ReactNode;
}) {
  return (
    <InspectorProvider>
      <div className="flex h-screen w-screen overflow-hidden bg-[var(--bg)] text-[var(--text)]">
        <Sidebar />
        <div className="flex min-w-0 flex-1 flex-col">
          <Topbar title={title} />
          <main className="min-h-0 flex-1 overflow-y-auto px-6 py-8 scrollbar-thin sm:px-8">
            {children}
          </main>
          <BottomConsole />
        </div>
      </div>
    </InspectorProvider>
  );
}
