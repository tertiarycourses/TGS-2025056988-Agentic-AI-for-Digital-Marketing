#!/usr/bin/env python3
"""Validate C926 Foundry configuration and make one bounded Responses API call."""

import argparse
import json
import os
import platform
import sys
from urllib.parse import urlparse

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda: None


def configuration():
    load_dotenv()
    endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "")
    model = os.getenv("FOUNDRY_MODEL_NAME", "")
    problems = []
    parsed = urlparse(endpoint)
    if parsed.scheme != "https" or "/api/projects/" not in parsed.path:
        problems.append("FOUNDRY_PROJECT_ENDPOINT must be an HTTPS Foundry project endpoint containing /api/projects/.")
    if not model or "<" in model or ">" in model:
        problems.append("FOUNDRY_MODEL_NAME must be the deployed model name, not a placeholder or catalog ID.")
    return endpoint, model, problems


def check_only():
    endpoint, model, problems = configuration()
    report = {
        "mode": "check-only",
        "python": platform.python_version(),
        "endpoint_host": urlparse(endpoint).hostname or "not-set",
        "endpoint_has_project_path": "/api/projects/" in endpoint,
        "model_deployment": model or "not-set",
        "status": "ok" if not problems else "needs_configuration",
        "problems": problems,
    }
    print(json.dumps(report, indent=2))
    return 0 if not problems else 2


def live():
    endpoint, model, problems = configuration()
    if problems:
        print(json.dumps({"status": "needs_configuration", "problems": problems}, indent=2))
        return 2
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential

    with DefaultAzureCredential() as credential, AIProjectClient(endpoint=endpoint, credential=credential) as project:
        deployments = []
        for item in project.deployments.list():
            deployments.append({
                "name": getattr(item, "name", None),
                "model_name": getattr(item, "model_name", None),
                "model_version": getattr(item, "model_version", None),
            })
        with project.get_openai_client() as client:
            response = client.responses.create(
                model=model,
                input=(
                    "Return exactly one short sentence confirming that the Northstar C926 "
                    "Foundry connection works. Do not use tools or external knowledge."
                ),
                max_output_tokens=80,
            )
        report = {
            "mode": "live",
            "status": "ok",
            "endpoint_host": urlparse(endpoint).hostname,
            "selected_deployment": model,
            "visible_deployments": deployments,
            "response_id": getattr(response, "id", None),
            "response_text": getattr(response, "output_text", "").strip(),
        }
        print(json.dumps(report, indent=2))
        return 0 if report["response_text"] else 3


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check-only", action="store_true")
    group.add_argument("--live", action="store_true")
    args = parser.parse_args()
    return live() if args.live else check_only()


if __name__ == "__main__":
    sys.exit(main())
