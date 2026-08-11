#!/usr/bin/env python3
"""Content Understanding prebuilt-invoice helper for C926 Lab 8."""

import argparse
import json
import os
import time
from datetime import date, datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda: None


ANALYZER_ID = "prebuilt-invoice"
INVOICE_URL = "https://raw.githubusercontent.com/Azure-Samples/azure-ai-content-understanding-assets/main/document/invoice.pdf"
EXPECTED_FIELDS = ["VendorName", "InvoiceId", "InvoiceDate", "SubTotal", "TotalTax", "InvoiceTotal", "Items"]


def plain(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return [plain(item) for item in value]
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if hasattr(value, "value"):
        return plain(value.value)
    return str(value)


def self_check():
    import importlib.util
    report = {
        "status": "ok",
        "check_scope": "static prerequisites only; live model mappings remain an instructor readiness check",
        "analyzer_id": ANALYZER_ID,
        "sample_url_https": INVOICE_URL.startswith("https://"),
        "sdk_available": importlib.util.find_spec("azure.ai.contentunderstanding") is not None,
        "foundry_endpoint_shape": "https://<foundry-resource>.services.ai.azure.com",
        "required_model_mappings": ["gpt-4.1", "text-embedding-3-large"],
        "expected_fields": EXPECTED_FIELDS,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["sdk_available"] else 2


def check_config():
    load_dotenv()
    endpoint = os.getenv("CONTENTUNDERSTANDING_ENDPOINT", "").strip().rstrip("/")
    endpoint_valid = endpoint.startswith("https://") and endpoint.endswith(".services.ai.azure.com") and "<" not in endpoint
    key = os.getenv("CONTENTUNDERSTANDING_KEY", "")
    report = {
        "status": "ok" if endpoint_valid else "failed",
        "endpoint_shape_valid": endpoint_valid,
        "credential_mode": "ephemeral_key" if key and "<" not in key else "default_azure_credential",
        "model_mapping_check": "Confirm gpt-4.1 and text-embedding-3-large default mappings in the instructor readiness record.",
    }
    print(json.dumps(report, indent=2))
    return 0 if endpoint_valid else 1


def live(out_path, markdown_path):
    load_dotenv()
    from azure.ai.contentunderstanding import ContentUnderstandingClient
    from azure.ai.contentunderstanding.models import AnalysisInput
    endpoint = os.environ["CONTENTUNDERSTANDING_ENDPOINT"]
    key = os.getenv("CONTENTUNDERSTANDING_KEY", "")
    if key and "<" not in key:
        from azure.core.credentials import AzureKeyCredential
        credential = AzureKeyCredential(key)
    else:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
    client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)
    started = time.perf_counter()
    result = client.begin_analyze(analyzer_id=ANALYZER_ID, inputs=[AnalysisInput(url=INVOICE_URL)]).result()
    latency_ms = round((time.perf_counter() - started) * 1000)
    if not result.contents:
        raise RuntimeError("No content returned by the analyzer")
    content = result.contents[0]
    fields = {}
    for name, field in (content.fields or {}).items():
        fields[name] = {
            "value": plain(field),
            "confidence": plain(getattr(field, "confidence", None)),
            "source": plain(getattr(field, "source", None)),
        }
    report = {
        "analyzer_id": ANALYZER_ID,
        "source_id": "microsoft-synthetic-invoice",
        "page_start": plain(getattr(content, "start_page_number", None)),
        "page_end": plain(getattr(content, "end_page_number", None)),
        "latency_ms": latency_ms,
        "fields": fields,
        "status": "ok",
    }
    Path(out_path).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    Path(markdown_path).write_text((getattr(content, "markdown", "") or "") + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


def sanitize(input_path, out_path):
    raw = json.loads(Path(input_path).read_text(encoding="utf-8"))
    fields = raw.get("fields", {})
    sanitized_fields = {}
    for name in EXPECTED_FIELDS:
        item = fields.get(name)
        if item is not None:
            sanitized_fields[name] = {
                "value": plain(item.get("value") if isinstance(item, dict) else item),
                "confidence": plain(item.get("confidence") if isinstance(item, dict) else None),
                "evidence": plain((item.get("source") or item.get("evidence")) if isinstance(item, dict) else None),
            }
    report = {
        "status": "sanitized",
        "analyzer_id": raw.get("analyzer_id", ANALYZER_ID),
        "source_id": raw.get("source_id", "microsoft-synthetic-invoice"),
        "page_start": raw.get("page_start"),
        "page_end": raw.get("page_end"),
        "latency_ms": raw.get("latency_ms"),
        "fields": sanitized_fields,
        "missing_expected_fields": [name for name in EXPECTED_FIELDS if name not in fields],
    }
    Path(out_path).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--check-config", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--sanitize")
    parser.add_argument("--out", default="invoice-result.json")
    parser.add_argument("--markdown", default="invoice-result.md")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    if args.check_config:
        return check_config()
    if args.sanitize:
        return sanitize(args.sanitize, args.out)
    if not args.live:
        parser.error("Use --self-check or --live")
    return live(args.out, args.markdown)


if __name__ == "__main__":
    raise SystemExit(main())
