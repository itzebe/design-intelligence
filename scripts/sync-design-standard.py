#!/usr/bin/env python3
"""Distribute the canonical design standard to the layers that actually persist.

Verified behaviour of this OpenHands deployment (measured, not assumed):

  * Account **memory**  -> injected into every new conversation, in every project. The public
                           settings API does NOT persist `memory_context` (it answers HTTP 200 and
                           ignores the field), so this layer is a MANUAL paste in the settings UI.
                           This script prints the exact block to paste and checks whether it is
                           already present.
  * Account **skill**   -> stored durably via the settings API, but a *custom* account skill is NOT
                           auto-injected into new conversations here. Kept as a best-effort layer.
  * Project `AGENTS.md` -> injected into new conversations in that project. This is the per-project
                           enforcement layer (copy `templates/AGENTS.md` into each repo).
  * Project skill file  -> `.agents/skills/<name>.md` (flat) is injected; the directory form
                           `.agents/skills/<name>/SKILL.md` is discovered but not injected.

No credentials are stored in this repository. The script reads from the environment:

  OPENHANDS_API_KEY   required for the cloud checks/writes
  OPENHANDS_HOST      optional; defaults to https://app.all-hands.dev
  SESSION_API_KEY     optional; enables the local agent-server layer

Usage:
  python3 scripts/sync-design-standard.py                   # check + push what it can
  python3 scripts/sync-design-standard.py --check           # report only; change nothing
  python3 scripts/sync-design-standard.py --print-memory    # print the block to paste into Memory
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CONSTITUTION = REPO_ROOT / "DESIGN_CONSTITUTION.md"
SKILL_NAME = "global-design-intelligence"

CLOUD_HOST = os.environ.get("OPENHANDS_HOST", "https://app.all-hands.dev").rstrip("/")
LOCAL_HOST = "http://localhost:60000"

# A short, stable phrase that should appear in account memory once the block is pasted.
MEMORY_MARKER = "Global Design Intelligence (applies to ALL UI work"


def read_constitution() -> str:
    if not CONSTITUTION.exists():
        sys.exit(f"error: {CONSTITUTION} not found")
    return CONSTITUTION.read_text(encoding="utf-8")


def request(method: str, url: str, headers: dict, body: dict | None = None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            return resp.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:400]}
    except Exception as e:  # noqa: BLE001
        return 0, {"error": str(e)}


def skill_payload(content: str, description: str) -> dict:
    return {
        "name": SKILL_NAME,
        "content": content,
        "version": "1.0.0",
        "description": description,
        "disable_model_invocation": False,
        "is_agentskills_format": False,
        "trigger": None,
    }


DESCRIPTION = (
    "Standing design standard that applies to EVERY user interface you produce, modify, or review, "
    "on any project, in every conversation. Use for any web or app UI work - building, redesigning, "
    "styling, or reviewing pages, components, dashboards, landing pages, or design systems."
)


def check_account_memory() -> bool:
    """Report whether the standard is present in account memory; print the block if not."""
    key = os.environ.get("OPENHANDS_API_KEY")
    if not key:
        print("[memory] OPENHANDS_API_KEY not set - cannot check account memory")
        return False
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    status, settings = request("GET", f"{CLOUD_HOST}/api/v1/settings", headers)
    if status != 200:
        print(f"[memory] GET settings failed: HTTP {status} {settings}")
        return False
    mem = settings.get("memory_context") or ""
    present = MEMORY_MARKER in mem
    print(
        f"[memory] account memory length={len(mem)} standard_present={present} "
        f"(enable_memory_context={settings.get('enable_memory_context')})"
    )
    if not present:
        print(
            "[memory] ACTION REQUIRED: paste the block from ACCOUNT_MEMORY.md into the OpenHands "
            "settings UI (Memory). The API will not persist it for you."
        )
    return present


def sync_account_skill(content: str, check: bool) -> bool:
    """Store the standard as an account skill (best-effort: not auto-injected in this deployment)."""
    key = os.environ.get("OPENHANDS_API_KEY")
    if not key:
        print("[skill] OPENHANDS_API_KEY not set - skipping account skill layer")
        return False
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    status, settings = request("GET", f"{CLOUD_HOST}/api/v1/settings", headers)
    if status != 200:
        print(f"[skill] GET settings failed: HTTP {status} {settings}")
        return False
    ac = (settings.get("agent_settings") or {}).get("agent_context") or {}
    have = {s.get("name"): s for s in (ac.get("skills") or [])}
    same = have.get(SKILL_NAME, {}).get("content") == content
    print(f"[skill] present={SKILL_NAME in have} content_matches={same}")
    if check:
        return True
    others = [s for s in (ac.get("skills") or []) if s.get("name") != SKILL_NAME]
    payload = {
        "agent_settings_diff": {
            "agent_context": {
                "skills": others + [skill_payload(content, DESCRIPTION)],
                "load_user_skills": True,
                "load_project_skills": True,
            }
        }
    }
    status, out = request("POST", f"{CLOUD_HOST}/api/v1/settings", headers, payload)
    print(f"[skill] POST settings -> HTTP {status} {json.dumps(out)[:200]}")
    return status in (200, 201)


def sync_local(content: str, check: bool) -> bool:
    key = os.environ.get("SESSION_API_KEY")
    if not key:
        print("[local] SESSION_API_KEY not set - skipping local agent-server layer")
        return False
    headers = {"X-Session-API-Key": key, "Content-Type": "application/json"}
    status, settings = request("GET", f"{LOCAL_HOST}/api/settings", headers)
    if status != 200:
        print(f"[local] GET settings failed: HTTP {status}")
        return False
    ac = (settings.get("agent_settings") or {}).get("agent_context") or {}
    print(
        f"[local] skills={len(ac.get('skills') or [])} "
        f"load_user_skills={ac.get('load_user_skills')} load_project_skills={ac.get('load_project_skills')}"
    )
    if check:
        return True
    others = [s for s in (ac.get("skills") or []) if s.get("name") != SKILL_NAME]
    payload = {
        "agent_settings_diff": {
            "agent_context": {
                "skills": others + [skill_payload(content, DESCRIPTION)],
                "load_user_skills": True,
                "load_project_skills": True,
            }
        }
    }
    status, out = request("PATCH", f"{LOCAL_HOST}/api/settings", headers, payload)
    print(f"[local] PATCH settings -> HTTP {status} {json.dumps(out)[:200]}")
    return status in (200, 201)


def print_memory_block() -> int:
    block = REPO_ROOT / "ACCOUNT_MEMORY.md"
    if not block.exists():
        sys.exit(f"error: {block} not found")
    text = block.read_text(encoding="utf-8")
    start = text.find("```markdown")
    end = text.rfind("```")
    if start == -1 or end <= start:
        sys.exit("error: could not find the fenced markdown block in ACCOUNT_MEMORY.md")
    print(text[start + len("```markdown"): end].strip())
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; change nothing")
    ap.add_argument("--print-memory", action="store_true", help="print the account-memory block")
    args = ap.parse_args()

    if args.print_memory:
        return print_memory_block()

    content = read_constitution()
    print(f"constitution: {len(content)} chars from {CONSTITUTION}")
    mem_ok = check_account_memory()
    skill_ok = sync_account_skill(content, args.check)
    local_ok = sync_local(content, args.check)
    print(
        "done: account_memory=%s account_skill=%s local=%s"
        % (
            "present" if mem_ok else "MISSING (manual paste required)",
            "ok" if skill_ok else "skipped/failed",
            "ok" if local_ok else "skipped/failed",
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
