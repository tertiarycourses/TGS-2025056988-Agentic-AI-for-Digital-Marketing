# Lab 1 — Design the Northstar Foundry Solution

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 1:** Plan and Manage an Azure AI Solution
- **Maps to:** LO1 - select task-fit models and Foundry services, then define infrastructure, security, operations and responsible AI controls.
- **Tools:** Text editor, diagram tool, labs/resources/northstar-scenario.md, solution-adr-template.md, northstar-architecture-example.md
- **Duration:** 45 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Translate the Northstar support scenario into a bounded architecture and decision record before provisioning or coding.

## What You Will Build

A completed solution architecture decision record with a service map, identity boundary, deployment path, operational indicators and risk controls.

## Prerequisites

- Open the scenario, ADR template and partially completed northstar-architecture-example.md; use the example to keep the nine-step design within 45 minutes.
- Use only the supplied synthetic users, policies, documents and request records.
- Review the official AI-103 skills outline in reference/SOURCES.md.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. From the repository root, create the standard learner workspace and copy the ADR and checkpoint templates before editing either file.**

```text
New-Item -ItemType Directory -Force C926-labs,C926-labs\evidence,C926-labs\work | Out-Null
Copy-Item labs\resources\solution-adr-template.md C926-labs\northstar-solution-adr.md
Copy-Item labs\resources\learner-checkpoint-manifest.md C926-labs\evidence\manifest.md
```

**2. In C926-labs/northstar-solution-adr.md, state the measurable outcome, intended users and explicit exclusions.**

```text
Outcome: cited support guidance and safe draft-request preparation
Excluded: identity changes, entitlement overrides, financial commitments
```

**3. Map the workload modalities and select a language model, Foundry project, Azure AI Search, Content Understanding, Speech or Translator only where the scenario needs them.**

```text
Question -> Foundry model
Policy evidence -> Azure AI Search
Invoice or image -> Content Understanding
Call audio -> Speech or multimodal processing
```

**4. Draw the solution boundary from user channel through application, Foundry project, model deployment, retrieval, agent tools and observability.**

```text
User -> App -> Foundry project -> {Model, Search, Tools} -> Trace store
```

**5. Record the acting identity at every hop and choose Microsoft Entra authentication for the application and developer path where supported.**

```text
Developer: Azure CLI identity
Application: managed identity
End user: application identity plus enforced user filter
```

**6. Define development, validation and production environments with one promotion path for code, prompts, indexes and configuration.**

```text
Development -> validation gate -> production
Rollback artifact: last known-good release plus configuration record
```

**7. Add capacity and cost controls for requests, tokens, concurrency, output length, image jobs and downstream rate limits.**

```text
Controls: budgets | quotas | bounded retry | token cap | model routing | alerts
```

**8. Complete the risk table for unsupported answers, unauthorized evidence, unsafe content, excessive agency, prompt injection and sensitive traces.**

```text
Evidence: groundedness check | permission test | content-filter result | approval record | trace review
```

**9. Assign an owner and release evidence to every decision, complete the checklist, mark the ADR Proposed and update evidence/manifest.md.**

```text
Owners: Product | AI engineering | Data | Security | Operations
Checkpoint path: C926-labs/evidence/manifest.md
```

## Test It

The ADR contains the outcome and exclusions, every required service has a scenario reason, every connection names an identity, and each priority risk has a control, owner and observable release evidence.

## Troubleshooting

- **The diagram is a list of product names.** Redraw it as actors, trust boundaries, information paths and ownership; keep product selection in the decision table.
- **Every service is included by default.** Remove any service that does not satisfy a stated modality, grounding, action or operational need.
- **A control says only 'be secure'.** Replace it with a configuration, test, trace, threshold or approval record that can be inspected.

## Challenge

Add an alternative low-cost architecture that uses a smaller model for classification and the larger model only for grounded synthesis.

## Reflection

Which architecture decision most reduces the chance of a fluent but unsupported answer reaching a user?

## Checkpoint

Save C926-labs/northstar-solution-adr.md and update C926-labs/evidence/manifest.md. Lab 2 adds verified project, deployment and operations evidence to this record.

---

[← Labs index](README.md) · [Lab 2 →](lab-02-verify-foundry-access-and-the-operations-baseline.md)
