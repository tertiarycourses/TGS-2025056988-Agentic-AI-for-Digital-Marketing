# Lab 4 — Build a Tool-Using Agent with Approval Control

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 2:** Implement Generative AI and Agentic Solutions
- **Maps to:** LO3 - define an agent role, typed function tools, conversation state and a human approval boundary for consequential actions.
- **Tools:** Python, Microsoft Agent Framework, Microsoft Foundry, labs/resources/agent_tools.py
- **Duration:** 90 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Build a Northstar service agent that can read a synthetic request without approval but must pause before creating a draft escalation.

## What You Will Build

A runnable Agent Framework app with read and write tools, an approval transcript and bounded error states.

## Prerequisites

- Complete Lab 3 and keep the Foundry endpoint and model settings available.
- Review labs/resources/northstar-requests.json; all records are synthetic.
- Use the agent-framework-foundry version installed from requirements-lock.txt in Lab 2.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Run the structural and deterministic edge checks. They inspect real tool metadata and schemas, then verify missing, invalid, first-write and duplicate outcomes in a temporary store.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\agent_tools.py --self-check
.\.venv\Scripts\python.exe ..\labs\resources\agent_tools.py --edge-check > evidence\agent-edge-check.json
```

**2. Inspect the agent instructions and state the allowed role: explain policy, look up a synthetic request and prepare a draft escalation; exclude live changes and direct notification.**

```text
Role boundary is stored in source control; credentials and user data are not.
```

**3. Inspect get_request. Confirm its record_id parameter is typed, the description states when to call it, and it returns a stable found/not_found shape.**

```text
Read-only tool: approval_mode=never_require
```

**4. Inspect create_escalation_draft. Confirm allowed priority values, idempotency key, synthetic-only storage and the explicit approval requirement.**

```text
Write-like tool: approval_mode=always_require
```

**5. Run the live agent for a read-only request and save the transcript. The lookup may execute without an approval interrupt.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\agent_tools.py --live --prompt "Show the status of NS-1042" --transcript evidence\agent-read.json
```

**6. Request a draft. Inspect the visible tool name and arguments, then type the exact interactive token `APPROVE create_escalation_draft`; no write occurs before that response.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\agent_tools.py --live --prompt "Prepare a High priority escalation draft for NS-1042 because the device is unusable" --transcript evidence\agent-approved.json
```

**7. Repeat the request with explicit rejection. Confirm the transcript's before/after draft count and hash are unchanged and the response explains cancellation.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\agent_tools.py --live --prompt "Prepare a Critical escalation draft for NS-1043" --reject --transcript evidence\agent-rejected.json
```

**8. Review evidence/agent-edge-check.json for the exact missing-record, invalid-priority and duplicate-idempotency results; verify tool and approval loops are bounded.**

```text
Expected: not_found | invalid_priority | draft_created | already_exists
Limits: at most three approval rounds and three approval requests.
```

**9. Open Foundry Observability, locate one read trace and one approval-controlled trace, and record model span, tool span, latency, token and error fields in agent-observations.md.**

```text
Do not copy user text or tokens into shared evidence when traces contain sensitive content.
```

**10. Append the agent role, tool inventory, approval boundary and trace file names to the ADR, then update evidence/manifest.md.**

```text
Tools: get_request | create_escalation_draft
```

## Test It

The self-check passes; read-only lookup works without approval; approved, rejected, missing, invalid and duplicate paths produce distinct bounded outcomes; and the write-like tool never executes before explicit approval.

## Troubleshooting

- **The agent calls the write tool too early.** Strengthen the tool description and instructions so it first summarizes the proposed fields, then waits for approval.
- **No approval request appears.** Confirm the decorator uses approval_mode=always_require and that the installed Agent Framework version matches requirements-lock.txt.
- **A duplicate draft is created.** Use the supplied idempotency key and check the local draft store before writing.

## Challenge

Add a conditional rule that requires approval only for High or Critical priority while Normal drafts remain non-consequential and synthetic.

## Reflection

Which tool arguments must be visible to a person before approval is meaningful?

## Checkpoint

Save all agent evidence under C926-labs/evidence and update evidence/manifest.md. Lab 5 uses these traces to design routing and quality gates.

---

[← Lab 3](lab-03-build-and-test-a-grounded-generative-app.md) · [Lab 5 →](lab-05-design-multi-agent-routing-and-quality-gates.md)
