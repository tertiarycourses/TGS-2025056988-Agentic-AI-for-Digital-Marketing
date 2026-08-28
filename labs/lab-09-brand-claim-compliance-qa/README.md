# Lab 09 — Brand, Claim & Compliance QA

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K5, A5

## Objective

Apply deterministic controls before human editorial review.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A QA report covering schema, brand, claims, privacy, accessibility and channel limits.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/brand_rules.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `rule_id`
- `category`
- `pattern`
- `severity`
- `action`
- `owner`

## Detailed procedure

1. Import workflow.json and open brand_rules.xlsx.
2. Load assets from Lab 8 and the mock rules.
3. Run Deterministic Checks.
4. Confirm the word guaranteed creates a high-severity violation.
5. Remove the prohibited claim and rerun.
6. Insert an email address and confirm privacy review is required.
7. Inspect the Risk Classifier routing.
8. Verify only zero-high-severity assets reach Pass Queue.
9. Assign review owners for medium-risk findings.
10. Export qa-report.json.

## Verification

No high-severity asset reaches approval; every medium-risk finding has category, evidence, owner and disposition.

Metric: `qa_pass_rate = passed_rules / applicable_rules`

## Failure and control

Risk: An AI self-review can miss the same hallucination made during generation.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
