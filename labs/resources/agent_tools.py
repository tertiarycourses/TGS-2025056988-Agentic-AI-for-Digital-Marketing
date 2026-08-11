#!/usr/bin/env python3
"""Northstar tool-using agent with approval-controlled synthetic draft creation."""

import argparse
import asyncio
import hashlib
import inspect
import json
import os
import tempfile
from pathlib import Path
from typing import Annotated, Any

from agent_framework import Agent, Message, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from pydantic import Field

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda: None


BASE = Path(__file__).resolve().parent
REQUESTS_FILE = BASE / "northstar-requests.json"
DRAFTS_FILE = Path.cwd() / ".northstar-drafts.json"
ALLOWED_PRIORITIES = {"Low", "Normal", "High", "Critical"}
MAX_APPROVAL_ROUNDS = 3
MAX_APPROVAL_REQUESTS = 3


def _requests():
    return json.loads(REQUESTS_FILE.read_text(encoding="utf-8"))


@tool(approval_mode="never_require", max_invocations=2, max_invocation_exceptions=1)
def get_request(
    record_id: Annotated[str, Field(description="Synthetic Northstar request ID in the form NS-1234")],
) -> dict:
    """Read one synthetic Northstar support request. Use only for status or details."""
    record = next((item for item in _requests() if item["record_id"].upper() == record_id.upper()), None)
    return {"status": "found", "record": record} if record else {"status": "not_found", "record_id": record_id}


@tool(approval_mode="always_require", max_invocations=1, max_invocation_exceptions=1)
def create_escalation_draft(
    record_id: Annotated[str, Field(description="Synthetic Northstar request ID in the form NS-1234")],
    priority: Annotated[str, Field(description="One of Low, Normal, High, Critical")],
    reason: Annotated[str, Field(description="Concise evidence-based reason for the proposed escalation")],
) -> dict:
    """Prepare a synthetic escalation draft after a person approves the visible fields. Never submits a live change."""
    return _create_escalation_draft(record_id, priority, reason, DRAFTS_FILE)


def _create_escalation_draft(record_id: str, priority: str, reason: str, store_path: Path) -> dict:
    record = next((item for item in _requests() if item["record_id"].upper() == record_id.upper()), None)
    if not record:
        return {"status": "not_found", "record_id": record_id}
    normalized = next((item for item in ALLOWED_PRIORITIES if item.lower() == priority.lower()), None)
    if not normalized:
        return {"status": "invalid_priority", "allowed": sorted(ALLOWED_PRIORITIES)}
    key = hashlib.sha256(f"{record_id.upper()}|{normalized}|{reason.strip().lower()}".encode()).hexdigest()[:16]
    drafts = json.loads(store_path.read_text(encoding="utf-8")) if store_path.exists() else []
    existing = next((item for item in drafts if item["idempotency_key"] == key), None)
    if existing:
        return {"status": "already_exists", "draft_id": existing["draft_id"], "idempotency_key": key}
    draft = {
        "draft_id": f"NS-DRAFT-{len(drafts) + 1:04d}",
        "record_id": record_id.upper(),
        "priority": normalized,
        "reason": reason.strip(),
        "idempotency_key": key,
        "state": "DraftOnly",
    }
    drafts.append(draft)
    store_path.write_text(json.dumps(drafts, indent=2) + "\n", encoding="utf-8")
    return {"status": "draft_created", **draft}


def _approval_mode(tool_object):
    for candidate in (tool_object, getattr(tool_object, "metadata", None), getattr(tool_object, "function", None)):
        if candidate is None:
            continue
        value = getattr(candidate, "approval_mode", None)
        if value is not None:
            return getattr(value, "value", str(value))
    return None


def _draft_snapshot(path=DRAFTS_FILE):
    rows = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {"count": len(rows), "sha256": hashlib.sha256(payload).hexdigest()}


def self_check():
    records = _requests()
    required_record_keys = {"record_id", "status", "summary"}
    records_valid = all(
        isinstance(row, dict)
        and required_record_keys.issubset(row)
        and isinstance(row["record_id"], str)
        and row["record_id"].startswith("NS-")
        for row in records
    )
    read_signature = inspect.signature(getattr(get_request, "func", get_request))
    write_signature = inspect.signature(getattr(create_escalation_draft, "func", create_escalation_draft))
    read_mode = _approval_mode(get_request)
    write_mode = _approval_mode(create_escalation_draft)
    read_schema = get_request.to_json_schema_spec()["function"]["parameters"]
    write_schema = create_escalation_draft.to_json_schema_spec()["function"]["parameters"]
    tool_contracts_valid = (
        set(read_schema.get("required", [])) == {"record_id"}
        and set(write_schema.get("required", [])) == {"record_id", "priority", "reason"}
        and get_request.max_invocations == 2
        and create_escalation_draft.max_invocations == 1
    )
    report = {
        "status": "ok" if records_valid and tool_contracts_valid and read_mode == "never_require" and write_mode == "always_require" else "failed",
        "dataset_records": len(records),
        "dataset_schema_valid": records_valid,
        "record_ids_unique": len({row["record_id"] for row in records}) == len(records),
        "read_tool": {"name": "get_request", "approval_mode": read_mode, "signature": str(read_signature), "schema": read_schema, "max_invocations": get_request.max_invocations},
        "write_tool": {"name": "create_escalation_draft", "approval_mode": write_mode, "signature": str(write_signature), "schema": write_schema, "max_invocations": create_escalation_draft.max_invocations},
        "allowed_priorities": sorted(ALLOWED_PRIORITIES),
        "approval_limits": {"rounds": MAX_APPROVAL_ROUNDS, "requests": MAX_APPROVAL_REQUESTS},
        "draft_store": str(DRAFTS_FILE),
    }
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "ok" and report["record_ids_unique"] else 1


