# Lab 10 — Human Approval State Machine

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: A5

## Objective

Pause automation until an accountable reviewer approves the exact payload.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

An approval request, tamper-evident decision record and state transition.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/approval_queue.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `approval_id`
- `asset_id`
- `payload_hash`
- `risk`
- `reviewer`
- `status`
- `decision_at`
- `comment`

## Detailed procedure

1. Import workflow.json and open approval_queue.xlsx.
2. Load the QA-passed asset from Lab 9.
3. Execute Create Approval Record and note payload_hash.
4. Open the simulated approval form URL shown by the workflow.
5. Approve the asset with a reviewer comment.
6. Confirm Wait for Decision resumes.
7. Change the payload after approval and rerun Verify Payload Hash.
8. Confirm the workflow escalates the mismatch.
9. Restore the approved payload and rerun.
10. Save approval-record.json with reviewer, timestamp and hash.

## Verification

Only APPROVED records with a matching payload hash proceed; rejected and changed payloads cannot publish.

Metric: `approval_integrity = decision_hash == current_payload_hash`

## Failure and control

Risk: A reviewer may approve one version while a changed payload is later published.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
