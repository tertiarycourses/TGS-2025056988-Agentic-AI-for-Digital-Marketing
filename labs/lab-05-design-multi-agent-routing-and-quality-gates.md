# Lab 5 — Design Multi-Agent Routing and Quality Gates

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 2:** Implement Generative AI and Agentic Solutions
- **Maps to:** LO3 - implement bounded specialist routing, evaluate agent behavior and define observability and release gates.
- **Tools:** Python, Microsoft Foundry Observability, labs/resources/multi_agent_router.py, quality rubric
- **Duration:** 60 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Use a deterministic routing simulator and Foundry traces to separate policy, request and extraction specialists, then define quality thresholds for release.

## What You Will Build

A multi-agent contract map, ten-case routing result, trace-based error analysis and release-gate decision record.

## Prerequisites

- Complete Lab 4 and retain its three agent transcripts.
- Copy all editable contracts, cases and analysis templates into C926-labs/work before changing them.
- Use the local simulator first; a live connected-agent implementation is optional when the instructor environment supports it.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the contracts, main cases, intentionally failing boundary case and error-analysis template into work/, then verify every specialist has a distinct description, routing terms, context, result, tools, timeout and owner.**

```text
Copy-Item ..\labs\resources\agent-contracts.yaml work\agent-contracts.yaml
Copy-Item ..\labs\resources\multi-agent-cases.jsonl work\multi-agent-cases.jsonl
Copy-Item ..\labs\resources\multi-agent-boundary-cases.jsonl work\multi-agent-boundary-cases.jsonl
Copy-Item ..\labs\resources\error-analysis-template.csv work\error-analysis.csv
```

**2. Run the ten-case deterministic router against the copied contracts and save its JSON report.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\multi_agent_router.py --contracts work\agent-contracts.yaml --cases work\multi-agent-cases.jsonl --out evidence\routing-report-before.json
```

**3. Run the intentional boundary baseline with --allow-errors, add one precise capability/routing term to the copied policy contract, capture the diff and rerun until the boundary case passes.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\multi_agent_router.py --contracts work\agent-contracts.yaml --cases work\multi-agent-boundary-cases.jsonl --out evidence\routing-boundary-before.json --allow-errors
# Edit work\agent-contracts.yaml: add entitlement or replacement-device wording only to policy_grounding
git diff --no-index ..\labs\resources\agent-contracts.yaml work\agent-contracts.yaml > evidence\agent-contract-change.diff
.\.venv\Scripts\python.exe ..\labs\resources\multi_agent_router.py --contracts work\agent-contracts.yaml --cases work\multi-agent-boundary-cases.jsonl --out evidence\routing-boundary-after.json
```

**4. Rerun all ten main cases after the contract change and confirm no existing boundary regressed.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\multi_agent_router.py --contracts work\agent-contracts.yaml --cases work\multi-agent-cases.jsonl --out evidence\routing-report-after.json
```

**5. Draw the orchestrator flow with minimum context shared to each specialist, one correlation ID, per-hop timeout and a safe fallback.**

```text
User -> Orchestrator -> Specialist -> Result
Limits: one delegation hop | bounded context | no recursive routing
```

**6. Review the Lab 4 traces and classify each issue in work/error-analysis.csv as routing, tool selection, tool input, tool result, generation, policy or infrastructure.**

```text
Each row needs correlation ID, evidence and corrective owner.
```

**7. Define a release set containing core, boundary, adversarial and failure scenarios; select relevance, groundedness, task completion, tool selection, tool input, latency and safety criteria.**

```text
Each criterion needs a target, threshold, evidence source and owner.
```

**8. In Foundry Evaluations, create or outline a run using the available built-in evaluators. Record unavailable or preview features as constraints rather than substituting unverified scores.**

```text
Suggested quality: relevance | groundedness | task completion
Suggested process: tool selection | tool input accuracy
```

**9. Set release, hold and rollback rules, make one evidence-based decision, link all evidence in the ADR and update evidence/manifest.md.**

```text
Release only if critical safety/tool cases meet their threshold and no unresolved high-impact defect remains.
```

## Test It

All ten cases have an expected and actual route, no specialist receives an excluded task, every observed failure is assigned to a pipeline stage, and the release record contains measurable quality, safety, latency and rollback criteria.

## Troubleshooting

- **Two specialists match the same case.** Rewrite descriptions around exclusive intent, data and permitted action; do not rely on agent names alone.
- **Tracing has not appeared.** Wait several minutes, verify project tracing is enabled and use transcript timestamps as temporary evidence.
- **An evaluator is unavailable in the region.** Record the limitation and use a documented manual rubric or custom deterministic check for the same criterion.

## Challenge

Add a fourth specialist and quantify the added routing ambiguity, latency budget and operational ownership before accepting it.

## Reflection

What evidence would justify multiple agents instead of one agent with three tools?

## Checkpoint

Save before/after routing reports, the contract diff, error analysis and release decision under C926-labs, then update evidence/manifest.md. Day 2 extends the same solution to visual, audio and document evidence.

---

[← Lab 4](lab-04-build-a-tool-using-agent-with-approval-control.md) · [Lab 6 →](lab-06-build-a-responsible-multimodal-workflow.md)
