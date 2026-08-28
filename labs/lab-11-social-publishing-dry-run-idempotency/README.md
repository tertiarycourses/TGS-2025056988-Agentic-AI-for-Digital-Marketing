# Lab 11 — Social Publishing Dry-Run & Idempotency

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: K5, A5

## Objective

Build safe per-channel publication payloads and prevent duplicates.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

Validated dry-run payloads for LinkedIn, Instagram and webhook-based channels.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/publishing_queue.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `publish_id`
- `asset_id`
- `channel`
- `scheduled_at`
- `idempotency_key`
- `approval_id`
- `dry_run`
- `status`

## Detailed procedure

1. Import workflow.json and keep Live Publisher disabled.
2. Open publishing_queue.xlsx and load PUB-001.
3. Execute Build Channel Payload.
4. Inspect the target account placeholder, media, text and scheduled time.
5. Run Idempotency Store and Already Published?.
6. Execute the dry-run branch and inspect the simulated 202 response.
7. Execute the same publish_id again.
8. Confirm the duplicate branch prevents a second publication.
9. Change channel to instagram and inspect channel-specific validation.
10. Save publication-log.json.

## Verification

Dry-run payload is channel-valid, approval-linked and idempotent; the credentialed live publisher remains disabled by default.

Metric: `duplicate_rate = duplicate_attempts / publish_attempts`

## Failure and control

Risk: Retries can publish the same content multiple times or to the wrong account.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
