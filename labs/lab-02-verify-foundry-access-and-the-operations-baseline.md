# Lab 2 — Verify Foundry Access and the Operations Baseline

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 1:** Plan and Manage an Azure AI Solution
- **Maps to:** LO1 - connect to a Foundry project with keyless developer authentication and record deployment, quota, cost, security and monitoring evidence.
- **Tools:** Python 3.12, Azure CLI, Microsoft Foundry, Azure AI Projects SDK, labs/resources/verify_foundry.py
- **Duration:** 60 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Create an isolated Python workspace, authenticate through Azure CLI, inspect the instructor-provided Foundry project and make one controlled Responses API call.

## What You Will Build

A verified local workspace, sanitized environment file, model response record and operations-baseline checklist linked from the ADR.

## Prerequisites

- Complete Lab 1 and keep northstar-solution-adr.md available.
- Obtain the instructor-provided Foundry project endpoint and language-model deployment name.
- Confirm Foundry User on the learner project plus Reader on the Foundry resource, as named in the readiness manifest.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. From the repository root, verify the Lab 1 workspace, enter it, create a virtual environment and install the tested lock file with that environment's interpreter.**

```text
Test-Path labs\resources\requirements-lock.txt
Test-Path C926-labs\northstar-solution-adr.md
Set-Location C926-labs
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r ..\labs\resources\requirements-lock.txt
# macOS/Linux equivalent: .venv/bin/python -m pip install -r ../labs/resources/requirements-lock.txt
```

**2. Sign in through Azure CLI and confirm the intended subscription and tenant; do not capture tokens in your evidence file.**

```text
az login
az account show --query '{subscription:name, tenant:tenantId, user:user.name}' -o table
```

**3. Copy the environment template, fill only FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_MODEL_NAME, and confirm .env is ignored by Git.**

```text
Copy-Item ..\labs\resources\.env.example .env
git check-ignore .env
```

**4. Run the supplied verifier first in configuration-only mode and save the sanitized output.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\verify_foundry.py --check-only > evidence\foundry-check.txt
```

**5. Run the live verifier. If the project or trace view is unavailable, copy the named sanitized rejoin output and record that limitation.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\verify_foundry.py --live > evidence\foundry-live.txt
# Rejoin: Copy-Item ..\labs\resources\foundry-verifier-rejoin.json evidence\foundry-verifier-rejoin.json
```

**6. In the Foundry portal, locate the selected deployment and record model name, deployment name, region, version or upgrade policy and capacity unit without recording credentials.**

```text
Record in northstar-solution-adr.md under Deployment evidence.
```

**7. Locate quota or usage, cost management and project access controls; record the limit, alert owner and least-privilege role used by the lab.**

```text
Evidence fields: quota surface | budget alert | project role | owner | review date
```

**8. Open Observability or Traces once and record the visible trace or timestamp, token and latency fields. If propagation is delayed, use the named rejoin file and record the delay instead of waiting.**

```text
Expected: one model operation associated with the lab call. Rejoin: evidence/foundry-verifier-rejoin.json.
```

**9. Append the endpoint shape, deployment evidence, operations owner and trace reference to the ADR, then link the evidence in evidence/manifest.md; never paste a key or token.**

```text
Endpoint shape: https://<resource>.services.ai.azure.com/api/projects/<project>
```

## Test It

The check-only run reports valid configured values, the live run prints a non-empty response and deployment list, and the ADR contains sanitized deployment, quota, identity, cost and trace evidence.

## Troubleshooting

- **DefaultAzureCredential cannot authenticate.** Run az account show, confirm the intended tenant, then use az login --tenant <TENANT_ID> and retry.
- **The project returns 403.** Ask the instructor to verify the exact project role and scope; do not substitute an API key into source code.
- **The model call returns deployment not found.** Use the deployment name shown in the Foundry project's deployed models table, not the catalog model ID.

## Challenge

Run the bounded prompt against a second approved deployment and compare latency, response length and task fit without changing the task prompt.

## Reflection

Which operational field would tell you first that the solution is becoming unreliable: error rate, latency, token use, safety events or groundedness, and why?

## Checkpoint

Keep the foundry evidence in C926-labs/evidence, revise the ADR and update evidence/manifest.md. Lab 3 reuses the same project endpoint and model deployment.

---

[← Lab 1](lab-01-design-the-northstar-foundry-solution.md) · [Lab 3 →](lab-03-build-and-test-a-grounded-generative-app.md)
