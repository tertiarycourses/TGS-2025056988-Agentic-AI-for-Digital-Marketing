"""Domain 4 - Implement text analysis solutions. Lab 7."""

from data_domain1 import lab


DOMAIN4 = [
    lab(
        7,
        4,
        "Implement a Text, Translation and Speech Pipeline",
        "LO5 - extract structured text signals, translate approved content and integrate speech input with explicit evidence and error handling.",
        "Process a synthetic Northstar support call from transcript or audio into structured JSON, translate the customer-facing summary and preserve timing and uncertainty evidence.",
        "A validated support-call JSON record, translated summary, speech evidence record and language-quality review.",
        "Python, Microsoft Foundry Responses API, Azure Speech SDK, Azure Translator SDK, labs/resources/text_speech_pipeline.py",
        "75 minutes",
        [
            "Complete Lab 6 and activate the C926-labs Python environment.",
            "Choose at most one live optional service path (Speech or Translator) inside the 75-minute lab; use the named rejoin/design path for the other.",
            "Keep editable transcript, schema and review files under C926-labs/work.",
        ],
        [
            ("Copy the transcript, schema and translation-review template into work/, then inspect required fields, enums, evidence, language, processing metadata and uncertainty.", "Copy-Item ..\\labs\\resources\\northstar-call-transcript.txt work\\northstar-call-transcript.txt\nCopy-Item ..\\labs\\resources\\support-call-schema.json work\\support-call-schema.json\nCopy-Item ..\\labs\\resources\\translation-review-template.csv work\\translation-review.csv"),
            ("Run offline extraction and validate the final serialized record against the copied schema before any service call.", ".\\.venv\\Scripts\\python.exe ..\\labs\\resources\\text_speech_pipeline.py --transcript work\\northstar-call-transcript.txt --schema work\\support-call-schema.json --offline --out evidence\\call-offline.json"),
            ("Run the live Foundry extraction. Require JSON only, preserve evidence and use null or uncertainty when the transcript does not support a field.", ".\\.venv\\Scripts\\python.exe ..\\labs\\resources\\text_speech_pipeline.py --transcript work\\northstar-call-transcript.txt --schema work\\support-call-schema.json --foundry --out evidence\\call-foundry.json"),
            ("Compare the sentiment signal with the evidence sentence. Record why the label is a routing signal rather than a fact about the caller's intent or character.", "Review: mixed sentiment | sarcasm | short utterance | domain language | confidence"),
            ("For the Speech path, save recognized text, result status, offset and duration. If unavailable or not selected, copy the named rejoin result.", ".\\.venv\\Scripts\\python.exe ..\\labs\\resources\\text_speech_pipeline.py --audio <INSTRUCTOR_WAV_PATH> --speech --out evidence\\call-speech.json\n# Rejoin: Copy-Item ..\\labs\\resources\\speech-rejoin-result.json evidence\\call-speech.json"),
            ("For the Translator path, translate the summary and revalidate the final record including translation metadata. If unavailable or not selected, perform the design review in work/translation-review.csv.", ".\\.venv\\Scripts\\python.exe ..\\labs\\resources\\text_speech_pipeline.py --input-json evidence\\call-foundry.json --schema work\\support-call-schema.json --translate-to <LANGUAGE_CODE> --out evidence\\call-translated.json"),
            ("Back-translate or bilingual-review the summary in work/translation-review.csv and record terminology, identifier, number, tone and unsupported-addition defects.", "Review fields: source_text | target_locale | translated_text | back_translation | terminology_check | numbers_names_check | disposition"),
            ("Map success, no-match, cancelled, unsupported language, throttled and service-unavailable states to user-safe messages and a correlation ID.", "Never display raw keys, tokens, request headers or full service error bodies."),
            ("Save the evidence summary in work/text-audio-evidence.md, link every artifact from evidence/manifest.md and add the text/audio checkpoint to the ADR.", "Keep synthetic transcript evidence; do not add real call recordings."),
        ],
        "The output validates against the supplied schema, every extracted conclusion has transcript evidence or uncertainty, the speech path records a success or named rejoin state, and the translated summary preserves identifiers and critical facts.",
        [
            ("The model fills a missing field with a plausible value.", "Require null plus an uncertainty entry, then reject any output whose evidence does not contain the value."),
            ("Speech returns NoMatch.", "Check audio format, language and signal level; use the supplied transcript to rejoin while preserving the failure record."),
            ("Translation changes an identifier or number.", "Protect tokens before translation or validate and restore them afterward; escalate material changes for review."),
        ],
        "Add a second transcript with code-switching and define how language identification and terminology review should change.",
        "Which fields can safely automate routing, and which should remain advisory because the evidence is probabilistic?",
        "Save validated call, speech and translation evidence under C926-labs, then update the ADR and evidence/manifest.md. Lab 8 extracts structured evidence from a document with Content Understanding.",
        ["Validate the output schema", "Extract with evidence and uncertainty", "Add speech and translation paths", "Review language quality and errors"],
    ),
]
