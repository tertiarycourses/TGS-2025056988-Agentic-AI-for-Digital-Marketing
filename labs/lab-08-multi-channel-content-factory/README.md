# Lab 08 — Multi-Channel Content Factory

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K5, A5

## Objective

Transform one approved brief into channel-specific assets and a SocialPost-ready publishing contract.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

Website, email and SocialPost text/photo/video drafts with shared message lineage.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/content_matrix.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `asset_id`
- `brief_id`
- `evidence_ids`
- `channel`
- `media_type`
- `title`
- `description`
- `caption`
- `media_path`
- `user`
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
6. Verify website, LinkedIn and Instagram outputs differ in format, CTA and media_type.
7. Confirm every social asset has title, user, platform/channel and the media fields required by its SocialPost endpoint.
8. Set a channel limit below output length and confirm the asset is flagged.
9. Restore the limit and rerun.
10. Save generated-assets.json for Lab 9 review.

## Verification

One approved brief produces distinct channel assets; every social asset is endpoint-ready and retains brief_id, evidence_ids and validation status.

Metric: `channel_fit = passed_length AND required_fields AND approved_claims_only`

## Failure and control

Risk: Copying identical text across channels ignores audience intent and platform constraints.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
