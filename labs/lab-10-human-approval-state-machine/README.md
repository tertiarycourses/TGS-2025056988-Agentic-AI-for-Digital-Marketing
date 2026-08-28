# Lab 10 — Human Approval State Machine

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: A5

## Objective

Pause automation until an accountable reviewer approves the exact SocialPost request payload.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

An approval request, tamper-evident decision record and state transition bound to endpoint, user and platforms.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/approval_queue.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `approval_id`
- `asset_id`
- `api_path`
- `user`
- `platforms`
- `title`
- `caption`
- `decision_hash`
- `risk`
- `reviewer`
- `status`
- `decision_at`
- `comment`

## Detailed procedure

1. Import workflow.json and open approval_queue.xlsx.
2. Load the QA-passed AST-002 asset from Lab 9.
3. Confirm api_path is /api/upload_text and platforms is the exact linkedin list used in Lab 11.
4. Execute Create Approval Record and note current_payload_hash.
5. Confirm the canonical hash covers asset_id, api_path, user, platform list, title and caption.
6. The supplied Wait for Decision node is disabled for deterministic dry-run inspection; enable and configure its test webhook only when practising a live reviewer callback.
7. Run Verify Payload Hash and confirm the APPROVED fixture reaches Approved with approval_verified=true.
8. Change the title without changing decision_hash and rerun Verify Payload Hash.
9. Confirm the workflow routes the mismatch to Escalated and never reaches Approved.
10. Restore the approved payload and save approval-record.json with reviewer, timestamp, canonical payload and decision hash.

## Verification

Only APPROVED records with a matching SocialPost payload hash proceed; rejected, retargeted or changed payloads cannot publish.

Metric: `approval_integrity = decision_hash == current_payload_hash`

## Failure and control

Risk: A reviewer may approve one version while a changed payload is later published.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
