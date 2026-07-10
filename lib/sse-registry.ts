/**
 * Lightweight in-process SSE connection registry for diagnostics.
 * Tracks active live-stream listeners without raising EventEmitter limits.
 */

let activeListeners = 0;
let totalOpened = 0;
let totalClosed = 0;
let lastOpenAt: string | null = null;
let lastCloseAt: string | null = null;

export function sseListenerOpened(): void {
  activeListeners += 1;
  totalOpened += 1;
  lastOpenAt = new Date().toISOString();
}

export function sseListenerClosed(): void {
  activeListeners = Math.max(0, activeListeners - 1);
  totalClosed += 1;
  lastCloseAt = new Date().toISOString();
}

export function getSseListenerStats() {
  return {
    active_listeners: activeListeners,
    total_opened: totalOpened,
    total_closed: totalClosed,
    last_open_at: lastOpenAt,
    last_close_at: lastCloseAt,
  };
}
