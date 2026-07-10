/**
 * Server-side live runtime manager.
 *
 * Lifecycle: idle → starting → running → stopping → stopped → failed
 * Enforces single-instance lock, real startup diagnostics, structured errors.
 * Never hides 503 with a generic message — always reports component + recovery.
 */

import { spawn, type ChildProcess } from "child_process";
import fs from "fs";
import path from "path";
import { randomBytes } from "crypto";
import { getRepoRoot } from "@/lib/paths";

export type RuntimeState =
  | "idle"
  | "starting"
  | "running"
  | "stopping"
  | "stopped"
  | "failed";

export type HealthLevel = "healthy" | "warning" | "failed" | "disabled";

export type RuntimeHealth = {
  runtime: HealthLevel;
  scheduler: HealthLevel;
  connector: HealthLevel;
  queue: HealthLevel;
  sse: HealthLevel;
  publisher: HealthLevel;
};

export type RuntimeFailure = {
  timestamp: string;
  component: string;
  exception: string;
  message: string;
  stack_trace?: string;
  correlation_id: string;
  session_id?: string | null;
  recovery_action: string;
  recoverable?: boolean;
  recovery_suggestion?: string;
  meta?: Record<string, unknown>;
};

export type RuntimeStatus = {
  status: RuntimeState | string;
  session_id: string | null;
  correlation_id: string | null;
  pid: number | null;
  started_at: string | null;
  stopped_at: string | null;
  current_stage: string | null;
  current_task: string | null;
  documents_processed: number;
  knowledge_candidates: number;
  uptime_seconds: number;
  instruction?: string | null;
  last_error: RuntimeFailure | null;
  health: RuntimeHealth;
  updated_at?: string;
  host_capabilities?: HostCapabilities;
};

export type HostCapabilities = {
  python_available: boolean;
  python_path: string | null;
  python_version: string | null;
  vercel: boolean;
  ecc_disable_python: boolean;
  repo_root: string;
  can_spawn_runtime: boolean;
  block_reason: string | null;
};

export type StartResult = {
  ok: boolean;
  status_code: number;
  message: string;
  pid?: number;
  correlation_id: string;
  session_id?: string | null;
  instruction?: string;
  stream?: string;
  status?: RuntimeStatus;
  failure?: RuntimeFailure;
  recovery_suggestion?: string;
};

const STATE_REL = "automation/runtime/state";
const LOGS_REL = "automation/runtime/logs";
const LOCK_FILE = "runtime.lock.json";
const STATUS_FILE = "runtime.status.json";

function nowIso(): string {
  return new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
}

function newCorrelationId(): string {
  return `CORR-${randomBytes(6).toString("hex").toUpperCase()}`;
}

function ensureDirs(root: string): void {
  fs.mkdirSync(path.join(root, STATE_REL), { recursive: true });
  fs.mkdirSync(path.join(root, LOGS_REL), { recursive: true });
}

function lockPath(root: string): string {
  return path.join(root, STATE_REL, LOCK_FILE);
}

function statusPath(root: string): string {
  return path.join(root, STATE_REL, STATUS_FILE);
}

function readJsonFile(file: string): Record<string, unknown> | null {
  try {
    if (!fs.existsSync(file)) return null;
    return JSON.parse(fs.readFileSync(file, "utf8")) as Record<string, unknown>;
  } catch {
    return null;
  }
}

