# Agentic AI for Digital Marketing — Learner Guide

**Course Code:** TGS-2025056988  
**TSC:** Digital Marketing (WST-SNM-5042-1.1)  
**Version:** v2.0 · 28 August 2026

## Document Version Control Record

| Version | Effective Date | Change | Author |
|---|---|---|---|
| 1.0 | 17 July 2025 | Initial course release | Tertiary Infotech Academy |
| 2.0 | 28 August 2026 | Rebuilt around n8n agentic marketing automation with 15 connected, human-supervised labs | Dr Alfred Ang |

## Learning Outcomes

- LO1: Use generative-AI deep research and agentic workflows to formulate a digital marketing strategy, measurable objectives, KPIs and ROI model.
- LO2: Evaluate channel and campaign ROI, synthesise RACE/SOSTAC strategy models, and align recommendations with overarching marketing objectives.
- LO3: Lead the creation of an integrated online presence across web, email, social and emerging channels with human oversight.

## How to Use This Guide

### Purpose

This guide contains the detailed build procedures intentionally omitted from the visual slide deck. The 15 labs form one connected Northstar Launch campaign automation from research to content, supervised publishing, measurement and optimisation.

### Safe mode

All workflows import inactive. Mock Excel workbooks contain synthetic data. Credentialed live-publishing nodes are disabled and point to an invalid example domain. Use dry-run mode unless the trainer authorises a sandbox account.

### Human oversight

A human reviewer owns research acceptance, strategy, brand/compliance disposition, the exact publication payload and every budget or optimisation decision.

### Evidence standard

For each lab, retain the execution output, acceptance checklist and a short explanation of the failure control. Never include API keys or personal data in evidence.

## Environment Setup

### Detailed procedure

1. Create or sign in to a training n8n workspace. Use a dedicated project named TGS-2025056988-Labs.
2. Download the complete labs folder from the LMS and keep every lab folder intact.
3. Confirm each lab contains README.md, workflow.json, a data/ Excel workbook, starter/, solution/ and evidence/.
4. In n8n, choose Import from File and select the lab's workflow.json. Do not activate it.
5. Open the mock workbook and read the READ ME and Data Dictionary sheets before mapping data.
6. Run workflows manually with synthetic data first. Inspect INPUT and OUTPUT for every node before continuing.
7. Keep all live credentials outside the lab folder. Never paste secrets into Code, Set or Sticky Note nodes.
8. After each run, export only synthetic output into the evidence folder and complete the evidence checklist.

## Connected Campaign Architecture

`Research → Strategy → Content → QA → Human Approval → Social Publishing → Analytics → Optimisation`

The campaign ID `CMP-NS-001` and the supplied artifact IDs preserve lineage. Do not rename them while completing the connected run.

## Lab 01 — Campaign Brief Intake & KPI Contract

**Criteria:** A1, A2  
**Objective:** Translate a business brief into measurable goals and channel KPIs.  
**Output:** A validated campaign object with objectives, KPI contracts, owners and guardrails.  
**Mock data:** `labs/lab-01-*/data/campaign_brief.xlsx`  

### Input contract

- `campaign_id`
- `objective`
- `audience`
- `budget_sgd`
- `start_date`
- `end_date`
- `owner`
- `risk_tier`

### Detailed step-by-step procedure

1. Import workflow.json into n8n and keep it inactive.
2. Open campaign_brief.xlsx and review the Campaign Brief sheet.
3. Copy the first row into the Brief Input node's JSON fields.
4. Execute the workflow manually.
5. Inspect Validate Required Fields for missingFields.
6. Confirm Build KPI Contract produces metric, formula, source, target and owner.
7. Set risk_tier to high and run again.
8. Confirm the review branch is selected.
9. Export the execution output to evidence/execution-output.json.
10. Record the acceptance result in evidence/checklist.md.

### Verification

Output contains campaign_id CMP-NS-001, at least three KPI contracts, one owner per KPI and a human-review flag.

Metric: `brief_completeness = populated_required_fields / 8`

### Failure and control

Risk: Missing owner or budget can cause unbounded spend.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 02 — Evidence Research & Source Scoring

**Criteria:** K2  
**Objective:** Collect research signals with citation lineage and confidence scoring.  
**Output:** A research evidence table with claim, source, recency, reliability and composite score.  
**Mock data:** `labs/lab-02-*/data/research_sources.xlsx`  

### Input contract

- `source_id`
- `publisher`
- `url`
- `published_date`
- `claim`
- `relevance`
- `reliability`
- `recency`

### Detailed step-by-step procedure

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

### Verification

Every accepted claim retains source_id, URL, published date and evidence_score; no rejected row reaches synthesis.

Metric: `evidence_score = relevance × reliability × recency`

### Failure and control

Risk: Low-quality sources can contaminate every downstream asset.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 03 — Audience Signal Synthesis & Opportunity Ranking

