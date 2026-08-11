#!/usr/bin/env python3
"""Compare offline, keyword, vector and hybrid Azure AI Search queries."""

import argparse
import json
import os
import re
import time
from pathlib import Path
from urllib.parse import quote

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda: None


BASE = Path(__file__).resolve().parent


def offline(query):
    docs = json.loads((BASE / "search-documents.json").read_text(encoding="utf-8"))
    terms = set(re.findall(r"[a-z0-9-]+", query.lower()))
    rows = []
    for doc in docs:
        if doc["access_scope"] != "learner":
            continue
        score = len(terms & set(re.findall(r"[a-z0-9-]+", (doc["title"] + " " + doc["content"]).lower())))
        if score:
            rows.append({**doc, "score": score})
    return sorted(rows, key=lambda row: (-row["score"], row["source_id"]))[:5]


def live(query, mode, semantic):
    import requests
    load_dotenv()
    endpoint = os.environ["AZURE_SEARCH_ENDPOINT"].rstrip("/")
    index = os.environ["AZURE_SEARCH_INDEX"]
    vector_field = os.getenv("AZURE_SEARCH_VECTOR_FIELD", "content_vector")
    semantic_config = os.getenv("AZURE_SEARCH_SEMANTIC_CONFIG", "")
    url = f"{endpoint}/indexes/{quote(index, safe='')}/docs/search?api-version=2026-04-01"
    payload = {
        "select": "id,title,content,source_id,category,effective_date,access_scope",
        "filter": "category eq 'device-support' and access_scope eq 'learner'",
        "top": 5,
        "count": True,
    }
    if mode in {"keyword", "hybrid"}:
        payload["search"] = query
    else:
        payload["search"] = "*"
    if mode in {"vector", "hybrid"}:
        payload["vectorQueries"] = [{"kind": "text", "text": query, "fields": vector_field, "k": 5}]
    if semantic:
        if not semantic_config or "<" in semantic_config:
            raise ValueError("AZURE_SEARCH_SEMANTIC_CONFIG must be set for --semantic")
        payload.update({"queryType": "semantic", "semanticConfiguration": semantic_config})
    headers = {"Content-Type": "application/json"}
    api_key = os.getenv("SEARCH_API_KEY", "")
    if api_key and "<" not in api_key:
        headers["api-key"] = api_key
    else:
        from azure.identity import DefaultAzureCredential
        headers["Authorization"] = "Bearer " + DefaultAzureCredential().get_token("https://search.azure.com/.default").token
    started = time.perf_counter()
    response = requests.post(url, headers=headers, json=payload, timeout=60)
    elapsed = round((time.perf_counter() - started) * 1000)
    response.raise_for_status()
    body = response.json()
    rows = []
    for item in body.get("value", []):
        rows.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "content": item.get("content"),
            "source_id": item.get("source_id"),
            "category": item.get("category"),
            "effective_date": item.get("effective_date"),
            "access_scope": item.get("access_scope"),
            "score": item.get("@search.score"),
            "reranker_score": item.get("@search.rerankerScore"),
        })
    return rows, elapsed, body.get("@odata.count")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--mode", choices=["keyword", "vector", "hybrid"], default="hybrid")
    parser.add_argument("--semantic", action="store_true")
    parser.add_argument("--query", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    if args.offline:
        rows, elapsed, count = offline(args.query), 0, None
        mode = "offline-keyword"
    else:
        rows, elapsed, count = live(args.query, args.mode, args.semantic)
        mode = args.mode
    if any(row.get("access_scope") != "learner" for row in rows):
        raise RuntimeError("Access filter violation: a non-learner document was returned")
    report = {"mode": mode, "semantic": args.semantic, "query": args.query, "latency_ms": elapsed, "count": count, "results": rows}
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
