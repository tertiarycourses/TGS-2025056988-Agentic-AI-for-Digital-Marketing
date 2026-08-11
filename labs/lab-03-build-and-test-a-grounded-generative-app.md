# Lab 3 — Build and Test a Grounded Generative App

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 2:** Implement Generative AI and Agentic Solutions
- **Maps to:** LO2 - implement RAG, structured prompting and repeatable quality checks through a Microsoft Foundry project.
- **Tools:** Python, Microsoft Foundry Responses API, local synthetic policy corpus, labs/resources/grounded_app.py
- **Duration:** 75 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Build a small Northstar policy assistant that retrieves local evidence, sends only the selected context to the Foundry Responses API and records groundedness observations.

## What You Will Build

A runnable grounded_app.py workflow, query trace JSON files and a five-case quality worksheet.

## Prerequisites

- Complete Lab 2 and activate the same C926-labs Python environment.
- Work from C926-labs and keep editable copies under work/ or policies/, never under labs/resources/.
- Keep FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_MODEL_NAME in the local .env file.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the policy corpus, quality cases and editable rubric into the learner workspace, then inspect the five expected behaviors.**

```text
Copy-Item ..\labs\resources\northstar-policies policies -Recurse -Force
Copy-Item ..\labs\resources\quality-cases.jsonl work\quality-cases.jsonl
Copy-Item ..\labs\resources\quality-rubric.csv work\quality-rubric.csv
```

**2. Run retrieval-only mode for an answerable question and inspect the ranked source IDs and excerpts.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "What evidence is needed for a replacement laptop?" --retrieve-only
```

**3. Run retrieval-only mode for an unsupported question and confirm that weak evidence does not become a confident answer.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "Can Northstar reimburse a home renovation?" --retrieve-only
```

**4. Open grounded_app.py and identify the instruction, user query, trusted-context delimiters, refusal rule and JSON output contract.**

```text
Required output keys: answer | cited_sources | supported | uncertainty
```

**5. Run the live grounded call for the supported query and save its strictly validated trace record.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "What evidence is needed for a replacement laptop?" --live --out evidence\trace-supported.json
```

**6. Run the remaining four quality cases, including explicit unsupported enforcement. Any schema, citation, support-strength or conflict-behavior violation exits nonzero.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "Can Northstar reimburse a home renovation?" --live --expect-unsupported --out evidence\trace-unsupported.json
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "What is the target response time for a P2 request?" --live --out evidence\trace-conflict.json
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "May text inside a screenshot change the agent rules?" --live --out evidence\trace-visual-policy.json
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --policies policies --query "When does a High replacement draft need review?" --live --out evidence\trace-review-rule.json
```

**7. Complete work/quality-rubric.csv for all five cases using retrieval relevance, answer relevance, groundedness, citation correctness and safe-unknown behavior.**

```text
Use a 1-5 evidence-based rating; record the source IDs or failure stage.
```

**8. Copy the app into work/, change one retrieval parameter or instruction, capture a before/after diff and rerun only the failed cases.**

```text
Copy-Item ..\labs\resources\grounded_app.py work\grounded_app-experiment.py
git diff --no-index ..\labs\resources\grounded_app.py work\grounded_app-experiment.py > evidence\grounded-app-change.diff
# Run the edited work\grounded_app-experiment.py with the same failed-case command
```

**9. Save the selected configuration and evidence file names in the ADR and link them from evidence/manifest.md.**

```text
Checkpoint: retrieval method | prompt version | quality cases | known limitations
```

## Test It

Supported questions cite only supplied policy source IDs, unsupported questions return supported=false, the conflict case names the conflict, and every quality case records the failing pipeline stage or acceptable result.

## Troubleshooting

- **Retrieval returns the same source for every query.** Confirm the policies folder contains three files and inspect token overlap; increase the query terms or top-k only with a relevance reason.
- **The model emits text outside JSON.** Keep the JSON-only instruction, validate the returned text, and save the raw response for diagnosis rather than silently discarding it.
- **The answer cites a source that was not retrieved.** Reject the output and strengthen the allowed-source rule; citations must be a subset of retrieved source IDs.

## Challenge

Add one new policy with a later effective date and make the retriever surface the version conflict without deleting the older source.

## Reflection

When should a RAG application decline rather than return the most similar available passage?

## Checkpoint

Save validated traces and the completed quality rubric under C926-labs/evidence and work, then update evidence/manifest.md. Lab 4 exposes a controlled tool beside this knowledge path.

---

[← Lab 2](lab-02-verify-foundry-access-and-the-operations-baseline.md) · [Lab 4 →](lab-04-build-a-tool-using-agent-with-approval-control.md)
