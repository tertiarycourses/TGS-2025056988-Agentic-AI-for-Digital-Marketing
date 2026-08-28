# Lab 05 — Channel Budget & ROI Simulator

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K4, A3

## Objective

Evaluate channel economics and allocate budget using explicit assumptions.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A scenario model for CAC, ROAS, contribution margin and incremental ROI.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/channel_economics.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `channel`
- `spend`
- `impressions`
- `clicks`
- `leads`
- `customers`
- `revenue`
- `gross_margin`

## Detailed procedure

1. Import workflow.json and open channel_economics.xlsx.
2. Load the three sample channel rows.
3. Execute Calculate Economics.
4. Manually verify LinkedIn CAC and ROAS.
5. Confirm Volume Guardrail excludes scenarios with fewer than 10 customers.
6. Change Search customers to 6 and rerun.
7. Inspect the exclusion reason.
8. Restore the value and review ranked scenarios.
9. Enter reviewer_decision and approved_budget.
10. Save the approved allocation to evidence/budget-decision.json.

## Verification

Calculated metrics match Excel formulas, low-volume scenarios are flagged and no allocation proceeds without reviewer_decision.

Metric: `CAC = spend/customers; ROAS = revenue/spend; ROI = (revenue×margin−spend)/spend`

## Failure and control

Risk: Optimising ROAS alone may cut channels that create assisted demand.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
