/**
 * Defensive HTTP JSON parsing for the dashboard.
 * Never call response.json() blindly — empty/HTML bodies must surface as diagnostics.
 */

export type RawHttpDiagnostic = {
  http_status: number;
  status_text: string;
  headers: Record<string, string>;
  body: string;
  content_type: string | null;
  url: string;
  parse_error?: string;
};

export type SafeJsonResult<T = Record<string, unknown>> = {
  /** True when body parsed as JSON object/array */
  parsed: boolean;
  /** HTTP ok (2xx) */
  http_ok: boolean;
  http_status: number;
  data: T | null;
  raw: RawHttpDiagnostic;
  /** Normalized success flag from contract when present */
  success?: boolean;
  reason?: string;
};

function headersToObject(headers: Headers): Record<string, string> {
  const out: Record<string, string> = {};
  headers.forEach((value, key) => {
    out[key] = value;
  });
  return out;
}

/**
 * Read Response as text, then JSON.parse safely.
 * Never throws "Unexpected end of JSON input".
 */
export async function safeParseJsonResponse<T = Record<string, unknown>>(
  res: Response
): Promise<SafeJsonResult<T>> {
  let body = "";
  try {
    body = await res.text();
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    return {
      parsed: false,
      http_ok: res.ok,
      http_status: res.status,
      data: null,
      reason: `Failed to read response body: ${msg}`,
      raw: {
        http_status: res.status,
        status_text: res.statusText,
        headers: headersToObject(res.headers),
        body: "",
        content_type: res.headers.get("content-type"),
        url: res.url,
        parse_error: msg,
      },
    };
  }

  const raw: RawHttpDiagnostic = {
    http_status: res.status,
    status_text: res.statusText,
    headers: headersToObject(res.headers),
    body,
    content_type: res.headers.get("content-type"),
    url: res.url,
  };

  if (!body || !body.trim()) {
    return {
      parsed: false,
      http_ok: res.ok,
      http_status: res.status,
      data: null,
      reason: `Empty response body (HTTP ${res.status})`,
      raw: {
        ...raw,
        parse_error: "Empty body — cannot JSON.parse",
      },
    };
  }

  try {
    const data = JSON.parse(body) as T;
    const rec = data as Record<string, unknown>;
    const success =
      typeof rec?.success === "boolean"
        ? (rec.success as boolean)
        : typeof rec?.ok === "boolean"
          ? (rec.ok as boolean)
          : undefined;
    const reason =
      typeof rec?.reason === "string"
        ? rec.reason
        : typeof rec?.message === "string"
          ? rec.message
          : typeof rec?.error === "string"
            ? rec.error
            : undefined;
    return {
      parsed: true,
      http_ok: res.ok,
      http_status: res.status,
      data,
      success,
      reason,
      raw,
    };
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    return {
      parsed: false,
      http_ok: res.ok,
      http_status: res.status,
      data: null,
      reason: `Invalid JSON: ${msg}`,
      raw: {
        ...raw,
        parse_error: msg,
      },
    };
  }
}

export async function safeFetchJson<T = Record<string, unknown>>(
  input: RequestInfo | URL,
  init?: RequestInit
): Promise<SafeJsonResult<T>> {
  try {
    const res = await fetch(input, init);
    return safeParseJsonResponse<T>(res);
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    return {
      parsed: false,
      http_ok: false,
      http_status: 0,
      data: null,
      reason: `Network error: ${msg}`,
      raw: {
        http_status: 0,
        status_text: "NETWORK_ERROR",
        headers: {},
        body: "",
        content_type: null,
        url: String(input),
        parse_error: msg,
      },
    };
  }
}