function writeJsonFile(file: string, data: unknown): void {
  const dir = path.dirname(file);
  fs.mkdirSync(dir, { recursive: true });
  const tmp = `${file}.tmp.${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2) + "\n", "utf8");
  fs.renameSync(tmp, file);
}

export function isPidAlive(pid: number | null | undefined): boolean {
  if (!pid || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch {
    return false;
  }
}

export function defaultHealth(): RuntimeHealth {
  return {
    runtime: "healthy",
    scheduler: "healthy",
    connector: "healthy",
    queue: "healthy",
    sse: "healthy",
    publisher: "healthy",
  };
}

export function resolvePython(root: string): {
  path: string | null;
  version: string | null;
  error: string | null;
} {
  const candidates = [
    process.env.IDA_PYTHON,
    process.env.PYTHON,
    "python3",
    "python",
  ].filter(Boolean) as string[];

  for (const bin of candidates) {
    try {
      const result = spawnSyncCapture(bin, ["--version"], root, 4000);
      if (result.exitCode === 0 || /Python\s+\d/i.test(result.stdout + result.stderr)) {
        return {
          path: bin,
          version: (result.stdout || result.stderr).trim() || null,
          error: null,
        };
      }
    } catch (e) {
      /* try next */
    }
  }
  return {
    path: null,
    version: null,
    error: "No working python3/python found on PATH (set IDA_PYTHON)",
  };
}

function spawnSyncCapture(
  cmd: string,
  args: string[],
  cwd: string,
  timeoutMs: number
): { exitCode: number | null; stdout: string; stderr: string } {
  // Use child_process.spawnSync via require to keep types simple
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const { spawnSync } = require("child_process") as typeof import("child_process");
  const r = spawnSync(cmd, args, {
    cwd,
    encoding: "utf8",
    timeout: timeoutMs,
    env: { ...process.env, PYTHONUNBUFFERED: "1" },
  });
  return {
    exitCode: r.status,
    stdout: String(r.stdout || ""),
    stderr: String(r.stderr || ""),
  };
}

export function probeHostCapabilities(root = getRepoRoot()): HostCapabilities {
  const vercel = Boolean(process.env.VERCEL);
  const eccDisable = process.env.ECC_DISABLE_PYTHON === "1";
  const py = resolvePython(root);
  let block: string | null = null;
  if (vercel) {
    block =
      "Host is Vercel serverless — detached Python subprocesses are not supported. " +
      "Run live learning on a local or long-running host.";
  } else if (eccDisable) {
    block =
      "ECC_DISABLE_PYTHON=1 is set — Python live runtime intentionally disabled on this host.";
  } else if (!py.path) {
    block = py.error;
  }

  // Preflight import only when not blocked by env
  if (!block && py.path) {
    const pre = spawnSyncCapture(
      py.path,
      ["-c", "import automation.learning.live_runtime"],
      root,
      8000
    );
    if (pre.exitCode !== 0) {
      block =
        `Python cannot import automation.learning.live_runtime: ` +
        `${(pre.stderr || pre.stdout || "unknown import error").slice(0, 500)}`;
    }
  }

  return {
    python_available: Boolean(py.path) && !block?.includes("cannot import"),
    python_path: py.path,
    python_version: py.version,
    vercel,
    ecc_disable_python: eccDisable,
    repo_root: root,
    can_spawn_runtime: !block,
    block_reason: block,
  };
}

export function reclaimStaleLock(root = getRepoRoot()): boolean {
  ensureDirs(root);
  const lock = readJsonFile(lockPath(root));
  if (!lock) return false;
  const pid = Number(lock.pid);
  if (isPidAlive(pid)) return false;
  try {
    fs.unlinkSync(lockPath(root));
  } catch {
    /* ignore */
  }
  const status = readRuntimeStatus(root);
  if (["starting", "running", "stopping"].includes(String(status.status))) {
    writeRuntimeStatus(
      {
        status: "failed",
        stopped_at: nowIso(),
        pid: null,
        last_error: {
          timestamp: nowIso(),
          component: "runtime.lock",
          exception: "StaleLock",
          message: `Lock held by dead process pid=${pid}; reclaimed.`,
          correlation_id: String(lock.correlation_id || newCorrelationId()),
          session_id: (lock.session_id as string) || null,
          recovery_action: "restart_runtime",
          recovery_suggestion:
            "Previous runtime process died without releasing the lock. You may retry start.",
        },
        health: { ...defaultHealth(), runtime: "failed" },
      },
      root
    );
  }
  return true;
}

export function readRuntimeStatus(root = getRepoRoot()): RuntimeStatus {
  ensureDirs(root);
  reclaimStaleLock(root);
  const raw = readJsonFile(statusPath(root)) || {};
  const startedAt = (raw.started_at as string) || null;
  let uptime = Number(raw.uptime_seconds || 0);
  const st = String(raw.status || "idle");
  if (startedAt && (st === "running" || st === "starting")) {
    const t = Date.parse(startedAt);
    if (!Number.isNaN(t)) {
      uptime = Math.max(0, Math.floor((Date.now() - t) / 1000));
    }
  }
  const lock = readJsonFile(lockPath(root));
  const pid = (raw.pid as number) ?? (lock?.pid as number) ?? null;
  // If status says running but pid dead → failed
  let status = st as RuntimeState | string;
  let lastError = (raw.last_error as RuntimeFailure) || null;
  if (
    (status === "running" || status === "starting") &&
    pid &&
    !isPidAlive(pid)
  ) {
    status = "failed";
    lastError = {
      timestamp: nowIso(),
      component: "runtime.process",
      exception: "ProcessDied",
      message: `Runtime process pid=${pid} is no longer alive`,
      correlation_id: String(raw.correlation_id || newCorrelationId()),
      session_id: (raw.session_id as string) || null,
      recovery_action: "restart_runtime",
      recovery_suggestion:
        "The Python runtime exited unexpectedly. Check /api/runtime/logs and retry.",
    };
  }

  const caps = probeHostCapabilities(root);
  const health = {
    ...defaultHealth(),
    ...((raw.health as RuntimeHealth) || {}),
  };
  if (!caps.can_spawn_runtime) {
    health.runtime = caps.vercel || caps.ecc_disable_python ? "disabled" : "failed";
  }

  // Activity overlay for current stage/task
  const activity = readJsonFile(
    path.join(root, "automation/learning/state/live_activity.json")
  );

  return {
    status,
    session_id: (raw.session_id as string) || (activity?.session_id as string) || null,
    correlation_id: (raw.correlation_id as string) || null,
    pid: pid && isPidAlive(pid) ? pid : status === "running" ? pid : pid,
    started_at: startedAt,
    stopped_at: (raw.stopped_at as string) || null,
    current_stage:
      (raw.current_stage as string) ||
      (activity?.stage as string) ||
      null,
    current_task:
      (raw.current_task as string) ||
      (activity?.current_task as string) ||
      (activity?.current_thought as string) ||
      null,
    documents_processed: Number(raw.documents_processed || 0),
    knowledge_candidates: Number(raw.knowledge_candidates || 0),
    uptime_seconds: uptime,
    instruction: (raw.instruction as string) || null,
    last_error: lastError,
    health,
    updated_at: (raw.updated_at as string) || nowIso(),
    host_capabilities: caps,
  };
}

export function writeRuntimeStatus(
  patch: Partial<RuntimeStatus> & Record<string, unknown>,
  root = getRepoRoot()
): RuntimeStatus {
  ensureDirs(root);
  const existing = readJsonFile(statusPath(root)) || {};
  const merged = {
    ...existing,
    ...patch,
    updated_at: nowIso(),
  };
  writeJsonFile(statusPath(root), merged);
  return readRuntimeStatus(root);
}

export function writeFailureLog(
  failure: RuntimeFailure,
  root = getRepoRoot()
): string {
  ensureDirs(root);
  const stamp = new Date().toISOString().replace(/[:.]/g, "").slice(0, 15);
  const file = path.join(
    root,
    LOGS_REL,
    `error_${stamp}_${failure.correlation_id}.json`
  );
  writeJsonFile(file, failure);
  const channel = path.join(root, LOGS_REL, "errors.jsonl");
  fs.appendFileSync(channel, JSON.stringify(failure) + "\n", "utf8");
  return file;
}

export function readRuntimeLogs(opts: {
  channel?: string;
  limit?: number;
  session_id?: string | null;
  correlation_id?: string | null;
  root?: string;
}): { channel: string; entries: Record<string, unknown>[] } {
  const root = opts.root || getRepoRoot();
  ensureDirs(root);
  const limit = opts.limit ?? 100;
  const channel = opts.channel || "all";
  const channels =
    channel === "all"
      ? [
          "system",
          "learning",
          "runtime",
          "errors",
          "publish",
          "review",
          "telemetry",
        ]
      : [channel];

  const entries: Record<string, unknown>[] = [];
  for (const ch of channels) {
    const file = path.join(root, LOGS_REL, `${ch}.jsonl`);
    if (!fs.existsSync(file)) continue;
    const lines = fs.readFileSync(file, "utf8").split("\n").filter(Boolean);
    for (const line of lines) {
      try {
        const row = JSON.parse(line) as Record<string, unknown>;
        if (opts.session_id && row.session_id !== opts.session_id) continue;
        if (opts.correlation_id && row.correlation_id !== opts.correlation_id)
          continue;
        if (!row.channel) row.channel = ch;
        entries.push(row);
      } catch {
        /* skip */
      }
    }
  }
  // also include error JSON files if channel is errors/all
  if (channel === "all" || channel === "errors") {
    const dir = path.join(root, LOGS_REL);
    if (fs.existsSync(dir)) {
      for (const name of fs.readdirSync(dir)) {
        if (!name.startsWith("error_") || !name.endsWith(".json")) continue;
        const row = readJsonFile(path.join(dir, name));
        if (!row) continue;
        if (opts.session_id && row.session_id !== opts.session_id) continue;
        if (
          opts.correlation_id &&
          row.correlation_id !== opts.correlation_id
        )
          continue;
        entries.push({ channel: "errors", ...row });
      }
    }
  }
  entries.sort((a, b) =>
    String(b.timestamp || b.ts || "").localeCompare(
      String(a.timestamp || a.ts || "")
    )
  );
  return { channel, entries: entries.slice(0, limit) };
}

export function readSessionInfo(
  sessionId?: string | null,
  root = getRepoRoot()
): Record<string, unknown> {
  const status = readRuntimeStatus(root);
  const sessionsDir = path.join(
    root,
    "automation/learning/state/sessions"
  );
  if (!sessionId) {
    // current session snapshot
    return {
      session_id: status.session_id,
      correlation_id: status.correlation_id,
      status: status.status,
      started_at: status.started_at,
      current_stage: status.current_stage,
      current_task: status.current_task,
      documents_processed: status.documents_processed,
      knowledge_candidates: status.knowledge_candidates,
      uptime_seconds: status.uptime_seconds,
      last_error: status.last_error,
      health: status.health,
    };
  }
  const file = path.join(sessionsDir, `${sessionId}.jsonl`);
  if (!fs.existsSync(file)) {
    return { error: "session_not_found", session_id: sessionId };
  }
  const lines = fs.readFileSync(file, "utf8").split("\n").filter(Boolean);
  let first: Record<string, unknown> | null = null;
  let last: Record<string, unknown> | null = null;
  try {
    first = JSON.parse(lines[0] || "{}");
    last = JSON.parse(lines[lines.length - 1] || "{}");
  } catch {
    /* ignore */
  }
  return {
    session_id: sessionId,
    events: lines.length,
    started_at: first?.ts ?? null,
    ended_at: last?.ts ?? null,
    last_verb: last?.verb ?? null,
    last_stage: last?.stage ?? null,
    last_status: last?.status ?? null,
    current_task: last?.current_task ?? null,
    correlation_id: status.session_id === sessionId ? status.correlation_id : null,
    runtime_status: status.session_id === sessionId ? status.status : null,
  };
}

/**
 * Start live runtime with exclusive lock + real diagnostics.
 * Root cause paths for 503 are explicit per component.
 */
export async function startLiveRuntime(opts: {
  instruction?: string;
  pace?: number;
}): Promise<StartResult> {
  const root = getRepoRoot();
  ensureDirs(root);
  const correlation_id = newCorrelationId();
  const instruction =
    opts.instruction?.trim() ||
    "Learn Industry Library knowledge — live session";
  const pace = opts.pace ?? 0.7;

  const caps = probeHostCapabilities(root);

  // --- Root cause path 1: host/environment gate ---
  if (!caps.can_spawn_runtime) {
    const component = caps.vercel
      ? "host.vercel"
      : caps.ecc_disable_python
        ? "host.ecc_disable_python"
        : !caps.python_path
          ? "host.python_missing"
          : "host.python_import";
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component,
      exception: "RuntimeUnavailable",
      message: caps.block_reason || "Live runtime unavailable on this host",
      correlation_id,
      recovery_action: "run_on_capable_host",
      recoverable: false,
      recovery_suggestion: caps.vercel
        ? "Deploy or run ECC on a machine with Python (local dev / VM). Vercel cannot host the live learning subprocess."
        : caps.ecc_disable_python
          ? "Unset ECC_DISABLE_PYTHON=1 on this host, or run: python3 -m automation.learning.live_runtime"
          : caps.block_reason ||
            "Install Python 3 and ensure `python3 -m automation.learning.live_runtime` works from the repo root.",
      meta: { host_capabilities: caps },
    };
    writeFailureLog(failure, root);
    writeRuntimeStatus(
      {
        status: "failed",
        correlation_id,
        last_error: failure,
        stopped_at: nowIso(),
        health: {
          ...defaultHealth(),
          runtime: caps.vercel || caps.ecc_disable_python ? "disabled" : "failed",
        },
      },
      root
    );
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: readRuntimeStatus(root),
    };
  }

  // --- Root cause path 2: already running ---
  reclaimStaleLock(root);
  const existing = readRuntimeStatus(root);
  if (
    (existing.status === "running" || existing.status === "starting") &&
    existing.pid &&
    isPidAlive(existing.pid)
  ) {
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: "runtime.lock",
      exception: "AlreadyRunning",
      message: `Runtime already running (pid=${existing.pid}, session=${existing.session_id})`,
      correlation_id,
      session_id: existing.session_id,
      recovery_action: "wait_or_stop_existing_runtime",
      recoverable: false,
      recovery_suggestion:
        "A live session is already active. Wait for it to finish. Refreshing the dashboard does not stop learning.",
    };
    writeFailureLog(failure, root);
    return {
      ok: false,
      status_code: 409,
      message: failure.message,
      correlation_id,
      session_id: existing.session_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: existing,
    };
  }

  const python = caps.python_path!;
  const logDir = path.join(root, LOGS_REL);
  const stdoutLog = path.join(logDir, `spawn_${correlation_id}.stdout.log`);
  const stderrLog = path.join(logDir, `spawn_${correlation_id}.stderr.log`);

  writeRuntimeStatus(
    {
      status: "starting",
      correlation_id,
      started_at: nowIso(),
      stopped_at: null,
      instruction,
      current_stage: "startup",
      current_task: "Spawning live_runtime process",
      documents_processed: 0,
      knowledge_candidates: 0,
      last_error: null,
      health: defaultHealth(),
    },
    root
  );

  let child: ChildProcess;
  let stdoutFd: number;
  let stderrFd: number;
  try {
    stdoutFd = fs.openSync(stdoutLog, "a");
    stderrFd = fs.openSync(stderrLog, "a");
    child = spawn(
      python,
      [
        "-m",
        "automation.learning.live_runtime",
        "--instruction",
        instruction,
        "--pace",
        String(pace),
        "--correlation-id",
        correlation_id,
      ],
      {
        cwd: root,
        env: {
          ...process.env,
          PYTHONUNBUFFERED: "1",
          IDA_CORRELATION_ID: correlation_id,
        },
        detached: true,
        stdio: ["ignore", stdoutFd, stderrFd],
      }
    );
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: "runtime.spawn",
      exception: err.name || "SpawnError",
      message: err.message,
      stack_trace: err.stack,
      correlation_id,
      recovery_action: "check_python_and_permissions",
      recoverable: false,
      recovery_suggestion:
        "Failed to spawn the Python process. Verify python path, execute permissions, and disk space.",
    };
    writeFailureLog(failure, root);
    writeRuntimeStatus(
      {
        status: "failed",
        correlation_id,
        last_error: failure,
        stopped_at: nowIso(),
        health: { ...defaultHealth(), runtime: "failed" },
      },
      root
    );
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: readRuntimeStatus(root),
    };
  }

  // Detach from parent event loop without orphaning logs immediately
  try {
    fs.closeSync(stdoutFd!);
    fs.closeSync(stderrFd!);
  } catch {
    /* ignore */
  }

  const pid = child.pid ?? null;
  if (!pid) {
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: "runtime.spawn",
      exception: "NoPid",
      message: "spawn() returned without a process id",
      correlation_id,
      recovery_action: "retry_start",
      recoverable: true,
      recovery_suggestion: "Spawn produced no PID. Retry once; if it persists check OS process limits.",
    };
    writeFailureLog(failure, root);
    writeRuntimeStatus(
      {
        status: "failed",
        correlation_id,
        last_error: failure,
        stopped_at: nowIso(),
        health: { ...defaultHealth(), runtime: "failed" },
      },
      root
    );
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: readRuntimeStatus(root),
    };
  }

  writeRuntimeStatus(
    {
      status: "starting",
      pid,
      correlation_id,
      current_task: `Process spawned pid=${pid}`,
    },
    root
  );

  // Verify process stays alive briefly (catch immediate import/crash)
  await sleep(600);
  if (!isPidAlive(pid)) {
    const stderr = safeReadTail(stderrLog, 4000);
    const stdout = safeReadTail(stdoutLog, 2000);
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: "runtime.process",
      exception: "EarlyExit",
      message:
        "Live runtime process exited immediately after spawn. " +
        (stderr || stdout || "No stderr captured."),
      stack_trace: stderr || undefined,
      correlation_id,
      recovery_action: "inspect_spawn_logs",
      recoverable: false,
      recovery_suggestion:
        "Open automation/runtime/logs/ for spawn stderr. Typical causes: missing module, bad cwd, permission error.",
      meta: {
        stdout_log: stdoutLog,
        stderr_log: stderrLog,
        stdout_tail: stdout.slice(0, 1000),
        stderr_tail: stderr.slice(0, 2000),
      },
    };
    writeFailureLog(failure, root);
    writeRuntimeStatus(
      {
        status: "failed",
        pid: null,
        correlation_id,
        last_error: failure,
        stopped_at: nowIso(),
        health: { ...defaultHealth(), runtime: "failed" },
      },
      root
    );
    try {
      child.unref();
    } catch {
      /* ignore */
    }
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: readRuntimeStatus(root),
    };
  }

  // Detach so Next.js can finish the request without killing the child
  child.unref();

  const status = writeRuntimeStatus(
    {
      status: "running",
      pid,
      correlation_id,
      started_at: nowIso(),
      current_stage: "startup",
      current_task: "Live runtime process running",
      health: defaultHealth(),
    },
    root
  );

  // system channel
  appendChannelLog(root, "system", {
    timestamp: nowIso(),
    channel: "system",
    level: "INFO",
    module: "runtime-manager",
    message: `Started live runtime pid=${pid}`,
    session_id: null,
    correlation_id,
    duration_ms: null,
    meta: { instruction, pace },
  });

  return {
    ok: true,
    status_code: 200,
    message: "Live learning session started",
    pid,
    correlation_id,
    instruction,
    stream: "/api/live",
    status,
  };
}

function appendChannelLog(
  root: string,
  channel: string,
  row: Record<string, unknown>
): void {
  const file = path.join(root, LOGS_REL, `${channel}.jsonl`);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.appendFileSync(file, JSON.stringify(row) + "\n", "utf8");
}

function safeReadTail(file: string, maxBytes: number): string {
  try {
    if (!fs.existsSync(file)) return "";
    const stat = fs.statSync(file);
    const start = Math.max(0, stat.size - maxBytes);
    const fd = fs.openSync(file, "r");
    const buf = Buffer.alloc(stat.size - start);
    fs.readSync(fd, buf, 0, buf.length, start);
    fs.closeSync(fd);
    return buf.toString("utf8");
  } catch {
    return "";
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}

/** Aggregate health for dashboard /api/runtime/status */
export function computeHealthBundle(root = getRepoRoot()): {
  overall: HealthLevel;
  components: RuntimeHealth;
  details: Record<string, string>;
} {
  const status = readRuntimeStatus(root);
  const components = { ...status.health };
  const details: Record<string, string> = {};

  const caps = status.host_capabilities || probeHostCapabilities(root);
  if (!caps.can_spawn_runtime) {
    components.runtime =
      caps.vercel || caps.ecc_disable_python ? "disabled" : "failed";
    details.runtime = caps.block_reason || "unavailable";
  } else if (status.status === "failed") {
    components.runtime = "failed";
    details.runtime = status.last_error?.message || "failed";
  } else if (status.status === "running" || status.status === "starting") {
    components.runtime = "healthy";
    details.runtime = `status=${status.status} pid=${status.pid}`;
  } else {
    components.runtime = "healthy";
    details.runtime = `status=${status.status}`;
  }

  // Queue dirs
  try {
    const q = path.join(root, "automation/queue");
    if (!fs.existsSync(q)) {
      components.queue = "warning";
      details.queue = "queue directory missing";
    } else {
      components.queue = "healthy";
      details.queue = "queue directories present";
    }
  } catch (e) {
    components.queue = "failed";
    details.queue = e instanceof Error ? e.message : "queue check failed";
  }

  // SSE: passive — presence of live route is assumed healthy unless many failures
  components.sse = "healthy";
  details.sse = "SSE endpoint /api/live (client ref-counted)";

  // Publisher
  components.publisher =
    status.status === "failed" && status.last_error?.component?.includes("publish")
      ? "failed"
      : "healthy";

  const levels = Object.values(components);
  let overall: HealthLevel = "healthy";
  if (levels.includes("failed")) overall = "failed";
  else if (levels.includes("warning")) overall = "warning";
  else if (levels.every((l) => l === "disabled")) overall = "disabled";

  return { overall, components, details };
}
