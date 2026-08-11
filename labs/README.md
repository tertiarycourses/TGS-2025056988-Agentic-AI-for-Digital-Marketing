# AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926) — Hands-On Labs

9 labs across 5 topics · 2 days · 15 instructional hours, plus scheduled tea breaks

Work through the labs in order — each one builds on the artifacts you produced in the labs before it.


## Topic 1 — Plan and Manage an Azure AI Solution

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 1 | [Design the Northstar Foundry Solution](lab-01-design-the-northstar-foundry-solution.md) | Text editor, diagram tool, labs/resources/northstar-scenario.md, solution-adr-template.md, northstar-architecture-example.md | A completed solution architecture decision record with a service map, identity boundary, deployment path, operational indicators and risk controls. |
| 2 | [Verify Foundry Access and the Operations Baseline](lab-02-verify-foundry-access-and-the-operations-baseline.md) | Python 3.12, Azure CLI, Microsoft Foundry, Azure AI Projects SDK, labs/resources/verify_foundry.py | A verified local workspace, sanitized environment file, model response record and operations-baseline checklist linked from the ADR. |

## Topic 2 — Implement Generative AI and Agentic Solutions

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 3 | [Build and Test a Grounded Generative App](lab-03-build-and-test-a-grounded-generative-app.md) | Python, Microsoft Foundry Responses API, local synthetic policy corpus, labs/resources/grounded_app.py | A runnable grounded_app.py workflow, query trace JSON files and a five-case quality worksheet. |
| 4 | [Build a Tool-Using Agent with Approval Control](lab-04-build-a-tool-using-agent-with-approval-control.md) | Python, Microsoft Agent Framework, Microsoft Foundry, labs/resources/agent_tools.py | A runnable Agent Framework app with read and write tools, an approval transcript and bounded error states. |
| 5 | [Design Multi-Agent Routing and Quality Gates](lab-05-design-multi-agent-routing-and-quality-gates.md) | Python, Microsoft Foundry Observability, labs/resources/multi_agent_router.py, quality rubric | A multi-agent contract map, ten-case routing result, trace-based error analysis and release-gate decision record. |

## Topic 3 — Implement Computer Vision Solutions

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 6 | [Build a Responsible Multimodal Workflow](lab-06-build-a-responsible-multimodal-workflow.md) | Microsoft Foundry image playground or image model, multimodal model or Content Understanding, labs/resources/visual-policy-checklist.csv | A visual evidence packet with prompt versions, generated or rejoin image, structured observations, alt text, extended description and policy disposition. |

## Topic 4 — Implement Text Analysis Solutions

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 7 | [Implement a Text, Translation and Speech Pipeline](lab-07-implement-a-text-translation-and-speech-pipeline.md) | Python, Microsoft Foundry Responses API, Azure Speech SDK, Azure Translator SDK, labs/resources/text_speech_pipeline.py | A validated support-call JSON record, translated summary, speech evidence record and language-quality review. |

## Topic 5 — Implement Information Extraction Solutions

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 8 | [Extract Invoice Evidence with Content Understanding](lab-08-extract-invoice-evidence-with-content-understanding.md) | Python, Azure Content Understanding SDK, prebuilt-invoice analyzer, labs/resources/content_understanding_invoice.py | A sanitized Content Understanding result, extracted invoice table, field-validation log and custom-analyzer design note. |
| 9 | [Build and Verify a Hybrid Grounding Pipeline](lab-09-build-and-verify-a-hybrid-grounding-pipeline.md) | Python, Azure AI Search REST API, Microsoft Foundry Responses API, labs/resources/hybrid_search.py | A retrieval comparison report, hybrid-query result, grounded response with source IDs and a production monitoring checklist. |

---

> Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.


_Tertiary Infotech Academy Pte Ltd · C926 · v1.0 (11 August 2026)_