**Criteria:** K1, K2  
**Objective:** Synthesize evidence into auditable audience jobs, pains, triggers and opportunities.  
**Output:** Ranked audience opportunities linked to evidence IDs.  
**Mock data:** `labs/lab-03-*/data/audience_signals.xlsx`  

### Input contract

- `signal_id`
- `segment`
- `job`
- `pain`
- `trigger`
- `evidence_ids`
- `impact`
- `confidence`
- `effort`

### Detailed step-by-step procedure

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

### Verification

Every opportunity has evidence_ids, an ICE score and explicit supported status before strategy synthesis.

Metric: `ICE = impact × confidence / effort`

### Failure and control

Risk: AI-generated personas may encode stereotypes or unsupported claims.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 04 — RACE/SOSTAC Strategy Synthesizer

**Criteria:** K1, K3, A4  
**Objective:** Map approved opportunities into an integrated strategy and control plan.  
**Output:** A strategy model connecting situation, objectives, audience, channels, tactics, actions and control.  
**Mock data:** `labs/lab-04-*/data/strategy_model.xlsx`  

### Input contract

- `stage`
- `decision`
- `evidence_id`
- `owner`
- `kpi`
- `target`
- `review_date`

### Detailed step-by-step procedure

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

### Verification

All strategy decisions trace to evidence, map to RACE, include control fields and pass human strategy review.

Metric: `alignment_rate = decisions_with_objective_and_owner / total_decisions`

### Failure and control

Risk: Channel tactics can drift from the business objective.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 05 — Channel Budget & ROI Simulator

**Criteria:** K4, A3  
**Objective:** Evaluate channel economics and allocate budget using explicit assumptions.  
**Output:** A scenario model for CAC, ROAS, contribution margin and incremental ROI.  
**Mock data:** `labs/lab-05-*/data/channel_economics.xlsx`  

### Input contract

- `channel`
- `spend`
- `impressions`
- `clicks`
- `leads`
- `customers`
- `revenue`
- `gross_margin`

### Detailed step-by-step procedure

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

### Verification

Calculated metrics match Excel formulas, low-volume scenarios are flagged and no allocation proceeds without reviewer_decision.

Metric: `CAC = spend/customers; ROAS = revenue/spend; ROI = (revenue×margin−spend)/spend`

### Failure and control

Risk: Optimising ROAS alone may cut channels that create assisted demand.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 06 — Campaign Backlog & Experiment Design

**Criteria:** A2, A4  
**Objective:** Convert strategy into sequenced work and measurable experiments.  
**Output:** A prioritised backlog with hypotheses, variants, sample thresholds and stop rules.  
**Mock data:** `labs/lab-06-*/data/campaign_backlog.xlsx`  

### Input contract

- `item_id`
- `stage`
- `hypothesis`
- `primary_metric`
- `minimum_sample`
- `stop_rule`
- `owner`
- `status`

### Detailed step-by-step procedure

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

### Verification

Each ready item has one falsifiable hypothesis, primary metric, minimum sample, stop rule and accountable owner.

Metric: `priority = expected_impact × confidence / effort`

### Failure and control

Risk: Automated testing without stop rules can expose audiences to harmful variants.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 07 — Content Brief & Prompt Contract

**Criteria:** K3, A4  
**Objective:** Create a canonical content brief with evidence, brand and output constraints.  
**Output:** A versioned JSON content contract suitable for deterministic channel generation.  
**Mock data:** `labs/lab-07-*/data/content_brief.xlsx`  

### Input contract

- `brief_id`
- `campaign_id`
- `audience_job`
- `message`
- `approved_claims`
- `evidence_ids`
- `tone`
- `cta`
- `prohibited_terms`

### Detailed step-by-step procedure

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

### Verification

The approved contract includes evidence IDs, approved claims, prohibited terms, CTA, version and contract hash.

Metric: `contract_valid = required_fields_present AND evidence_ids_resolved`

### Failure and control

Risk: Unbounded prompts can invent claims or leak confidential context.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 08 — Multi-Channel Content Factory

**Criteria:** K5, A5  
**Objective:** Transform one approved brief into channel-specific assets.  
**Output:** Website, email, LinkedIn, Instagram and short-video drafts with shared message lineage.  
**Mock data:** `labs/lab-08-*/data/content_matrix.xlsx`  

### Input contract

- `asset_id`
- `channel`
- `format`
- `max_chars`
- `message_angle`
- `cta`
- `status`

### Detailed step-by-step procedure

1. Import workflow.json and open content_matrix.xlsx.
2. Load the approved BRF-001 contract.
3. Execute Generate Canonical Copy.
4. Inspect the common message and evidence lineage.
5. Run Split Channels and Apply Channel Rules.
6. Verify LinkedIn, email and website outputs differ in format and CTA placement.
7. Set a channel limit below output length and confirm the asset is flagged.
8. Restore the limit and rerun.
9. Inspect Recombine Assets for one asset per requested channel.
10. Save generated-assets.json.

