#!/usr/bin/env python3
"""Minimal stdlib validation. For canonical validation use: skills-ref validate ."""
from __future__ import annotations
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def check(root: Path = ROOT) -> list[str]:
    errors = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["Falta SKILL.md"]
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return ["SKILL.md requiere frontmatter YAML delimitado por ---"]
    header = match.group(1)
    values = {}
    for line in header.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        field = re.match(r"([a-z][a-z0-9-]*):\s*(.*)", line)
        if field:
            values[field.group(1)] = field.group(2).strip(' "')
    name = values.get("name", "")
    description = values.get("description", "")
    if not (0 < len(name) <= 64 and NAME_RE.fullmatch(name) and name == root.name):
        errors.append("name inválido o diferente del nombre de carpeta")
    if not (0 < len(description) <= 1024):
        errors.append("description vacía o >1024 caracteres")
    if "# Musk Algorithm" not in text:
        errors.append("No se encuentra el título de la skill")
    for referenced in re.findall(r"(?<![\w/])(?:references|assets)/[\w.-]+(?:\.md|\.json)", text):
        if not (root / referenced).is_file():
            errors.append(f"Referencia ausente: {referenced}")
    for expected in [
        "README.md", "LICENSE", "scripts/install.py", "scripts/session_engine.py",
        "references/automation-playbook.md", "references/adaptive-discovery.md",
        "references/stage-gates.md", "references/sufficiency-evaluation.md",
        "references/automation-coordinator.md", "references/v1.3-demonstrations.md",
        "assets/decision-session-template.md", "assets/automation-blueprint.md",
    ]:
        if not (root / expected).is_file():
            errors.append(f"Archivo esperado ausente: {expected}")
    required = ["version: \"1.3.0\"", "Adaptive Discovery Engine",
                "Smart Stage Gate Manager", "Automation Execution Coordinator"]
    for marker in required:
        if marker not in text:
            errors.append(f"Contrato v1.3 ausente: {marker}")
    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        sys.exit(1)
    print(f"OK: {ROOT.name} — formato, metadatos y referencias básicas válidas")
