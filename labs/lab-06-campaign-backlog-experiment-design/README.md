# Lab 06 — Campaign Backlog & Experiment Design

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: A2, A4

## Objective

Convert strategy into sequenced work and measurable experiments.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

A prioritised backlog with hypotheses, variants, sample thresholds and stop rules.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/campaign_backlog.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `item_id`
- `stage`
- `hypothesis`
- `primary_metric`
- `minimum_sample`
- `stop_rule`
- `owner`
- `status`

## Detailed procedure

1. Import workflow.json and open campaign_backlog.xlsx.
2. Load the approved strategy decisions from Lab 4.
3. Run Create Work Items.
4. Inspect hypothesis, metric and owner fields.
5. Set minimum_sample to zero and confirm validation fails.
6. Restore a realistic sample threshold.
7. Add a stop rule and rerun.
8. Review prioritised items with the campaign owner.
9. Approve only items with evidence and capacity.
10. Export approved-backlog.csv.

## Verification

Each ready item has one falsifiable hypothesis, primary metric, minimum sample, stop rule and accountable owner.

Metric: `priority = expected_impact × confidence / effort`

## Failure and control

Risk: Automated testing without stop rules can expose audiences to harmful variants.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
