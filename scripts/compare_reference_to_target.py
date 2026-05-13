#!/usr/bin/env python3
"""Compare Kuali form outline/template JSON files by section and field labels."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def collect(node):
    sections = []
    fields = []

    def walk(value):
        if isinstance(value, dict):
            kind = value.get("type")
            label = value.get("label")
            if kind == "Section":
                sections.append(label or "(unlabeled)")
            if value.get("formKey"):
                fields.append(
                    {
                        "label": label or "(unlabeled)",
                        "type": kind or "",
                        "formKey": value.get("formKey"),
                        "required": value.get("required"),
                    }
                )
            for child in value.get("children") or []:
                walk(child)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(node)
    return sections, fields


def load(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference_json")
    parser.add_argument("target_json")
    args = parser.parse_args()

    ref_sections, ref_fields = collect(load(args.reference_json))
    tgt_sections, tgt_fields = collect(load(args.target_json))

    ref_field_labels = {f["label"] for f in ref_fields}
    tgt_field_labels = {f["label"] for f in tgt_fields}

    result = {
        "reference_sections": ref_sections,
        "target_sections": tgt_sections,
        "common_field_labels": sorted(ref_field_labels & tgt_field_labels),
        "reference_only_field_labels": sorted(ref_field_labels - tgt_field_labels),
        "target_only_field_labels": sorted(tgt_field_labels - ref_field_labels),
        "reference_field_count": len(ref_fields),
        "target_field_count": len(tgt_fields),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
