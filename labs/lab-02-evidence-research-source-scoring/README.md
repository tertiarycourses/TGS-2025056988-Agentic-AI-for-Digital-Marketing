# Lab 02 — Evidence Research & Source Scoring

Course: Agentic AI for Digital Marketing (TGS-2025056988)  
Version: v2.1  
Criteria: K2

## Objective

Collect research signals with citation lineage and confidence scoring.

## Connected campaign stage

This lab continues the synthetic **Northstar Launch** campaign. Its output is designed to feed the next lab. Keep all supplied IDs unchanged so lineage remains visible end to end.


## What you will build

A research evidence table with claim, source, recency, reliability and composite score.

## Files in this folder

- `workflow.json` — importable n8n workflow; inactive and safe by default.
- `data/research_sources.xlsx` — synthetic Excel input with Data Dictionary and READ ME sheets.
- `starter/notes.md` — learner working notes.
- `solution/expected-output.json` — expected evidence shape, not a live credential or answer key.
- `evidence/checklist.md` — acceptance checklist.

## Input contract

- `source_id`
- `publisher`
- `url`
- `published_date`
- `claim`
- `relevance`
- `reliability`
- `recency`

## Detailed procedure

1. Import workflow.json and open research_sources.xlsx.
2. Inspect the field definitions on the Data Dictionary sheet.
3. Paste the mock rows into Research Inputs.
4. Execute Normalise Evidence and inspect ISO dates and numeric scores.
5. Confirm Score Sources calculates evidence_score.
6. Change reliability of SRC-002 to 0.90 and rerun.
7. Verify Confidence Gate routes records at or above 0.60 to Accepted Evidence.
8. Verify rejected records retain rejection_reason.
9. Save accepted rows to evidence/accepted-research.csv.
10. Document one source-quality limitation.

## Verification

Every accepted claim retains source_id, URL, published date and evidence_score; no rejected row reaches synthesis.

Metric: `evidence_score = relevance × reliability × recency`

## Failure and control

Risk: Low-quality sources can contaminate every downstream asset.

Keep the workflow inactive while learning. Credentialed publishing nodes remain disabled. Use dry-run output unless a trainer explicitly authorises a sandbox social account.

## Clean-up

Delete any temporary credentials from n8n, leave the workflow inactive, and retain only synthetic evidence files. Never place API keys in this folder.
