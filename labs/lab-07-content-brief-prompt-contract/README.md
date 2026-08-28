# Lab 07 — Content Brief & Prompt Contract

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.0  
Criteria: K3, A4

## Objective

Create a canonical content brief with evidence, brand and output constraints.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.

## What you will build

A versioned JSON content contract suitable for deterministic channel generation.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/content_brief.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `brief_id`
- `campaign_id`
- `audience_job`
- `message`
- `approved_claims`
- `evidence_ids`
- `tone`
- `cta`
- `prohibited_terms`

## Detailed procedure

1. Import workflow.json and open content_brief.xlsx.
2. Load EXP-001 and the approved research evidence.
3. Run Assemble Brief.
4. Inspect the JSON contract and version.
5. Delete evidence_ids and confirm Schema Validator fails.
6. Restore evidence_ids and run Claim Gate.
7. Add an unapproved claim and confirm it is rejected.
8. Remove the claim and review the final prompt contract.
9. Approve the exact contract hash.
10. Save brief-contract.json in evidence/.

## Verification

The approved contract includes evidence IDs, approved claims, prohibited terms, CTA, version and contract hash.

Metric: `contract_valid = required_fields_present AND evidence_ids_resolved`

## Failure and control

Risk: Unbounded prompts can invent claims or leak confidential context.

Keep the workflow inactive while learning. Credentialed publishing nodes are disabled and point to a non-routable example domain. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
