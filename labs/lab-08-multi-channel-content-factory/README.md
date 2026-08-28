# Lab 08 — Multi-Channel Content Factory

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: K5, A5

## Objective

Transform one approved brief into channel-specific assets.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

Website, email, LinkedIn, Instagram and short-video drafts with shared message lineage.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/content_matrix.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `asset_id`
- `channel`
- `format`
- `max_chars`
- `message_angle`
- `cta`
- `status`

## Detailed procedure

1. Import workflow.json and open content_matrix.xlsx.
2. Load the approved BRF-001 contract.
3. Execute Generate Canonical Copy.
4. Inspect the common message and evidence lineage.
5. Run Split Channels and Apply Channel Rules.
6. Verify LinkedIn, email and website outputs differ in format and CTA placement.
7. Set a channel limit below output length and confirm the asset is flagged.
8. Restore the limit and rerun.
9. Inspect Recombine Assets for one asset per requested channel.
10. Save generated-assets.json.

## Verification

One approved brief produces distinct channel assets; every asset retains brief_id, evidence_ids and validation status.

Metric: `channel_fit = passed_length AND required_fields AND approved_claims_only`

## Failure and control

Risk: Copying identical text across channels ignores audience intent and platform constraints.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
