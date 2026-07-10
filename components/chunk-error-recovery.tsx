"use client";

import { useEffect } from "react";

const STORAGE_KEY = "ida-chunk-reload";
const RELOAD_WINDOW_MS = 15_000;

/**
 * Recover from intermittent ChunkLoadError after rolling Vercel deploys.
 *
 * When a previous HTML document references a hashed chunk that no longer
 * exists on the CDN (404), Next/webpack throws ChunkLoadError. A single
 * automatic full reload fetches fresh HTML + matching assets. Without this,
 * users see a broken shell until they hard-refresh.
 */
export function ChunkErrorRecovery() {
  useEffect(() => {
    if (typeof window === "undefined") return;

    const shouldReload = (): boolean => {
      try {
        const raw = sessionStorage.getItem(STORAGE_KEY);
        const last = raw ? Number(raw) : 0;
        if (last && Date.now() - last < RELOAD_WINDOW_MS) {
          // Already reloaded recently — avoid loop.
          return false;
        }
        sessionStorage.setItem(STORAGE_KEY, String(Date.now()));
        return true;
      } catch {
        return true;
      }
    };

    const isChunkFailure = (msg: string, src?: string | null): boolean => {
      const hay = `${msg} ${src || ""}`.toLowerCase();
      return (
        hay.includes("chunkloaderror") ||
        hay.includes("loading chunk") ||
        hay.includes("failed to fetch dynamically imported module") ||
        hay.includes("loading css chunk") ||
        (hay.includes("/_next/static/chunks/") &&
          (hay.includes("404") || hay.includes("failed to load")))
      );
    };

    const onError = (event: ErrorEvent) => {
      const msg = event.message || "";
      const src =
        (event.filename || "") +
        " " +
        ((event.target as HTMLElement | null)?.getAttribute?.("src") || "");
      if (!isChunkFailure(msg, src)) return;
      if (!shouldReload()) return;
      // Full navigation — not soft router refresh — so HTML + build id match.
      window.location.reload();
    };

    const onRejection = (event: PromiseRejectionEvent) => {
      const reason = event.reason;
      const msg =
        reason instanceof Error
          ? `${reason.name} ${reason.message}`
          : String(reason ?? "");
      if (!isChunkFailure(msg)) return;
      if (!shouldReload()) return;
      event.preventDefault?.();
      window.location.reload();
    };

    window.addEventListener("error", onError, true);
    window.addEventListener("unhandledrejection", onRejection);
    return () => {
      window.removeEventListener("error", onError, true);
      window.removeEventListener("unhandledrejection", onRejection);
    };
  }, []);

  return null;
}
