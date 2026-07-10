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

/**
 * Detect serverless / read-only hosts (Vercel, Lambda, /var/task).
 * These cannot mkdir under the deployment root or run detached Python.
 */
export function isServerlessHost(root?: string): boolean {
  const r = root || getRepoRoot();
  return Boolean(
    process.env.VERCEL ||
      process.env.VERCEL_ENV ||
      process.env.AWS_LAMBDA_FUNCTION_NAME ||
      process.env.LAMBDA_TASK_ROOT ||
      process.env.ECS_AGENT_URI ||
      r === "/var/task" ||
      r.startsWith("/var/task/") ||
      process.cwd() === "/var/task"
  );
}

export type DirEnsureResult =
  | { ok: true; stateDir: string; logsDir: string }
  | { ok: false; error: string; code?: string; path?: string };

/**
 * Create runtime state/log dirs. Never throws — returns structured result.
 * On Vercel/read-only FS this fails with a clear path error instead of crashing start.
 */
export function ensureDirs(root: string): DirEnsureResult {
  const stateDir = path.join(root, STATE_REL);
  const logsDir = path.join(root, LOGS_REL);
  try {
    fs.mkdirSync(stateDir, { recursive: true });
    fs.mkdirSync(logsDir, { recursive: true });
    // Prove write works (mkdir alone can succeed on some FUSE mounts that still fail writes)
    const probe = path.join(stateDir, `.write_probe_${process.pid}`);
    fs.writeFileSync(probe, "ok", "utf8");
    try {
      fs.unlinkSync(probe);
    } catch {
      /* ignore */
    }
    return { ok: true, stateDir, logsDir };
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    return {
      ok: false,
      error: err.message || String(e),
      code: err.code,
      path: stateDir,
    };
  }
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

function writeJsonFile(file: string, data: unknown): boolean {
  try {
    const dir = path.dirname(file);
    fs.mkdirSync(dir, { recursive: true });
    const tmp = `${file}.tmp.${process.pid}`;
    fs.writeFileSync(tmp, JSON.stringify(data, null, 2) + "\n", "utf8");
    fs.renameSync(tmp, file);
    return true;
  } catch (e) {
    console.error("[runtime-manager] writeJsonFile failed", file, e);
    return false;
  }
}

/** Classify filesystem / serverless failures into a precise component. */
export function classifyFilesystemFailure(
  errMessage: string,
  root: string
): {
  component: string;
  error_code: string;
  recovery_suggestion: string;
} {
  const serverless = isServerlessHost(root);
  const msg = errMessage || "";
  const isFs =
    /ENOENT|EACCES|EPERM|EROFS|read-only|mkdir|open '/i.test(msg) ||
    msg.includes("/var/task");

  if (serverless || msg.includes("/var/task")) {
    return {
      component: "host.vercel",
      error_code: "SERVERLESS_READ_ONLY",
      recovery_suggestion:
        "This deployment is on Vercel/serverless (/var/task is read-only). " +
        "Live learning cannot create automation/runtime/state or spawn Python there. " +
        "Run locally: python3 -m automation.learning.live_runtime " +
        "— or host ECC on a long-running machine with a writable repo checkout.",
    };
  }
  if (isFs) {
    return {
      component: "host.filesystem",
      error_code: "RUNTIME_STATE_NOT_WRITABLE",
      recovery_suggestion:
        "Cannot create automation/runtime/state under the repo root. " +
        "Check disk space, permissions, and that the process cwd is the ida-dataset repo. " +
        "Set IDA_REPO_ROOT to a writable checkout if needed.",
    };
  }
  return {
    component: "runtime.manager",
    error_code: "START_EXCEPTION",
    recovery_suggestion:
      "Unexpected exception in startLiveRuntime. Check /api/runtime/debug and server logs.",
  };
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

/** Cache host probe briefly — status polling must not re-spawn python every few seconds. */
let _capsCache: { at: number; root: string; value: HostCapabilities } | null =
  null;
const CAPS_TTL_MS = 10_000;

export function probeHostCapabilities(
  root = getRepoRoot(),
  opts: { force?: boolean } = {}
): HostCapabilities {
  try {
    if (
      !opts.force &&
      _capsCache &&
      _capsCache.root === root &&
      Date.now() - _capsCache.at < CAPS_TTL_MS
    ) {
      return _capsCache.value;
    }

    const vercel =
      Boolean(process.env.VERCEL) ||
      Boolean(process.env.VERCEL_ENV) ||
      isServerlessHost(root);
    const eccDisable = process.env.ECC_DISABLE_PYTHON === "1";
    const py = resolvePython(root);
    let block: string | null = null;
    if (vercel) {
      block =
        "Host is Vercel/serverless (deployment root is read-only, e.g. /var/task). " +
        "Detached Python live runtime is not supported. " +
        "Run live learning on a local or long-running host with a writable checkout.";
    } else if (eccDisable) {
      block =
        "ECC_DISABLE_PYTHON=1 is set — Python live runtime intentionally disabled on this host.";
    } else if (!py.path) {
      block = py.error;
    }

    // Writable state dir required for lock + status + spawn logs
    if (!block) {
      const dirs = ensureDirs(root);
      if (!dirs.ok) {
        const classified = classifyFilesystemFailure(dirs.error, root);
        block =
          `Cannot write runtime state under ${dirs.path || root}: ${dirs.error} ` +
          `(${classified.error_code})`;
      }
    }

    // Preflight import only when not blocked by env/fs
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

    const value: HostCapabilities = {
      python_available: Boolean(py.path) && !block?.includes("cannot import"),
      python_path: py.path,
      python_version: py.version,
      vercel,
      ecc_disable_python: eccDisable,
      repo_root: root,
      can_spawn_runtime: !block,
      block_reason: block,
    };
    _capsCache = { at: Date.now(), root, value };
    return value;
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    const value: HostCapabilities = {
      python_available: false,
      python_path: null,
      python_version: null,
      vercel: isServerlessHost(root),
      ecc_disable_python: process.env.ECC_DISABLE_PYTHON === "1",
      repo_root: root,
      can_spawn_runtime: false,
      block_reason: `Host capability probe crashed: ${err.message}`,
    };
    _capsCache = { at: Date.now(), root, value };
    return value;
  }
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
  // Soft ensure — never throw from status reads on read-only hosts
  ensureDirs(root);
  try {
    reclaimStaleLock(root);
  } catch {
    /* ignore on read-only */
  }
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
  const dirs = ensureDirs(root);
  // Always log to console so Vercel log drain captures the exact exception
  console.error(
    "[runtime.failure]",
    JSON.stringify({
      timestamp: failure.timestamp,
      component: failure.component,
      exception: failure.exception,
      message: failure.message,
      correlation_id: failure.correlation_id,
      session_id: failure.session_id,
      recovery_action: failure.recovery_action,
      recovery_suggestion: failure.recovery_suggestion,
      stack_trace: failure.stack_trace,
    })
  );
  if (!dirs.ok) {
    return "";
  }
  const stamp = new Date().toISOString().replace(/[:.]/g, "").slice(0, 15);
  const file = path.join(
    root,
    LOGS_REL,
    `error_${stamp}_${failure.correlation_id}.json`
  );
  writeJsonFile(file, failure);
  try {
    const channel = path.join(root, LOGS_REL, "errors.jsonl");
    fs.appendFileSync(channel, JSON.stringify(failure) + "\n", "utf8");
  } catch (e) {
    console.error("[runtime.failure] append channel failed", e);
  }
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
 * Never throws — always returns StartResult with structured failure.
 */
export async function startLiveRuntime(opts: {
  instruction?: string;
  pace?: number;
}): Promise<StartResult> {
  let correlation_id = newCorrelationId();
  try {
    return await startLiveRuntimeInner(opts, correlation_id);
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    const root = getRepoRoot();
    const classified = classifyFilesystemFailure(err.message, root);
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: classified.component,
      exception: err.name || "UnhandledStartError",
      message: err.message || "Unhandled exception during runtime start",
      stack_trace: err.stack,
      correlation_id,
      recovery_action:
        classified.component === "host.vercel"
          ? "run_on_capable_host"
          : "inspect_runtime_debug",
      recoverable: false,
      recovery_suggestion: classified.recovery_suggestion,
      meta: {
        error_code: classified.error_code,
        repo_root: root,
        serverless: isServerlessHost(root),
      },
    };
    try {
      writeFailureLog(failure, root);
      writeRuntimeStatus(
        {
          status: "failed",
          correlation_id,
          last_error: failure,
          stopped_at: nowIso(),
          health: {
            ...defaultHealth(),
            runtime:
              classified.component === "host.vercel" ? "disabled" : "failed",
          },
        },
        root
      );
    } catch {
      /* never throw from failure path */
    }
    console.error("[runtime.manager] start failed", err);
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
    };
  }
}

async function startLiveRuntimeInner(
  opts: { instruction?: string; pace?: number },
  correlation_id: string
): Promise<StartResult> {
  const root = getRepoRoot();
  const instruction =
    opts.instruction?.trim() ||
    "Learn Industry Library knowledge — live session";
  const pace = opts.pace ?? 0.7;

  // --- Root cause path 0: serverless / /var/task (before any mkdir) ---
  if (isServerlessHost(root)) {
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: "host.vercel",
      exception: "ServerlessReadOnly",
      message:
        `Live runtime cannot start on serverless host (repo_root=${root}). ` +
        `Deployment filesystem is read-only — cannot mkdir automation/runtime/state ` +
        `and cannot spawn a long-lived Python process.`,
      correlation_id,
      recovery_action: "run_on_capable_host",
      recoverable: false,
      recovery_suggestion:
        "Run IDA live learning locally or on a VM: " +
        "`python3 -m automation.learning.live_runtime`. " +
        "Vercel/serverless only hosts the dashboard (read-only /var/task).",
      meta: {
        repo_root: root,
        vercel: Boolean(process.env.VERCEL),
        vercel_env: process.env.VERCEL_ENV || null,
        cwd: process.cwd(),
        error_code: "SERVERLESS_READ_ONLY",
      },
    };
    writeFailureLog(failure, root);
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
      status: {
        status: "failed",
        session_id: null,
        correlation_id,
        pid: null,
        started_at: null,
        stopped_at: nowIso(),
        current_stage: null,
        current_task: null,
        documents_processed: 0,
        knowledge_candidates: 0,
        uptime_seconds: 0,
        last_error: failure,
        health: { ...defaultHealth(), runtime: "disabled" },
        host_capabilities: probeHostCapabilities(root, { force: true }),
      },
    };
  }

  // Force fresh host probe on start (includes writable-dir check)
  const caps = probeHostCapabilities(root, { force: true });

  // --- Root cause path 1: host/environment gate ---
  if (!caps.can_spawn_runtime) {
    const fsClassified = caps.block_reason
      ? classifyFilesystemFailure(caps.block_reason, root)
      : null;
    const component = caps.vercel
      ? "host.vercel"
      : caps.ecc_disable_python
        ? "host.ecc_disable_python"
        : !caps.python_path
          ? "host.python_missing"
          : caps.block_reason &&
              /mkdir|ENOENT|EROFS|writable|runtime\/state/i.test(
                caps.block_reason
              )
            ? fsClassified?.component || "host.filesystem"
            : "host.python_import";
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component,
      exception:
        component === "host.vercel"
          ? "ServerlessReadOnly"
          : component === "host.filesystem"
            ? "RuntimeStateNotWritable"
            : "RuntimeUnavailable",
      message: caps.block_reason || "Live runtime unavailable on this host",
      correlation_id,
      recovery_action: "run_on_capable_host",
      recoverable: false,
      recovery_suggestion: caps.vercel
        ? "Deploy or run ECC on a machine with Python (local dev / VM). Vercel cannot host the live learning subprocess or write /var/task/automation/runtime/state."
        : caps.ecc_disable_python
          ? "Unset ECC_DISABLE_PYTHON=1 on this host, or run: python3 -m automation.learning.live_runtime"
          : fsClassified?.recovery_suggestion ||
            caps.block_reason ||
            "Install Python 3 and ensure `python3 -m automation.learning.live_runtime` works from the repo root.",
      meta: {
        host_capabilities: caps,
        error_code: fsClassified?.error_code || component,
      },
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
          runtime:
            caps.vercel || caps.ecc_disable_python ? "disabled" : "failed",
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

  // Writable dirs already verified by probe — ensure again for spawn logs
  const dirs = ensureDirs(root);
  if (!dirs.ok) {
    const classified = classifyFilesystemFailure(dirs.error, root);
    const failure: RuntimeFailure = {
      timestamp: nowIso(),
      component: classified.component,
      exception: dirs.code || "DirEnsureFailed",
      message: `Cannot create runtime directories: ${dirs.error}`,
      correlation_id,
      recovery_action: "run_on_capable_host",
      recoverable: false,
      recovery_suggestion: classified.recovery_suggestion,
      meta: { path: dirs.path, code: dirs.code, repo_root: root },
    };
    writeFailureLog(failure, root);
    return {
      ok: false,
      status_code: 503,
      message: failure.message,
      correlation_id,
      failure,
      recovery_suggestion: failure.recovery_suggestion,
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

/**
 * Full diagnostic snapshot for GET /api/runtime/debug
 */
export function collectRuntimeDebug(root = getRepoRoot()): Record<string, unknown> {
  let runtimeState: RuntimeStatus | Record<string, unknown> = {};
  let health: ReturnType<typeof computeHealthBundle> | null = null;
  let lastException: RuntimeFailure | null = null;
  let schedulerState: Record<string, unknown> | null = null;
  let connectorStatus: Record<string, unknown> = {};
  let lock: Record<string, unknown> | null = null;
  let activity: Record<string, unknown> | null = null;
  let recentErrors: Record<string, unknown>[] = [];

  try {
    runtimeState = readRuntimeStatus(root);
    lastException = (runtimeState as RuntimeStatus).last_error;
  } catch (e) {
    runtimeState = {
      status: "failed",
      error: e instanceof Error ? e.message : String(e),
    };
  }
  try {
    health = computeHealthBundle(root);
  } catch (e) {
    health = null;
  }
  try {
    lock = readJsonFile(lockPath(root));
  } catch {
    lock = null;
  }
  try {
    activity = readJsonFile(
      path.join(root, "automation/learning/state/live_activity.json")
    );
  } catch {
    activity = null;
  }
  try {
    const schedPath = path.join(
      root,
      "automation/scheduler/state/scheduler_state.json"
    );
    const alt = path.join(root, "automation/scheduler/state/state.json");
    schedulerState =
      readJsonFile(schedPath) ||
      readJsonFile(alt) ||
      { note: "No scheduler state file present" };
  } catch (e) {
    schedulerState = {
      error: e instanceof Error ? e.message : String(e),
    };
  }
  try {
    const healthCsv = path.join(
      root,
      "automation/connectors/cache/connector_health.csv"
    );
    connectorStatus = {
      health_csv_exists: fs.existsSync(healthCsv),
      cache_dir: path.join(root, "automation/connectors/cache"),
    };
    // list recent connector events if present
    const eventsPath = path.join(
      root,
      "automation/connectors/cache/connector_events.jsonl"
    );
    if (fs.existsSync(eventsPath)) {
      const lines = fs
        .readFileSync(eventsPath, "utf8")
        .split("\n")
        .filter(Boolean)
        .slice(-5);
      connectorStatus.recent_events = lines.map((l) => {
        try {
          return JSON.parse(l);
        } catch {
          return l;
        }
      });
    }
  } catch (e) {
    connectorStatus = {
      error: e instanceof Error ? e.message : String(e),
    };
  }
  try {
    recentErrors = readRuntimeLogs({
      channel: "errors",
      limit: 5,
      root,
    }).entries;
  } catch {
    recentErrors = [];
  }

  const status = runtimeState as RuntimeStatus;
  const workerPid = status.pid ?? null;
  const workerAlive = isPidAlive(workerPid);

  return {
    timestamp: nowIso(),
    runtime_state: runtimeState,
    scheduler_state: schedulerState,
    active_session: {
      session_id: status.session_id ?? null,
      correlation_id: status.correlation_id ?? null,
      status: status.status ?? null,
      stage: status.current_stage ?? null,
      task: status.current_task ?? null,
      started_at: status.started_at ?? null,
      instruction: status.instruction ?? null,
    },
    worker_status: {
      pid: workerPid,
      alive: workerAlive,
      status: workerAlive
        ? "running"
        : workerPid
          ? "dead"
          : "none",
    },
    lock,
    activity,
    connector_status: connectorStatus,
    health,
    last_exception: lastException,
    recent_errors: recentErrors,
    host_capabilities: probeHostCapabilities(root),
    repo_root: root,
    node: {
      pid: process.pid,
      node_env: process.env.NODE_ENV ?? null,
      vercel: Boolean(process.env.VERCEL),
      ecc_disable_python: process.env.ECC_DISABLE_PYTHON === "1",
      platform: process.platform,
    },
  };
}
