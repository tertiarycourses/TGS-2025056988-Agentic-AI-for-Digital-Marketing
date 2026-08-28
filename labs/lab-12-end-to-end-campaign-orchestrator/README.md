# Lab 12 — End-to-End Campaign Orchestrator

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: A4, A5

## Objective

Connect research, strategy, content, QA, approval and publishing workflows.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A parent workflow that calls each stage, records state and stops safely on failure.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/orchestrator_runs.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `run_id`
- `campaign_id`
- `stage`
- `status`
- `started_at`
- `ended_at`
- `evidence_uri`
- `error_code`

## Detailed procedure

1. Import workflow.json plus the workflows from Labs 2, 4, 8, 9, 10 and 11.
2. Map each Execute Workflow node to the imported child workflow.
3. Enable Wait for Sub-Workflow Completion.
4. Run CMP-NS-001 in dry-run mode.
5. Inspect Run Ledger after every stage.
6. Force QA Sub-workflow to return rejected.
7. Confirm Approval and SocialPost publishing do not execute.
8. Restore the valid asset and approve its exact api_path, user, platforms and payload hash.
9. Confirm the SocialPost dry-run inspector executes once and the disabled live node is not called.
10. Export the complete run ledger and final state.

## Verification

A successful run reaches SOCIALPOST_REQUEST_INSPECTED only after research, strategy, content, QA and approval succeed; failures stop downstream execution.

Metric: `stage_success_rate = successful_stages / attempted_stages`

## Failure and control

Risk: A parent agent may continue after a failed or unapproved stage.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
