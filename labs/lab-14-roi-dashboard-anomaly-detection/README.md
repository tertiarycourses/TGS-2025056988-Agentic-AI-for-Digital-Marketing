# Lab 14 — ROI Dashboard & Anomaly Detection

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K2, K4, A3

## Objective

Calculate channel economics and surface statistically meaningful changes.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A channel-period metric table with CAC, ROAS, ROI, confidence and anomaly flags.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/roi_dashboard.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `period`
- `channel`
- `spend`
- `customers`
- `revenue`
- `gross_margin`
- `baseline_cv`
- `current_cv`

## Detailed procedure

1. Import workflow.json and open roi_dashboard.xlsx.
2. Load the weekly samples.
3. Execute Aggregate Channel-Period and Calculate ROI.
4. Manually verify one ROI result in Excel.
5. Run Compare Baseline and inspect relative lift.
6. Set customers to 1 and confirm the confidence guardrail flags low volume.
7. Restore the value and check CPA and complaint-rate guardrails.
8. Review the dashboard dataset.
9. Enter analyst_decision for each anomaly.
10. Export dashboard-dataset.json.

## Verification

Dashboard metrics match the formulas; anomalies include volume, baseline, guardrail status and analyst decision.

Metric: `ROI = (revenue×gross_margin−spend)/spend; lift = (current−baseline)/baseline`

## Failure and control

Risk: Small samples can produce dramatic but unreliable lift.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
