# Lab 9 — Build and Verify a Hybrid Grounding Pipeline

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 5:** Implement Information Extraction Solutions
- **Maps to:** LO6 - configure semantic, hybrid and vector retrieval, connect evidence to an agent workflow and verify retrieval and grounding quality.
- **Tools:** Python, Azure AI Search REST API, Microsoft Foundry Responses API, labs/resources/hybrid_search.py
- **Duration:** 90 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Query an instructor-prepared Azure AI Search index with keyword, vector and hybrid modes, compare relevance, and pass compact cited evidence to the Northstar grounded app.

## What You Will Build

A retrieval comparison report, hybrid-query result, grounded response with source IDs and a production monitoring checklist.

## Prerequisites

- Complete Lab 8 and retain its sanitized markdown and structured fields.
- Confirm the prepared index, vectorizer and semantic configuration, plus Search Index Data Reader on the prepared index or search-service scope.
- Set AZURE_SEARCH_ENDPOINT and AZURE_SEARCH_INDEX; use SEARCH_API_KEY only if the training environment cannot use Entra ID.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the index contract, sample documents and editable comparison template into work/, then identify the key, content, vector, source, freshness and permission-filter fields.**

```text
Copy-Item ..\labs\resources\search-index-contract.json work\search-index-contract.json
Copy-Item ..\labs\resources\search-documents.json work\search-documents.json
Copy-Item ..\labs\resources\retrieval-comparison.csv work\retrieval-comparison.csv
```

**2. Run offline mode first. Confirm both the operations-only restricted document and the same-category restricted device document are excluded for learner scope.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\hybrid_search.py --offline --query "replacement laptop evidence" --out evidence\search-offline.json
Expected absent: NS-RESTRICTED-001 and NS-RESTRICTED-DEVICE-002
```

**3. Run a keyword query and record top source IDs, ranks and exact-term strengths; if unavailable, copy the exact keyword rejoin report.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\hybrid_search.py --mode keyword --query "replacement laptop evidence" --out evidence\search-keyword.json
# Rejoin: Copy-Item ..\labs\resources\search-keyword-rejoin.json evidence\search-keyword.json
```

**4. Run a vector query using integrated text vectorization and record semantic matches that lack exact words; if unavailable, copy the exact vector rejoin report.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\hybrid_search.py --mode vector --query "proof required when a work computer must be exchanged" --out evidence\search-vector.json
# Rejoin: Copy-Item ..\labs\resources\search-vector-rejoin.json evidence\search-vector.json
```

**5. Run a hybrid query with semantic ranking when supported. If the service is unavailable, copy the named answerable and unsupported rejoin reports into the exact downstream filenames.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\hybrid_search.py --mode hybrid --semantic --query "proof required for urgent laptop exchange" --out evidence\search-hybrid.json
# Rejoin: Copy-Item ..\labs\resources\search-hybrid-rejoin.json evidence\search-hybrid.json
# Rejoin: Copy-Item ..\labs\resources\search-unsupported-rejoin.json evidence\search-unsupported.json
```

**6. Verify the combined category and learner-scope filter separately from relevance using the same-category restricted device document.**

```text
Filter: category eq 'device-support' and access_scope eq 'learner'
Expected excluded source: NS-RESTRICTED-DEVICE-002
```

**7. Complete work/retrieval-comparison.csv for precision, coverage, empty results, freshness, permission filtering and latency across all three modes.**

```text
Do not compare scores from unlike ranking stages as if they shared one scale.
```

**8. Run the unsupported retrieval unless its rejoin file exists, then pass both evidence files to the grounded app. The unsupported command fails unless supported=false with no citations.**

```text
if (-not (Test-Path evidence\search-unsupported.json)) { .\.venv\Scripts\python.exe ..\labs\resources\hybrid_search.py --mode keyword --query "home renovation reimbursement" --out evidence\search-unsupported.json }
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --evidence evidence\search-hybrid.json --query "What proof should I attach for an urgent laptop exchange?" --live --out evidence\final-grounded.json
.\.venv\Scripts\python.exe ..\labs\resources\grounded_app.py --evidence evidence\search-unsupported.json --query "Can Northstar reimburse a home renovation?" --live --expect-unsupported --out evidence\final-unsupported.json
```

**9. Define monitoring for ingestion failures, document count, index freshness, empty retrieval, relevance, citation coverage, groundedness, latency, tokens, safety events and access-filter violations.**

```text
For each signal: query or view | threshold | owner | response
```

**10. Update the ADR with the query pattern, filter, evidence contract, quality results, limitations and rollback path, then complete evidence/manifest.md.**

```text
Final checkpoint: architecture -> app -> agent -> multimodal -> text -> extraction -> retrieval -> operations
```

## Test It

Keyword, vector and hybrid reports contain source IDs and latency; the permission filter excludes restricted content; the final answer cites only retrieved sources; and the monitoring checklist covers ingestion, retrieval, generation, security and operations.

## Troubleshooting

- **The vector query reports no vectorizer.** Use the instructor-provided index that has integrated vectorization or switch to the documented rejoin result; do not invent embedding dimensions.
- **Hybrid results are worse than keyword results.** Inspect query wording, k, fields, filters and semantic configuration; hybrid is a method to evaluate, not a guaranteed win.
- **A restricted source appears.** Stop the workflow, preserve the trace, verify filter construction and index metadata, and do not pass the evidence to generation.

## Challenge

Add a freshness test that inserts a later synthetic policy version and verifies the old source remains auditable but is not presented as current.

## Reflection

Which retrieval and grounding signals would allow you to distinguish a stale index from a weak generation prompt?

## Checkpoint

Save all search and grounded reports under evidence/, the comparison under work/, and complete the ADR plus evidence/manifest.md. The Northstar course project is ready for final recap.

---

[← Lab 8](lab-08-extract-invoice-evidence-with-content-understanding.md) · [Labs index →](README.md)
