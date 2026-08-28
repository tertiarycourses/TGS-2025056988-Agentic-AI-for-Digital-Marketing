# Lab 01 — Campaign Brief Intake & KPI Contract

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: A1, A2

## Objective

Translate a business brief into measurable goals and channel KPIs.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A validated campaign object with objectives, KPI contracts, owners and guardrails.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/campaign_brief.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `campaign_id`
- `objective`
- `audience`
- `budget_sgd`
- `start_date`
- `end_date`
- `owner`
- `risk_tier`

## Detailed procedure

1. Import workflow.json into n8n and keep it inactive.
2. Open campaign_brief.xlsx and review the Campaign Brief sheet.
3. Copy the first row into the Brief Input node's JSON fields.
4. Execute the workflow manually.
5. Inspect Validate Required Fields for missingFields.
6. Confirm Build KPI Contract produces metric, formula, source, target and owner.
7. Set risk_tier to high and run again.
8. Confirm the review branch is selected.
9. Export the execution output to evidence/execution-output.json.
10. Record the acceptance result in evidence/checklist.md.

## Verification

Output contains campaign_id CMP-NS-001, at least three KPI contracts, one owner per KPI and a human-review flag.

Metric: `brief_completeness = populated_required_fields / 8`

## Failure and control

Risk: Missing owner or budget can cause unbounded spend.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
