# Lab 04 — RACE/SOSTAC Strategy Synthesizer

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: K1, K3, A4

## Objective

Map approved opportunities into an integrated strategy and control plan.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

A strategy model connecting situation, objectives, audience, channels, tactics, actions and control.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/strategy_model.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `stage`
- `decision`
- `evidence_id`
- `owner`
- `kpi`
- `target`
- `review_date`

## Detailed procedure

1. Import workflow.json and review strategy_model.xlsx.
2. Load approved opportunities from Lab 3.
3. Execute Build RACE Map.
4. Verify each RACE stage names an audience action and channel role.
5. Execute Build SOSTAC Control.
6. Inspect owner, KPI, target and review date.
7. Remove an owner and confirm Alignment Gate fails.
8. Restore the owner and set review_status=approved.
9. Export strategy-draft.json.
10. Compare the automation output with the original business objective.

## Verification

All strategy decisions trace to evidence, map to RACE, include control fields and pass human strategy review.

Metric: `alignment_rate = decisions_with_objective_and_owner / total_decisions`

## Failure and control

Risk: Channel tactics can drift from the business objective.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
