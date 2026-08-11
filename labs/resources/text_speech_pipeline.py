#!/usr/bin/env python3
"""Structured text, optional Speech, and optional Translator paths for C926 Lab 7."""

import argparse
import json
import os
import re
from pathlib import Path

try:
    from jsonschema import validate as jsonschema_validate
except ImportError:
    jsonschema_validate = None

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda: None


def offline_extract(text):
    request = re.search(r"\bNS-\d{4}\b", text)
    asset = re.search(r"\bNST-LT-\d{4}\b", text)
    diag = re.search(r"\bDIAG-\d+\b", text)
    return {
        "request_id": request.group(0) if request else None,
        "summary": "Synthetic caller reports a laptop startup failure after an update and requests a reviewed escalation draft.",
        "entities": {
            "asset_tag": asset.group(0) if asset else None,
            "diagnostic_reference": diag.group(0) if diag else None,
            "time_constraint": "presentation at three" if "presentation at three" in text.lower() else None,
        },
        "sentiment_signal": "negative" if "frustrated" in text.lower() else "uncertain",
        "urgency": "High" if "core" not in text.lower() and "presentation" in text.lower() else "Uncertain",
        "evidence": [line for line in text.splitlines() if "frustrated" in line.lower() or "DIAG-" in line][:2],
        "source_language": "en-US",
        "translated_summary": None,
        "uncertainty": ["Urgency is advisory until impact and workaround are reviewed."],
    }


def model_extract(text, schema):
    load_dotenv()
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    model = os.environ["FOUNDRY_MODEL_NAME"]
    prompt = f"""Extract a structured support-call record from the synthetic transcript.
Return JSON only and follow this schema: {json.dumps(schema)}
Use an evidence quote for each important conclusion. Use null or an uncertainty entry when unsupported.
Sentiment is only a routing signal. Do not infer identity, character or protected attributes.

TRANSCRIPT
{text}
END TRANSCRIPT
"""
    with DefaultAzureCredential() as credential, AIProjectClient(endpoint=endpoint, credential=credential) as project:
        with project.get_openai_client() as client:
            response = client.responses.create(model=model, input=prompt, max_output_tokens=900)
    raw = response.output_text.strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I | re.S)
    return json.loads(raw[raw.find("{") : raw.rfind("}") + 1])


def speech_recognize(audio_path):
    import azure.cognitiveservices.speech as speechsdk
    key = os.environ["SPEECH_KEY"]
    endpoint = os.environ["SPEECH_ENDPOINT"]
    config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)
    config.speech_recognition_language = "en-US"
    audio = speechsdk.audio.AudioConfig(filename=str(audio_path))
    result = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio).recognize_once_async().get()
    duration = getattr(result, "duration", None)
    if hasattr(duration, "total_seconds"):
        duration = int(duration.total_seconds() * 10_000_000)
    return {
        "mode": "speech",
        "reason": str(result.reason),
        "text": result.text or "",
        "result_id": getattr(result, "result_id", None),
        "offset_ticks": getattr(result, "offset", None),
        "duration_ticks": duration,
        "locale": "en-US",
    }


def translate_record(record, target):
    from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
    from azure.ai.translation.text.models import InputTextItem
    client = TextTranslationClient(
        endpoint=os.getenv("TRANSLATOR_ENDPOINT", "https://api.cognitive.microsofttranslator.com"),
        credential=TranslatorCredential(os.environ["TRANSLATOR_KEY"], os.environ["TRANSLATOR_REGION"]),
    )
    response = client.translate(content=[InputTextItem(text=record["summary"])], to=[target], from_parameter="en")
    record["translated_summary"] = response[0].translations[0].text
    record.setdefault("processing", {"validation": "schema_ok"})["translation_target"] = target
    return record


def validate_record(record, schema):
    if jsonschema_validate:
        jsonschema_validate(instance=record, schema=schema)
        return
    missing = [key for key in schema.get("required", []) if key not in record]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")
    if record.get("urgency") not in {"Low", "Normal", "High", "Critical", "Uncertain"}:
        raise ValueError("Invalid urgency")
    if record.get("sentiment_signal") not in {"positive", "neutral", "negative", "mixed", "uncertain"}:
        raise ValueError("Invalid sentiment_signal")


def write(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript")
    parser.add_argument("--schema", default=str(Path(__file__).with_name("support-call-schema.json")))
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--foundry", action="store_true")
    parser.add_argument("--audio")
    parser.add_argument("--speech", action="store_true")
    parser.add_argument("--input-json")
    parser.add_argument("--translate-to")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    if args.speech:
        if not args.audio:
            parser.error("--speech requires --audio")
        data = speech_recognize(args.audio)
    elif args.translate_to:
        if not args.input_json:
            parser.error("--translate-to requires --input-json")
        schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
        data = translate_record(json.loads(Path(args.input_json).read_text(encoding="utf-8")), args.translate_to)
        validate_record(data, schema)
    else:
        if not args.transcript or not (args.offline or args.foundry):
            parser.error("Provide --transcript with --offline or --foundry")
        text = Path(args.transcript).read_text(encoding="utf-8")
        schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
        data = model_extract(text, schema) if args.foundry else offline_extract(text)
        data["processing"] = {"validation": "schema_ok", "translation_target": None}
        validate_record(data, schema)
    write(args.out, data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
