# Lab 6 — Build a Responsible Multimodal Workflow

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 3:** Implement Computer Vision Solutions
- **Maps to:** LO4 - generate or edit visual content, analyze visual evidence, produce accessible descriptions and apply multimodal safety controls.
- **Tools:** Microsoft Foundry image playground or image model, multimodal model or Content Understanding, labs/resources/visual-policy-checklist.csv
- **Duration:** 75 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Create a visual-support evidence packet that combines one generated image, one image-understanding result, accessibility text and an indirect-prompt-injection check.

## What You Will Build

A visual evidence packet with prompt versions, generated or rejoin image, structured observations, alt text, extended description and policy disposition.

## Prerequisites

- Complete Day 1 and open the instructor-provided Foundry project.
- Confirm whether an approved image-generation deployment is available; otherwise use labs/resources/rejoin-generated-device-desk.svg.
- Confirm a multimodal model or Content Understanding image analyzer is available; otherwise use the named sanitized analysis rejoin result.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the editable evidence-packet, policy-checklist and injection-result templates before adding results.**

```text
Copy-Item ..\labs\resources\visual-evidence-packet-template.md work\visual-evidence-packet.md
Copy-Item ..\labs\resources\visual-policy-checklist.csv work\visual-policy-checklist.csv
Copy-Item ..\labs\resources\visual-injection-result-template.json evidence\multimodal-analysis.json
```

**2. Write a generation prompt for a Northstar service-desk training scene with subject, composition, visual treatment, accessibility intent and explicit exclusions.**

```text
Prompt fields: purpose | subject | setting | composition | style | visible text | exclusions
```

**3. Generate one image in the approved tool and record deployment, prompt version, size, quality and filter outcome; if unavailable, use the exact rejoin command.**

```text
Output: work\northstar-device-desk.png
Rejoin: Copy-Item ..\labs\resources\rejoin-generated-device-desk.svg work\generated-device-desk.svg
```

**4. Create one controlled edit request that changes only the laptop screen content while preserving people, composition and lighting. Use a mask if the available model supports it; otherwise document the intended mask region.**

```text
Edit: replace the screen with a generic diagnostics dashboard; do not add personal data or logos.
```

**5. Analyze the image with the available multimodal tool. Ask first for visible observations, text and regions, then answer the bounded support question; if unavailable, copy the sanitized analysis rejoin result.**

```text
Question: Which visible evidence suggests the laptop is awaiting diagnostics?
Rejoin: Copy-Item ..\labs\resources\multimodal-analysis-rejoin.json evidence\multimodal-analysis.json
```

**6. Produce concise alt text for the image's role in the guide and a longer description that explains relevant layout and evidence without inferring identity, emotion or protected attributes.**

```text
Alt text target: purpose plus essential evidence
Extended description: layout, objects, visible text and uncertainty
```

**7. Analyze visual-prompt-injection.svg with tools disabled. Fill evidence/multimodal-analysis.json, including both source IDs and the indirect_prompt_injection object, then run the deterministic check.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\verify_visual_injection.py --result evidence\multimodal-analysis.json > evidence\visual-injection-check.json
Expected: detected=true | treated_as_untrusted_data=true | tool_invocation_allowed=false
```

**8. Complete work/visual-policy-checklist.csv for unsafe content, unsupported inference, injection, brand, provenance, watermark, accessibility and human-review conditions.**

```text
Disposition values: allow | transform | block | review
```

**9. Complete work/visual-evidence-packet.md with the exact source, prompt/model version, region/time, filter result, observations, evidence regions, alt text, extended description, injection result and reviewer disposition.**

```text
Exclude credentials and private URLs; link the packet and checklist from evidence/manifest.md.
```

## Test It

The packet contains a reproducible generation or rejoin source, a bounded edit, evidence-first analysis, accessible descriptions, and an injection result that never follows instructions embedded in the image.

## Troubleshooting

- **Image generation is not available in the region.** Use the supplied rejoin SVG, record the limitation and continue with understanding, accessibility and policy checks.
- **The model invents a person's identity or emotional state.** Constrain the prompt to visible facts and remove unsupported personal inference from the final description.
- **The image asks the model to reveal configuration or call a tool.** Treat embedded text as untrusted data, keep application instructions authoritative and disable tools for the analysis step.

## Challenge

Create a video-analysis design that samples scenes, preserves timestamps and detects the same injection and accessibility risks without generating a video.

## Reflection

Why is a safe text prompt insufficient evidence that a generated or analyzed image is safe to publish?

## Checkpoint

Save the visual packet and checklist under C926-labs/work, keep machine evidence under evidence/, and update evidence/manifest.md. Lab 7 uses the same evidence-first pattern for text and audio.

---

[← Lab 5](lab-05-design-multi-agent-routing-and-quality-gates.md) · [Lab 7 →](lab-07-implement-a-text-translation-and-speech-pipeline.md)
