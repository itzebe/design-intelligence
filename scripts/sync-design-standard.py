#!/usr/bin/env python3
"""Distribute the canonical design standard to the layers that actually persist.

Verified behaviour of this OpenHands deployment (measured, not assumed):

  * Account **memory**  -> the user memory file `~/.openhands/memory/MEMORY.md`, injected into
                           every new conversation, in every project, as the <MEMORY_CONTEXT> block.
                           It is populated FROM DISK: the settings UI has no memory text box (only
                           a `load_memory` toggle), and the public settings API accepts a
                           `memory_context` field with HTTP 200 but SILENTLY IGNORES it. To write
                           it, edit the file with the `file_editor` tool - a MemoryChangeCallback
                           Processor persists `MEMORY.md` edits made that way, while a plain shell
                           write does not. Only the LAST ~100 lines (~3000 chars) of each tier reach
                           the prompt, so the GDI block must sit at the END of MEMORY.md.
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
  python3 scripts/sync-design-standard.py --print-memory    # print the block for MEMORY.md
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
MEMORY_MARKER = "Global Design Intelligence (GDI)"


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


MEMORY_FILE = pathlib.Path.home() / ".openhands" / "memory" / "MEMORY.md"


def memory_block() -> str:
    """Extract the fenced markdown block from ACCOUNT_MEMORY.md."""
    text = (REPO_ROOT / "ACCOUNT_MEMORY.md").read_text(encoding="utf-8")
    start = text.find("```markdown")
    end = text.rfind("```")
    if start == -1 or end <= start:
        sys.exit("error: could not find the fenced markdown block in ACCOUNT_MEMORY.md")
    return text[start + len("```markdown"):end].strip()


def check_account_memory() -> bool:
    """Report whether the standard is present in the user memory file; print the block if not."""
    if not MEMORY_FILE.exists():
        print(f"[memory] {MEMORY_FILE} does not exist - the block has not been installed")
        return False
    mem = MEMORY_FILE.read_text(encoding="utf-8")
    present = MEMORY_MARKER in mem
    tail_ok = MEMORY_MARKER in mem[-4000:]
    print(
        f"[memory] {MEMORY_FILE} length={len(mem)} standard_present={present} "
        f"within_truncation_window={tail_ok}"
    )
    if not present:
        print(
            "[memory] ACTION REQUIRED: append the block from ACCOUNT_MEMORY.md to the END of "
            f"{MEMORY_FILE}, then touch the file with the `file_editor` tool so the change is "
            "persisted to your account record. (The settings API cannot persist memory text.)"
        )
    elif not tail_ok:
        print(
            "[memory] WARNING: the standard is present but sits too high in the file - only the "
            "last ~3000 chars are injected. Move the block to the very end."
        )
    return present and tail_ok


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
    print(memory_block())
    return 0


def install_memory_block() -> int:
    """Append the block to the END of the user memory file (idempotent)."""
    block = memory_block()
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = MEMORY_FILE.read_text(encoding="utf-8") if MEMORY_FILE.exists() else ""
    if MEMORY_MARKER in existing:
        print(f"[memory] block already present in {MEMORY_FILE}; nothing to do")
        return 0
    updated = existing.rstrip() + "\n\n" + block + "\n"
    MEMORY_FILE.write_text(updated, encoding="utf-8")
    print(
        f"[memory] appended block to {MEMORY_FILE} (now {len(updated)} chars).\n"
        "         IMPORTANT: touch the file with the `file_editor` tool in an OpenHands "
        "conversation so the change is persisted to your account record - a plain shell write "
        "is not detected."
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; change nothing")
    ap.add_argument("--print-memory", action="store_true", help="print the account-memory block")
    ap.add_argument("--install-memory", action="store_true", help="append the block to the user memory file")
    args = ap.parse_args()

    if args.print_memory:
        return print_memory_block()
    if args.install_memory:
        return install_memory_block()

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
