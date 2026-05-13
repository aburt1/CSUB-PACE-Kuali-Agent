#!/usr/bin/env python3
"""Summarize Kuali app/form/workflow/permissions JSON for review."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def walk_form(node, sections, fields):
    if isinstance(node, dict):
        if node.get("type") == "Section":
            sections.append({"id": node.get("id"), "label": node.get("label")})
        if node.get("formKey"):
            fields.append(
                {
                    "id": node.get("id"),
                    "label": node.get("label"),
                    "type": node.get("type"),
                    "formKey": node.get("formKey"),
                    "required": node.get("required"),
                }
            )
        for child in node.get("children") or []:
            walk_form(child, sections, fields)
    elif isinstance(node, list):
        for item in node:
            walk_form(item, sections, fields)


def summarize(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    data = obj.get("data", obj)
    app = data.get("app", data) if isinstance(data, dict) else data
    summary = {"source": str(path)}

    if isinstance(app, dict):
        summary["id"] = app.get("id")
        summary["name"] = app.get("name")
        summary["published"] = app.get("isPublished") or app.get("published")

        workflow = app.get("workflow")
        if workflow:
            summary["workflow"] = {
                "status": workflow.get("status"),
                "steps": [
                    {
                        "name": step.get("stepName"),
                        "type": step.get("type"),
                        "assignee": (step.get("assignee") or {}).get("type"),
                    }
                    for step in workflow.get("steps") or []
                ],
            }

        if "listPolicyGroups" in app:
            summary["permission_groups"] = [
                {
                    "name": group.get("name"),
                    "identities": [i.get("label") for i in group.get("identities") or []],
                    "actions": [
                        action
                        for policy in group.get("policies") or []
                        for statement in policy.get("statements") or []
                        for action in statement.get("action") or []
                    ],
                }
                for group in app.get("listPolicyGroups") or []
            ]

    sections, fields = [], []
    walk_form(obj, sections, fields)
    if sections or fields:
        summary["sections"] = sections
        summary["fields"] = fields

    print(json.dumps(summary, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", nargs="+")
    args = parser.parse_args()
    for file_name in args.json_file:
        summarize(Path(file_name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