### Verification

One approved brief produces distinct channel assets; every asset retains brief_id, evidence_ids and validation status.

Metric: `channel_fit = passed_length AND required_fields AND approved_claims_only`

### Failure and control

Risk: Copying identical text across channels ignores audience intent and platform constraints.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 09 — Brand, Claim & Compliance QA

**Criteria:** K5, A5  
**Objective:** Apply deterministic controls before human editorial review.  
**Output:** A QA report covering schema, brand, claims, privacy, accessibility and channel limits.  
**Mock data:** `labs/lab-09-*/data/brand_rules.xlsx`  

### Input contract

- `rule_id`
- `category`
- `pattern`
- `severity`
- `action`
- `owner`

### Detailed step-by-step procedure

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

### Verification

No high-severity asset reaches approval; every medium-risk finding has category, evidence, owner and disposition.

Metric: `qa_pass_rate = passed_rules / applicable_rules`

### Failure and control

Risk: An AI self-review can miss the same hallucination made during generation.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 10 — Human Approval State Machine

**Criteria:** A5  
**Objective:** Pause automation until an accountable reviewer approves the exact payload.  
**Output:** An approval request, tamper-evident decision record and state transition.  
**Mock data:** `labs/lab-10-*/data/approval_queue.xlsx`  

### Input contract

- `approval_id`
- `asset_id`
- `payload_hash`
- `risk`
- `reviewer`
- `status`
- `decision_at`
- `comment`

### Detailed step-by-step procedure

1. Import workflow.json and open approval_queue.xlsx.
2. Load the QA-passed asset from Lab 9.
3. Execute Create Approval Record and note payload_hash.
4. Open the simulated approval form URL shown by the workflow.
5. Approve the asset with a reviewer comment.
6. Confirm Wait for Decision resumes.
7. Change the payload after approval and rerun Verify Payload Hash.
8. Confirm the workflow escalates the mismatch.
9. Restore the approved payload and rerun.
10. Save approval-record.json with reviewer, timestamp and hash.

### Verification

Only APPROVED records with a matching payload hash proceed; rejected and changed payloads cannot publish.

Metric: `approval_integrity = decision_hash == current_payload_hash`

### Failure and control

Risk: A reviewer may approve one version while a changed payload is later published.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 11 — Social Publishing Dry-Run & Idempotency

**Criteria:** K5, A5  
**Objective:** Build safe per-channel publication payloads and prevent duplicates.  
**Output:** Validated dry-run payloads for LinkedIn, Instagram and webhook-based channels.  
**Mock data:** `labs/lab-11-*/data/publishing_queue.xlsx`  

### Input contract

- `publish_id`
- `asset_id`
- `channel`
- `scheduled_at`
- `idempotency_key`
- `approval_id`
- `dry_run`
- `status`

### Detailed step-by-step procedure

1. Import workflow.json and keep Live Publisher disabled.
2. Open publishing_queue.xlsx and load PUB-001.
3. Execute Build Channel Payload.
4. Inspect the target account placeholder, media, text and scheduled time.
5. Run Idempotency Store and Already Published?.
6. Execute the dry-run branch and inspect the simulated 202 response.
7. Execute the same publish_id again.
8. Confirm the duplicate branch prevents a second publication.
9. Change channel to instagram and inspect channel-specific validation.
10. Save publication-log.json.

### Verification

Dry-run payload is channel-valid, approval-linked and idempotent; the credentialed live publisher remains disabled by default.

Metric: `duplicate_rate = duplicate_attempts / publish_attempts`

### Failure and control

Risk: Retries can publish the same content multiple times or to the wrong account.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 12 — End-to-End Campaign Orchestrator

**Criteria:** A4, A5  
**Objective:** Connect research, strategy, content, QA, approval and publishing workflows.  
**Output:** A parent workflow that calls each stage, records state and stops safely on failure.  
**Mock data:** `labs/lab-12-*/data/orchestrator_runs.xlsx`  

### Input contract

- `run_id`
- `campaign_id`
- `stage`
- `status`
- `started_at`
- `ended_at`
- `evidence_uri`
- `error_code`

### Detailed step-by-step procedure

1. Import workflow.json plus the workflows from Labs 2, 4, 8, 9, 10 and 11.
2. Map each Execute Workflow node to the imported child workflow.
3. Enable Wait for Sub-Workflow Completion.
4. Run CMP-NS-001 in dry-run mode.
5. Inspect Run Ledger after every stage.
6. Force QA Sub-workflow to return rejected.
7. Confirm Approval and Publishing do not execute.
8. Restore the valid asset and approve it.
9. Confirm the dry-run publisher executes once.
10. Export the complete run ledger and final state.

