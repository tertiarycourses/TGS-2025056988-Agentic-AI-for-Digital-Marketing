# Lab 7 — Implement a Text, Translation and Speech Pipeline

- **Course:** AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)
- **Topic 4:** Implement Text Analysis Solutions
- **Maps to:** LO5 - extract structured text signals, translate approved content and integrate speech input with explicit evidence and error handling.
- **Tools:** Python, Microsoft Foundry Responses API, Azure Speech SDK, Azure Translator SDK, labs/resources/text_speech_pipeline.py
- **Duration:** 75 minutes
- **Version:** v1.0 — 11 August 2026

---

## Goal

Process a synthetic Northstar support call from transcript or audio into structured JSON, translate the customer-facing summary and preserve timing and uncertainty evidence.

## What You Will Build

A validated support-call JSON record, translated summary, speech evidence record and language-quality review.

## Prerequisites

- Complete Lab 6 and activate the C926-labs Python environment.
- Choose at most one live optional service path (Speech or Translator) inside the 75-minute lab; use the named rejoin/design path for the other.
- Keep editable transcript, schema and review files under C926-labs/work.

> **Data note.** Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control.

## Steps

**1. Copy the transcript, schema and translation-review template into work/, then inspect required fields, enums, evidence, language, processing metadata and uncertainty.**

```text
Copy-Item ..\labs\resources\northstar-call-transcript.txt work\northstar-call-transcript.txt
Copy-Item ..\labs\resources\support-call-schema.json work\support-call-schema.json
Copy-Item ..\labs\resources\translation-review-template.csv work\translation-review.csv
```

**2. Run offline extraction and validate the final serialized record against the copied schema before any service call.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\text_speech_pipeline.py --transcript work\northstar-call-transcript.txt --schema work\support-call-schema.json --offline --out evidence\call-offline.json
```

**3. Run the live Foundry extraction. Require JSON only, preserve evidence and use null or uncertainty when the transcript does not support a field.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\text_speech_pipeline.py --transcript work\northstar-call-transcript.txt --schema work\support-call-schema.json --foundry --out evidence\call-foundry.json
```

**4. Compare the sentiment signal with the evidence sentence. Record why the label is a routing signal rather than a fact about the caller's intent or character.**

```text
Review: mixed sentiment | sarcasm | short utterance | domain language | confidence
```

**5. For the Speech path, save recognized text, result status, offset and duration. If unavailable or not selected, copy the named rejoin result.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\text_speech_pipeline.py --audio <INSTRUCTOR_WAV_PATH> --speech --out evidence\call-speech.json
# Rejoin: Copy-Item ..\labs\resources\speech-rejoin-result.json evidence\call-speech.json
```

**6. For the Translator path, translate the summary and revalidate the final record including translation metadata. If unavailable or not selected, perform the design review in work/translation-review.csv.**

```text
.\.venv\Scripts\python.exe ..\labs\resources\text_speech_pipeline.py --input-json evidence\call-foundry.json --schema work\support-call-schema.json --translate-to <LANGUAGE_CODE> --out evidence\call-translated.json
```

**7. Back-translate or bilingual-review the summary in work/translation-review.csv and record terminology, identifier, number, tone and unsupported-addition defects.**

```text
Review fields: source_text | target_locale | translated_text | back_translation | terminology_check | numbers_names_check | disposition
```

**8. Map success, no-match, cancelled, unsupported language, throttled and service-unavailable states to user-safe messages and a correlation ID.**

```text
Never display raw keys, tokens, request headers or full service error bodies.
```

**9. Save the evidence summary in work/text-audio-evidence.md, link every artifact from evidence/manifest.md and add the text/audio checkpoint to the ADR.**

```text
Keep synthetic transcript evidence; do not add real call recordings.
```

## Test It

The output validates against the supplied schema, every extracted conclusion has transcript evidence or uncertainty, the speech path records a success or named rejoin state, and the translated summary preserves identifiers and critical facts.

## Troubleshooting

- **The model fills a missing field with a plausible value.** Require null plus an uncertainty entry, then reject any output whose evidence does not contain the value.
- **Speech returns NoMatch.** Check audio format, language and signal level; use the supplied transcript to rejoin while preserving the failure record.
- **Translation changes an identifier or number.** Protect tokens before translation or validate and restore them afterward; escalate material changes for review.

## Challenge

Add a second transcript with code-switching and define how language identification and terminology review should change.

## Reflection

Which fields can safely automate routing, and which should remain advisory because the evidence is probabilistic?

## Checkpoint

Save validated call, speech and translation evidence under C926-labs, then update the ADR and evidence/manifest.md. Lab 8 extracts structured evidence from a document with Content Understanding.

---

[← Lab 6](lab-06-build-a-responsible-multimodal-workflow.md) · [Lab 8 →](lab-08-extract-invoice-evidence-with-content-understanding.md)
