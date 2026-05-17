#!/usr/bin/env python3
"""Basic Agent Skills / Hermes skill validator.

This intentionally uses only Python standard library modules. It performs
lightweight checks that catch common packaging mistakes:
- SKILL.md exists
- YAML-like frontmatter exists
- name and description exist
- name matches the parent folder
- name follows the common Agent Skills identifier rules
- referenced files from the bundled Greek grammar skill exist

It is not a full YAML parser and does not replace `skills-ref validate`.
"""

from __future__ import annotations

import pathlib
import re
import sys
from typing import Dict, Tuple

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_REFERENCES = [
    "references/QUICK_TABLES.md",
    "references/ORTHOGRAPHY_AND_ACCENTS.md",
    "references/NOUNS_ADJECTIVES_PRONOUNS.md",
    "references/VERBS_AND_ASPECT.md",
    "references/SYNTAX_USAGE_STYLE.md",
    "references/ERROR_PATTERNS_AND_FEEDBACK.md",
    "assets/exercise_templates.md",
]


def split_frontmatter(text: str) -> Tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md is missing the closing --- frontmatter delimiter")
    return text[4:end], text[end + 5 :]


def parse_simple_frontmatter(frontmatter: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate(root: pathlib.Path) -> int:
    errors = []
    skill_file = root / "SKILL.md"
    if not skill_file.exists():
        errors.append("Missing SKILL.md")
    else:
        text = skill_file.read_text(encoding="utf-8")
        try:
            frontmatter, body = split_frontmatter(text)
            metadata = parse_simple_frontmatter(frontmatter)
            name = metadata.get("name", "")
            description = metadata.get("description", "")

            if not name:
                errors.append("Missing required frontmatter field: name")
            elif not NAME_RE.match(name):
                errors.append(f"Invalid skill name {name!r}; use lowercase letters, numbers, and single hyphens")
            elif name != root.name:
                errors.append(f"Skill name {name!r} must match folder name {root.name!r}")
            elif len(name) > 64:
                errors.append("Skill name must be at most 64 characters")

            if not description:
                errors.append("Missing required frontmatter field: description")
            elif len(description) > 1024:
                errors.append("Description must be at most 1024 characters")

            if not body.strip():
                errors.append("SKILL.md body is empty")
        except ValueError as exc:
            errors.append(str(exc))

    for relative in REQUIRED_REFERENCES:
        if not (root / relative).exists():
            errors.append(f"Missing bundled file: {relative}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {root} looks like a valid greek-grammar-agent-skill skill package.")
    return 0


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    return validate(root)


if __name__ == "__main__":
    raise SystemExit(main())
