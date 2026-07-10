/**
 * Standard runtime API response contract.
 *
 * Success:
 *   { success: true, status, session_id, data }
 * Failure:
 *   { success: false, status, component, reason, error_code, correlation_id, session_id }
 *
 * Every handler MUST use these helpers so clients never receive empty/HTML/undefined bodies.
 */

import { NextResponse } from "next/server";
import { randomBytes } from "crypto";

export type ApiSuccessBody<T = Record<string, unknown>> = {
  success: true;
  status: string;
  session_id: string | null;
  correlation_id?: string | null;
  data: T;
  // backward-compatible aliases
  ok: true;
  message?: string;
};

export type ApiFailureBody = {
  success: false;
  status: "failed" | string;
  component: string;
  reason: string;
  error_code: string;
  correlation_id: string;
  session_id: string | null;
  recovery_suggestion?: string;
  stack_trace?: string | null;
  // backward-compatible aliases
  ok: false;
  message: string;
  error: string;
  failure?: {
    timestamp: string;
    component: string;
    exception: string;
    message: string;
    stack_trace?: string | null;
    correlation_id: string;
    session_id: string | null;
    recovery_action?: string;
    recovery_suggestion?: string;
    error_code: string;
  };
  data?: Record<string, unknown> | null;
};

export type ApiEnvelope<T = Record<string, unknown>> =
  | ApiSuccessBody<T>
  | ApiFailureBody;

function nowIso(): string {
  return new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
}

export function newCorrelationId(): string {
  return `CORR-${randomBytes(6).toString("hex").toUpperCase()}`;
}

export function isDev(): boolean {
  return (
    process.env.NODE_ENV === "development" ||
    process.env.IDA_EXPOSE_STACK === "1"
  );
}

/**
 * Always produce a NextResponse with application/json and a non-empty body.
 */
export function jsonSuccess<T extends Record<string, unknown>>(
  opts: {
    status?: string;
    session_id?: string | null;
    correlation_id?: string | null;
    data?: T;
    message?: string;
    httpStatus?: number;
  } = {}
): NextResponse {
  const body: ApiSuccessBody<T> = {
    success: true,
    ok: true,
    status: opts.status ?? "ok",
    session_id: opts.session_id ?? null,
    correlation_id: opts.correlation_id ?? null,
    data: (opts.data ?? ({} as T)) as T,
    message: opts.message,
  };
  return NextResponse.json(body, {
    status: opts.httpStatus ?? 200,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

export function jsonFailure(opts: {
  component: string;
  reason: string;
  error_code: string;
  correlation_id?: string | null;
  session_id?: string | null;
  recovery_suggestion?: string;
  stack_trace?: string | null;
  status?: string;
  httpStatus?: number;
  data?: Record<string, unknown> | null;
  exception?: string;
  recovery_action?: string;
}): NextResponse {
  const correlation_id = opts.correlation_id || newCorrelationId();
  const reason = opts.reason || "Unknown failure";
  const stack =
    opts.stack_trace && isDev()
      ? opts.stack_trace
      : opts.stack_trace
        ? "[redacted outside development — set IDA_EXPOSE_STACK=1 to show]"
        : null;

  const failure = {
    timestamp: nowIso(),
    component: opts.component || "api",
    exception: opts.exception || opts.error_code || "Error",
    message: reason,
    stack_trace: isDev() ? opts.stack_trace ?? null : stack,
    correlation_id,
    session_id: opts.session_id ?? null,
    recovery_action: opts.recovery_action,
    recovery_suggestion: opts.recovery_suggestion,
    error_code: opts.error_code || "UNKNOWN",
  };

  const body: ApiFailureBody = {
    success: false,
    ok: false,
    status: opts.status ?? "failed",
    component: failure.component,
    reason,
    error_code: failure.error_code,
    correlation_id,
    session_id: opts.session_id ?? null,
    recovery_suggestion: opts.recovery_suggestion,
    stack_trace: isDev() ? opts.stack_trace ?? null : null,
    message: reason,
    error: reason,
    failure,
    data: opts.data ?? null,
  };

  // Absolute guarantee: never empty
  const payload = JSON.stringify(body);
  return new NextResponse(payload, {
    status: opts.httpStatus ?? 500,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

/**
 * Wrap an API handler so uncaught exceptions still return valid JSON.
 */
export async function withApiJson(
  component: string,
  fn: () => Promise<NextResponse> | NextResponse
): Promise<NextResponse> {
  try {
    const res = await fn();
    // Guard against accidental empty responses
    if (!res) {
      return jsonFailure({
        component,
        reason: "Handler returned empty response",
        error_code: "EMPTY_RESPONSE",
        httpStatus: 500,
      });
    }

    let text = "";
    try {
      text = await res.text();
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component,
        reason: `Failed to read handler body: ${err.message}`,
        error_code: "BODY_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }

    if (!text || !text.trim()) {
      return jsonFailure({
        component,
        reason: "Handler produced empty body",
        error_code: "EMPTY_BODY",
        httpStatus: res.status || 500,
      });
    }

    try {
      JSON.parse(text);
    } catch {
      return jsonFailure({
        component,
        reason: "Handler produced non-JSON body",
        error_code: "NON_JSON_BODY",
        httpStatus: 500,
        data: { raw_preview: text.slice(0, 500) },
      });
    }

    // Re-emit validated JSON text — never empty, never non-JSON
    return new NextResponse(text, {
      status: res.status,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store",
        "X-Content-Type-Options": "nosniff",
      },
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    console.error(`[${component}] uncaught`, err);
    return jsonFailure({
      component,
      reason: err.message || "Unhandled API exception",
      error_code: "UNHANDLED_EXCEPTION",
      exception: err.name || "Error",
      stack_trace: err.stack,
      recovery_suggestion:
        "Inspect server logs and GET /api/sessions for the latest session diagnostics.",
      recovery_action: "inspect_runtime_debug",
      httpStatus: 500,
    });
  }
}
