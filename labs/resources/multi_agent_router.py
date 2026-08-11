#!/usr/bin/env python3
"""Deterministic contract-routing simulator for C926 Lab 5."""

import argparse
import json
from pathlib import Path

import yaml


def route(query, contracts):
    q = query.lower()
    if any(term.lower() in q for term in contracts["orchestrator"].get("deny_terms", [])):
        return "decline", "The request is outside all specialist boundaries."
    matches = []
    for specialist in contracts["specialists"]:
        terms = [str(term).lower() for term in specialist.get("routing_terms", [])]
        matched = sorted(term for term in terms if term in q)
        if matched:
            matches.append((specialist["name"], matched))
    if len(matches) > 1:
        return "ambiguous", "More than one contract matched: " + "; ".join(f"{name}={terms}" for name, terms in matches)
    if len(matches) == 1:
        name, terms = matches[0]
        return name, f"Contract routing_terms matched: {terms}"
    return "decline", "No specialist contract covers the request."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--contracts", required=True)
    parser.add_argument("--cases", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--allow-errors", action="store_true", help="Write a baseline report without failing the process")
    args = parser.parse_args()
    contract_text = Path(args.contracts).read_text(encoding="utf-8")
    contracts = yaml.safe_load(contract_text)
    specialist_names = [item["name"] for item in contracts["specialists"]]
    max_hops = contracts["orchestrator"]["max_delegation_hops"]
    for specialist in contracts["specialists"]:
        missing = [key for key in ["description", "routing_terms", "required_context", "returns", "tools", "timeout_seconds", "owner"] if key not in specialist]
        if missing:
            raise ValueError(f"Contract {specialist.get('name')} is missing {missing}")
    valid = set(specialist_names) | {"decline", "ambiguous"}
    rows = []
    for line in Path(args.cases).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        case = json.loads(line)
        actual, reason = route(case["query"], contracts)
        if actual not in valid:
            raise ValueError(f"Unknown route {actual}")
        rows.append({**case, "actual": actual, "correct": actual == case["expected"], "reason": reason})
    correct = sum(row["correct"] for row in rows)
    report = {
        "contracts": specialist_names,
        "max_delegation_hops": max_hops,
        "total": len(rows),
        "correct": correct,
        "accuracy": round(correct / len(rows), 3) if rows else 0,
        "cases": rows,
    }
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if correct == len(rows) or args.allow_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
