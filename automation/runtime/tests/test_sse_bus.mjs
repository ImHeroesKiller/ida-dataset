/**
 * Stress test for shared SSE bus ref-counting (Node-side simulation).
 * Run: node automation/runtime/tests/test_sse_bus.mjs
 */

import assert from "node:assert/strict";

function createBus() {
  let es = null;
  let refCount = 0;
  let nextId = 1;
  const subs = new Map();
  let connected = false;
  let openCount = 0;
  let closeCount = 0;

  function ensureSource() {
    if (es) return;
    es = { closed: false };
    openCount += 1;
    connected = true;
  }

  function teardownIfIdle() {
    if (refCount > 0) return;
    if (es) {
      es.closed = true;
      es = null;
      closeCount += 1;
    }
    connected = false;
  }

  function subscribe(handlers = {}) {
    const id = nextId++;
    subs.set(id, { id, ...handlers });
    refCount += 1;
    ensureSource();
    handlers.onConnection?.(connected);
    return () => {
      subs.delete(id);
      refCount = Math.max(0, refCount - 1);
      teardownIfIdle();
    };
  }

  function stats() {
    return {
      refCount,
      subscriberCount: subs.size,
      hasSource: Boolean(es),
      openCount,
      closeCount,
    };
  }

  return { subscribe, stats };
}

function testDualMountSingleSource() {
  const bus = createBus();
  const u1 = bus.subscribe();
  const u2 = bus.subscribe();
  const s = bus.stats();
  assert.equal(s.refCount, 2);
  assert.equal(s.openCount, 1, "only one EventSource for two mounts");
  assert.equal(s.hasSource, true);
  u1();
  assert.equal(bus.stats().hasSource, true);
  u2();
  assert.equal(bus.stats().hasSource, false);
  assert.equal(bus.stats().closeCount, 1);
  console.log("  PASS  dual_mount_single_source");
}

function testBrowserRefreshCycle() {
  const bus = createBus();
  for (let i = 0; i < 20; i++) {
    const unsubs = [bus.subscribe(), bus.subscribe()];
    assert.equal(bus.stats().openCount, i + 1);
    unsubs.forEach((u) => u());
    assert.equal(bus.stats().hasSource, false);
    assert.equal(bus.stats().refCount, 0);
  }
  assert.equal(bus.stats().closeCount, 20);
  console.log("  PASS  browser_refresh_cycle");
}

function testUnexpectedDisconnectCleanup() {
  const bus = createBus();
  const unsubs = [];
  for (let i = 0; i < 10; i++) unsubs.push(bus.subscribe());
  assert.equal(bus.stats().openCount, 1);
  unsubs.slice(0, 5).forEach((u) => u());
  assert.equal(bus.stats().refCount, 5);
  assert.equal(bus.stats().hasSource, true);
  unsubs.slice(5).forEach((u) => u());
  assert.equal(bus.stats().hasSource, false);
  assert.equal(bus.stats().refCount, 0);
  console.log("  PASS  unexpected_disconnect_cleanup");
}

function testNoListenerAccumulation() {
  const bus = createBus();
  for (let i = 0; i < 50; i++) {
    const u = bus.subscribe();
    u();
  }
  const s = bus.stats();
  assert.equal(s.refCount, 0);
  assert.equal(s.subscriberCount, 0);
  assert.equal(s.hasSource, false);
  assert.equal(s.openCount, 50);
  assert.equal(s.closeCount, 50);
  console.log("  PASS  no_listener_accumulation");
}

console.log("SSE bus ownership stress tests");
console.log("=".repeat(50));
testDualMountSingleSource();
testBrowserRefreshCycle();
testUnexpectedDisconnectCleanup();
testNoListenerAccumulation();
console.log("=".repeat(50));
console.log("All SSE bus tests passed");
