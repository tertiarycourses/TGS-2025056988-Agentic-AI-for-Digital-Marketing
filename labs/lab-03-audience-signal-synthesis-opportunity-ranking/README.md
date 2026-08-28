# Lab 03 — Audience Signal Synthesis & Opportunity Ranking

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K1, K2

## Objective

Synthesize evidence into auditable audience jobs, pains, triggers and opportunities.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

Ranked audience opportunities linked to evidence IDs.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/audience_signals.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `signal_id`
- `segment`
- `job`
- `pain`
- `trigger`
- `evidence_ids`
- `impact`
- `confidence`
- `effort`

## Detailed procedure

1. Import workflow.json and open audience_signals.xlsx.
2. Review each signal's evidence_ids.
3. Load the sample row into Audience Signals.
4. Execute Validate Evidence Links.
5. Remove SRC-001 and confirm validation fails.
6. Restore the link and run Compute ICE Score.
7. Confirm the score is 10.0 for the sample.
8. Review the ranked backlog and mark supported=true only after checking evidence.
9. Save the approved backlog.
10. Record a rejected persona statement and why it was rejected.

## Verification

Every opportunity has evidence_ids, an ICE score and explicit supported status before strategy synthesis.

Metric: `ICE = impact × confidence / effort`

## Failure and control

Risk: AI-generated personas may encode stereotypes or unsupported claims.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