def edge_check():
    with tempfile.TemporaryDirectory(prefix="c926-agent-check-") as folder:
        store = Path(folder) / "drafts.json"
        created = _create_escalation_draft("NS-1042", "High", "Synthetic edge check", store)
        report = {
            "missing": _create_escalation_draft("NS-9999", "High", "Synthetic edge check", store),
            "invalid_priority": _create_escalation_draft("NS-1042", "Immediate", "Synthetic edge check", store),
            "first_write": created,
            "duplicate": _create_escalation_draft("NS-1042", "High", "Synthetic edge check", store),
            "store_snapshot": _draft_snapshot(store),
        }
    expected = [report["missing"]["status"], report["invalid_priority"]["status"], report["first_write"]["status"], report["duplicate"]["status"]]
    report["status"] = "ok" if expected == ["not_found", "invalid_priority", "draft_created", "already_exists"] else "failed"
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "ok" else 1


async def run_live(prompt: str, reject: bool, transcript_path: str):
    load_dotenv()
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    model = os.environ["FOUNDRY_MODEL_NAME"]
    before = _draft_snapshot()
    transcript: dict[str, Any] = {"prompt": prompt, "approval_requests": [], "draft_store_before": before}
    client = FoundryChatClient(project_endpoint=endpoint, model=model, credential=AzureCliCredential())
    async with Agent(
        client=client,
        name="NorthstarSupportAgent",
        instructions=(
            "You are Northstar's synthetic support assistant. You may explain supplied policy, look up synthetic requests, "
            "and prepare a draft escalation. Never claim to submit a live change. Before a draft tool call, summarize the "
            "record ID, priority and reason. Respect tool errors and approval rejection. Use at most one lookup and one "
            "draft call for a user request; never recurse or delegate."
        ),
        tools=[get_request, create_escalation_draft],
    ) as agent:
        result = await agent.run(prompt)
        approval_rounds = 0
        approval_requests = 0
        while result.user_input_requests:
            approval_rounds += 1
            if approval_rounds > MAX_APPROVAL_ROUNDS:
                raise RuntimeError(f"Approval flow exceeded {MAX_APPROVAL_ROUNDS} rounds")
            new_inputs: list[Any] = [prompt]
            for request in result.user_input_requests:
                call = request.function_call
                if call is None:
                    continue
                approval_requests += 1
                if approval_requests > MAX_APPROVAL_REQUESTS:
                    raise RuntimeError(f"Approval flow exceeded {MAX_APPROVAL_REQUESTS} requests")
                visible = {"approval_required": call.name, "arguments": call.arguments}
                print(json.dumps(visible, indent=2))
                if reject:
                    approved = False
                else:
                    token = input(f"Inspect the fields above. Type APPROVE {call.name} to execute this synthetic draft, or press Enter to reject: ").strip()
                    approved = token == f"APPROVE {call.name}"
                transcript["approval_requests"].append({**visible, "approved": approved})
                new_inputs.append(Message("assistant", [request]))
                new_inputs.append(Message("user", [request.to_function_approval_response(approved)]))
            result = await agent.run(new_inputs)
    transcript["final_text"] = result.text
    transcript["draft_store_after"] = _draft_snapshot()
    if any(not item["approved"] for item in transcript["approval_requests"]) and transcript["draft_store_after"] != before:
        raise RuntimeError("Draft store changed after a rejected approval")
    Path(transcript_path).write_text(json.dumps(transcript, indent=2, default=str) + "\n", encoding="utf-8")
    print(result.text)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--edge-check", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--prompt")
    parser.add_argument("--reject", action="store_true")
    parser.add_argument("--transcript", default="agent-transcript.json")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    if args.edge_check:
        return edge_check()
    if not args.live or not args.prompt:
        parser.error("Use --self-check, or use --live with --prompt")
    return asyncio.run(run_live(args.prompt, args.reject, args.transcript))


if __name__ == "__main__":
    raise SystemExit(main())
