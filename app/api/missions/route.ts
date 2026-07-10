import { NextRequest, NextResponse } from "next/server";
import {
  listContracts,
  listMissions,
  listLearningReports,
  enrichLearningReports,
  createMissionRecord,
  runSchedulerCli,
} from "@/lib/learning";
import {
  dispatchLearningWorkflow,
  isGithubConfigured,
} from "@/lib/github-actions";
import { getSessionsDashboard } from "@/lib/sessions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

function safeJsonBody(req: NextRequest): Promise<Record<string, unknown>> {
  return req.json().catch(() => ({}));
}

export async function GET() {
  try {
    const sessions = getSessionsDashboard();
    return NextResponse.json({
      ok: true,
      missions: listMissions(),
      contracts: listContracts(),
      reports: enrichLearningReports(listLearningReports()),
      sessions: sessions.sessions || [],
      history: sessions.history || null,
      github_actions: null,
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      {
        ok: false,
        error: "Unable to load missions right now.",
        detail: err.message,
        missions: [],
        contracts: [],
        reports: [],
        sessions: [],
      },
      { status: 500 }
    );
  }
}

/**
 * POST /api/missions — queue a production mission.
 *
 * Production path (preferred): write mission record + dispatch learn.yml.
 * Optional local path: Python scheduler CLI when available.
 * Never returns raw Python/JSON parse errors to the client.
 */
export async function POST(req: NextRequest) {
  try {
    const body = (await safeJsonBody(req)) as {
      action?: string;
      text?: string;
      mission?: string;
      dry_run?: boolean;
    };
    const text = String(body.text || body.mission || "").trim();
    if (!text) {
      return NextResponse.json(
        {
          ok: false,
          error: "Please enter a mission instruction before dispatching.",
          code: "EMPTY_INSTRUCTION",
        },
        { status: 400 }
      );
    }
    if (text.length < 8) {
      return NextResponse.json(
        {
          ok: false,
          error: "Mission instruction is too short. Describe what to produce.",
          code: "INSTRUCTION_TOO_SHORT",
        },
        { status: 400 }
      );
    }

    // Prefer Python scheduler when available (local/dev)
    let mission: Record<string, unknown> | null = null;
    let channel = "github_actions";
    const cli = runSchedulerCli(["mission", text]);
    if (cli.ok && cli.data && typeof cli.data === "object") {
      const data = cli.data as Record<string, unknown>;
      const nested = (data.mission || data.result || data) as Record<
        string,
        unknown
      >;
      if (nested && (nested.mission_id || (data as { mission?: { mission_id?: string } }).mission)) {
        mission =
          (data.mission as Record<string, unknown>) ||
          nested;
        channel = "scheduler_cli";
      }
    }

    // Always have a durable mission record for the UI
    if (!mission || !mission.mission_id) {
      mission = createMissionRecord(text, {
        requester: "factory-ui",
        status: "Queued",
      });
      channel = "github_actions";
    }

    // Dispatch autonomous production via GitHub Actions when configured
    let dispatch: Awaited<ReturnType<typeof dispatchLearningWorkflow>> | null =
      null;
    if (isGithubConfigured()) {
      dispatch = await dispatchLearningWorkflow({
        mission: text,
        environment: "production",
        // production dispatch is real by default for mission queue
        dry_run: body.dry_run === true,
        trigger: "mission",
        commit_session: true,
      });
      if (!dispatch.ok) {
        // Mission is still queued on disk; surface friendly failure
        return NextResponse.json(
          {
            ok: false,
            code: dispatch.error_code || "DISPATCH_FAILED",
            error:
              "Mission was saved but could not start production right now. It remains queued for the next autonomous run.",
            reason: dispatch.message,
            recovery: dispatch.recovery_suggestion,
            mission,
            channel,
            missions: listMissions(),
          },
          { status: 422 }
        );
      }
    } else if (channel !== "scheduler_cli") {
      // No GHA and no CLI — still queue for scheduled learn.yml when secrets appear
      return NextResponse.json({
        ok: true,
        queued: true,
        code: "MISSION_QUEUED_OFFLINE",
        message:
          "Mission queued for autonomous production. Connect GitHub Actions to start runs immediately.",
        mission,
        channel: "local_queue",
        missions: listMissions(),
      });
    }

    return NextResponse.json({
      ok: true,
      queued: true,
      message:
        channel === "scheduler_cli"
          ? "Mission created and queued for autonomous production."
          : "Mission queued — production will run through GitHub Actions.",
      mission,
      channel,
      dispatch: dispatch
        ? {
            ok: dispatch.ok,
            workflow: dispatch.workflow,
            repository: dispatch.repository,
          }
        : null,
      missions: listMissions(),
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    // Never leak SyntaxError / Unexpected token / stack to the UI
    const friendly =
      /json|token|syntax|unexpected/i.test(err.message)
        ? "Something went wrong while processing the mission. Please try again."
        : "Unable to dispatch the mission right now. Please try again shortly.";
    return NextResponse.json(
      {
        ok: false,
        code: "MISSION_DISPATCH_ERROR",
        error: friendly,
      },
      { status: 500 }
    );
  }
}
