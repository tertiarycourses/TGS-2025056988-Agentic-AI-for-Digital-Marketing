# Lab 11 — SocialPost API Publishing & Idempotency

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K5, A5

## Objective

Map approved content into the SocialPost API and prevent duplicate sends.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## Lab 12 sub-workflow entry

Use **Manual Trigger → Approved Social Asset** for this lab's two-row duplicate demonstration. When Lab 12 calls this workflow, **Sub-workflow Input** consumes the single approved item passed from Lab 10 and bypasses the standalone fixture.


## What you will build

Validated SocialPost multipart request; live HTTP node disabled.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/publishing_queue.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `publish_id`
- `asset_id`
- `media_type`
- `api_path`
- `user`
- `platforms`
- `title`
- `description`
- `caption`
- `media_path`
- `scheduled_at`
- `idempotency_key`
- `approval_id`
- `decision_hash`
- `approval_verified`
- `credential_ready`
- `dry_run`
- `status`

## Detailed procedure

1. Import workflow.json and keep all three SocialPost API nodes disabled.
2. Open publishing_queue.xlsx and load both PUB-001 rows to exercise the in-batch duplicate gate.
3. Execute Build SocialPost Form Data and verify api_url resolves to https://socialmediapost.tertiaryinfotech.com/api/upload_text.
4. Inspect the multipart map: user, one exact platform[] value, title and caption; no API key appears in workflow JSON.
5. Confirm each queue item contains exactly one approved platform; create one queue item per platform so repeated multi-platform sends remain approval-bound and idempotent.
6. Confirm current_payload_hash matches the decision_hash from Lab 10 and approval_verified remains true.
7. In n8n Credentials, create a Header Auth credential named SocialPost Training with header Authorization and value Apikey followed by the sandbox key; do not paste the key into any node.
8. Select that credential on Text API (Disabled), Photo API (Disabled) and Video API (Disabled), but leave all nodes disabled.
9. Run Idempotency Store and Already Published?; confirm the second PUB-001 row routes to Dead Letter as a duplicate.
10. Confirm the first row reaches Dry Run? and routes to SocialPost Dry-Run Inspect because dry_run=true; no HTTP node executes.
11. For production, replace workflow static data with a durable n8n Data Table or database-backed unique key on idempotency_key.
12. Only with trainer authorisation, set dry_run=false and credential_ready=true, enable exactly the matching media node for one sandbox post, and confirm Publish Succeeded? receives a real 2xx full response before the key is marked.
13. Leave the media node disabled deliberately once and confirm pass-through routes to Dead Letter without consuming the idempotency key; repeat with a simulated non-2xx/partial-failure result.
14. Save publication-log.json with publish_id, approval_id, current_payload_hash, terminal node, HTTP status and raw response.

## Verification

The inspected request uses the documented SocialPost endpoint and Apikey credential pattern, remains approval-linked and idempotent, and sends nothing unless the trainer explicitly enables the sandbox node.

Metric: `duplicate_rate = duplicate_attempts / publish_attempts`

## Failure and control

Risk: Retries can publish the same approved content more than once or to an unapproved SocialPost profile.

The SocialPost HTTP Request node points to the live documented API but is disabled. Keep the API key only in an n8n Header Auth credential and use the local dry-run inspector unless a trainer explicitly authorises one sandbox post.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
