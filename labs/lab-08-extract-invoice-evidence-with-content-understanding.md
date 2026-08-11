# Lab 8 — Extract Invoice Evidence with Content Understanding

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 5:** Implement Information Extraction Solutions
- **Maps to:** LO6 - use OCR, layout and a Content Understanding analyzer to produce structured, grounded document fields.
- **Tools:** Python, Azure Content Understanding SDK, prebuilt-invoice analyzer, labs/resources/content_understanding_invoice.py
- **Duration:** 90 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Run the prebuilt invoice analyzer on a Microsoft synthetic sample, inspect markdown and fields, and validate business-critical values against source evidence.

## What You Will Build

A sanitized Content Understanding result, extracted invoice table, field-validation log and custom-analyzer design note.

## Prerequisites

- Complete Lab 7 and activate the C926-labs Python environment.
- Confirm a Foundry resource endpoint and the default `gpt-4.1` and `text-embedding-3-large` model mappings required by prebuilt-invoice.
- Confirm Cognitive Services User on the Foundry resource for your Entra principal, or obtain an ephemeral instructor key; store values only in the local environment.
- Use the Microsoft synthetic invoice URL already declared in the supplied script.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the editable validation template and run the static self-check for SDK availability, analyzer ID, sample URL, expected fields and documented model-mapping prerequisites.**

```text
Copy-Item ..\labs\resources\invoice-field-validation.csv work\invoice-field-validation.csv
.\.venv\Scripts\python.exe ..\labs\resources\content_understanding_invoice.py --self-check
```

**2. Set the endpoint and optional ephemeral key with executable PowerShell assignments, then validate the configured endpoint shape. Instructor readiness separately confirms the live model mappings.**

```text
$env:CONTENTUNDERSTANDING_ENDPOINT="https://<foundry-resource>.services.ai.azure.com"
# Only when required: $env:CONTENTUNDERSTANDING_KEY="<private-training-value>"
.\.venv\Scripts\python.exe ..\labs\resources\content_understanding_invoice.py --check-config
```

**3. Run prebuilt-invoice analysis and preserve the raw JSON and markdown locally. If the analyzer is unavailable, copy the named sanitized rejoin result and continue at source validation.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\content_understanding_invoice.py --live --out evidence\invoice-result.json --markdown evidence\invoice-result.md
# Rejoin: Copy-Item ..\labs\resources\content-understanding-invoice-rejoin.json evidence\invoice-result-sanitized.json
```

**4. Download the Microsoft synthetic invoice to work/, render or open page 1 locally, and locate VendorName, InvoiceId, InvoiceDate, SubTotal, TotalTax, InvoiceTotal and Items in the source and result.**

```text
Invoke-WebRequest 'https://raw.githubusercontent.com/Azure-Samples/azure-ai-content-understanding-assets/main/document/invoice.pdf' -OutFile work\invoice.pdf
Start-Process work\invoice.pdf
```

**5. Complete work/invoice-field-validation.csv with extracted value, source value, page/region evidence, confidence and disposition.**

```text
Disposition: accept | correct | review | missing
```

**6. Check arithmetic consistency across line items, subtotal, tax and total. Record mismatches as validation defects rather than modifying the raw analyzer result.**

```text
subtotal + tax = total; preserve currency and decimal precision
```

**7. On the live path, create the shareable sanitized result with the supplied command. On the rejoin path, retain the already-sanitized supplied file and do not run this command without a raw result.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\content_understanding_invoice.py --sanitize evidence\invoice-result.json --out evidence\invoice-result-sanitized.json
```

**8. Design work/custom-invoice-analyzer.md with three additional fields and explicit descriptions; do not deploy it in this time-box.**

```text
Suggested: support_request_id | asset_tag | service_category
```

**9. Record latency, missing and low-confidence fields, review threshold and evidence links in the ADR, then update evidence/manifest.md.**

```text
A syntactically valid field can still be wrong; evidence review remains required.
```

## Test It

The prebuilt analyzer returns document content, seven critical field groups are checked against source evidence, arithmetic is reconciled, and uncertain or missing values are routed to review rather than silently accepted.

## Troubleshooting

- **The SDK cannot import.** Reinstall azure-ai-contentunderstanding in the active virtual environment and verify the interpreter used by python.
- **The operation returns unauthorized.** Verify endpoint resource, environment variable scope and the instructor-provided role or key; never hard-code the key.
- **A field value exists but has no trustworthy evidence.** Mark it review and preserve the raw content, page and field path for a person.

## Challenge

Add a validation rule that detects duplicate invoice IDs across two sanitized results without storing the original documents.

## Reflection

Which extracted fields can be accepted automatically, and what evidence threshold justifies that choice?

## Checkpoint

Save sanitized invoice evidence under C926-labs/evidence, editable validation/design files under work/, and update the ADR and evidence/manifest.md. Lab 9 indexes clean representations and tests grounded retrieval.

---

[← Lab 7](lab-07-implement-a-text-translation-and-speech-pipeline.md) · [Lab 9 →](lab-09-build-and-verify-a-hybrid-grounding-pipeline.md)