### Verification

A successful run reaches PUBLISHED_DRY_RUN only after research, strategy, content, QA and approval succeed; failures stop downstream execution.

Metric: `stage_success_rate = successful_stages / attempted_stages`

### Failure and control

Risk: A parent agent may continue after a failed or unapproved stage.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 13 — Performance Event Ingestion & Attribution

**Criteria:** K2, K4, A3  
**Objective:** Normalise channel events into a campaign performance contract.  
**Output:** A deduplicated fact table joined by campaign, asset, channel and event time.  
**Mock data:** `labs/lab-13-*/data/performance_events.xlsx`  

### Input contract

- `event_id`
- `campaign_id`
- `asset_id`
- `channel`
- `event`
- `event_time`
- `value_sgd`
- `cost_sgd`
- `source`

### Detailed step-by-step procedure

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

### Verification

All facts have unique event_id, valid campaign_id, normalised time and an explicit attribution rule or quarantine reason.

Metric: `data_quality = valid_unique_events / received_events`

### Failure and control

Risk: Inconsistent IDs and time zones can misattribute outcomes.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 14 — ROI Dashboard & Anomaly Detection

**Criteria:** K2, K4, A3  
**Objective:** Calculate channel economics and surface statistically meaningful changes.  
**Output:** A channel-period metric table with CAC, ROAS, ROI, confidence and anomaly flags.  
**Mock data:** `labs/lab-14-*/data/roi_dashboard.xlsx`  

### Input contract

- `period`
- `channel`
- `spend`
- `customers`
- `revenue`
- `gross_margin`
- `baseline_cv`
- `current_cv`

### Detailed step-by-step procedure

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

### Verification

Dashboard metrics match the formulas; anomalies include volume, baseline, guardrail status and analyst decision.

Metric: `ROI = (revenue×gross_margin−spend)/spend; lift = (current−baseline)/baseline`

### Failure and control

Risk: Small samples can produce dramatic but unreliable lift.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## Lab 15 — Optimisation Feedback Loop & Capstone

**Criteria:** A3, A4, A5  
**Objective:** Propose evidence-led changes without allowing autonomous budget or publishing mutations.  
**Output:** A controlled recommendation, experiment update and approved next-cycle campaign plan.  
**Mock data:** `labs/lab-15-*/data/optimisation_actions.xlsx`  

### Input contract

- `action_id`
- `finding`
- `evidence`
- `proposed_change`
- `expected_impact`
- `risk`
- `owner`
- `decision`
- `next_review`

### Detailed step-by-step procedure

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

### Verification

No optimisation changes a live campaign automatically; approved recommendations create a measured next-cycle experiment with full lineage.

Metric: `realised_lift = (new_result−baseline)/baseline`

### Failure and control

Risk: A self-optimising agent can chase short-term metrics and exceed delegated authority.

If the check fails, stop the downstream branch, preserve the failed payload, record the error and owner, correct the contract or policy issue, then rerun from the failed stage. Never bypass approval to make the execution appear complete.

### Required evidence

- Workflow remains inactive unless the trainer authorises otherwise.
- Execution output exported with synthetic data only.
- `evidence/checklist.md` completed.
- Learner can explain the decision rule and human oversight point.

## End-to-End Capstone Acceptance

A capstone run is complete only when:

- Research evidence has source lineage and confidence.
- Strategy decisions map to objectives, owners, KPIs and review dates.
- Channel assets retain the approved brief and evidence IDs.
- QA has no unresolved high-severity issue.
- The human decision matches the exact payload hash.
- Publishing runs in dry-run mode or an authorised sandbox and is idempotent.
- The performance ledger uses valid campaign, asset and event IDs.
- Optimisation creates a reviewed next-cycle experiment; it does not mutate a live campaign autonomously.

## Troubleshooting

### Workflow imports but has a warning

Open the named node and confirm the installed n8n version supports its type. Keep the workflow inactive until the warning is resolved.

### A field is undefined

Compare the item JSON with the lab Data Dictionary. Correct the exact field name; n8n expressions are case-sensitive.

### A branch is not taken

Open the upstream node's OUTPUT, inspect types as well as values, and test the IF/Code rule with one item.

### The Wait node does not resume

Use the test webhook URL during a manual run, keep the execution open, and submit a reviewer decision before the test URL expires.

### A duplicate publish appears

Confirm publish_id and idempotency_key are stable across retries and check the publication ledger before the publisher.

### Metrics differ from Excel

Confirm the same grain, gross-margin assumption, period and zero-division rule are used in both calculations.

## References

- n8n documentation: https://docs.n8n.io/
- Course page: https://www.tertiarycourses.com.sg/wsq-agentic-ai-for-digital-marketing.html
- Legacy course deck and the two supplied ebooks in `reference/`.

