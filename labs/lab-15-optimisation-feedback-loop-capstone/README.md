# Lab 15 — Optimisation Feedback Loop & Capstone

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: A3, A4, A5

## Objective

Propose evidence-led changes without allowing autonomous budget or publishing mutations.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

A controlled recommendation, experiment update and approved next-cycle campaign plan.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/optimisation_actions.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `action_id`
- `finding`
- `evidence`
- `proposed_change`
- `expected_impact`
- `risk`
- `owner`
- `decision`
- `next_review`

## Detailed procedure

1. Import workflow.json and open optimisation_actions.xlsx.
2. Load the reviewed dashboard from Lab 14.
3. Execute Generate Recommendation.
4. Inspect evidence, expected impact and uncertainty.
5. Set proposed budget change to 60% and confirm Policy Guardrails rejects it.
6. Restore the change to 10%.
7. Approve the recommendation with an accountable owner.
8. Confirm Update Backlog creates a new experiment rather than mutating a live campaign.
9. Run the full dry-run chain from Lab 12 with the new backlog item.
10. Save the cycle audit and write a capstone reflection.

## Verification

No optimisation changes a live campaign automatically; approved recommendations create a measured next-cycle experiment with full lineage.

Metric: `realised_lift = (new_result−baseline)/baseline`

## Failure and control

Risk: A self-optimising agent can chase short-term metrics and exceed delegated authority.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
