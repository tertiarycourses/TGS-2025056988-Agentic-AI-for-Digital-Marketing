# Lab 13 — Performance Event Ingestion & Attribution

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: K2, K4, A3

## Objective

Normalise channel events into a campaign performance contract.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

A deduplicated fact table joined by campaign, asset, channel and event time.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/performance_events.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `event_id`
- `campaign_id`
- `asset_id`
- `channel`
- `event`
- `event_time`
- `value_sgd`
- `cost_sgd`
- `source`

## Detailed procedure

1. Import workflow.json and open performance_events.xlsx.
2. Load the sample events.
3. Execute Normalise Schema.
4. Confirm timestamps use ISO 8601 with offset.
5. Duplicate EVT-001 and run Deduplicate Event IDs.
6. Confirm only one fact remains.
7. Remove campaign_id and confirm the event is quarantined.
8. Restore the ID and run Join Campaign Map.
9. Inspect the attribution label and limitation field.
10. Save performance-facts.csv.

## Verification

All facts have unique event_id, valid campaign_id, normalised time and an explicit attribution rule or quarantine reason.

Metric: `data_quality = valid_unique_events / received_events`

## Failure and control

Risk: Inconsistent IDs and time zones can misattribute outcomes.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
