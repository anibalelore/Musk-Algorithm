#!/usr/bin/env python3
"""Install this standalone Agent Skill for Claude Code or Codex.

Usage: python scripts/install.py --agent both --scope user
       python scripts/install.py --agent claude --scope project --project /path/to/repo
"""
from __future__ import annotations

import argparse
from datetime import datetime
import shutil
from pathlib import Path
import sys

SKILL_NAME = "musk-algorithm"
ROOT = Path(__file__).resolve().parents[1]


def targets(agent: str, scope: str, project: Path | None) -> list[Path]:
    base = Path.home() if scope == "user" else project
    if base is None:
        raise ValueError("Para --scope project, utiliza --project /ruta/al/repositorio.")
    base = base.expanduser().resolve()
    kinds = ("claude", "codex") if agent == "both" else (agent,)
    return [base / (".claude/skills" if kind == "claude" else ".agents/skills") / SKILL_NAME
            for kind in kinds]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Instalar musk-algorithm como skill independiente")
    parser.add_argument("--agent", required=True, choices=["claude", "codex", "both"])
    parser.add_argument("--scope", default="user", choices=["user", "project"])
    parser.add_argument("--project", type=Path, help="Ruta del repositorio si scope=project")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar rutas sin tocar archivos")
    parser.add_argument("--replace", action="store_true", help="Respaldar versión existente y reemplazarla")
    args = parser.parse_args(argv)

    if args.scope == "project" and args.project is None:
        parser.error("--scope project necesita --project /ruta/al/repositorio")
    if not (ROOT / "SKILL.md").is_file():
        print("Error: SKILL.md no encontrado; ejecuta desde el paquete completo.", file=sys.stderr)
        return 2
    try:
        locations = targets(args.agent, args.scope, args.project)
        for location in locations:
            if location == ROOT or ROOT in location.parents:
                raise ValueError("El destino está dentro del paquete fuente; elige otro proyecto para evitar copia recursiva.")
        existing = [path for path in locations if path.exists() or path.is_symlink()]
        if existing and not args.replace:
            print("La skill ya existe. No se sobrescribe sin --replace:", file=sys.stderr)
            for location in existing:
                print(f"  {location}", file=sys.stderr)
            return 3
        for destination in locations:
            print(f"{'[DRY RUN] ' if args.dry_run else ''}Instalación: {destination}")
        if args.dry_run:
            return 0

        # Backup existing skill before replacement. Never merge old and new files.
        for destination in locations:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() or destination.is_symlink():
                if destination.is_symlink():
                    raise ValueError(f"No se reemplazan enlaces simbólicos: {destination}")
                if not destination.is_dir():
                    raise ValueError(f"La ruta de destino no es directorio: {destination}")
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                backup = destination.with_name(f"{SKILL_NAME}.backup-{timestamp}")
                counter = 1
                while backup.exists():
                    backup = destination.with_name(f"{SKILL_NAME}.backup-{timestamp}-{counter}")
                    counter += 1
                destination.rename(backup)
                print(f"Copia de seguridad: {backup}")
            shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
        print("Instalación completada. Inicia una sesión nueva de tu agente y prueba /musk-algorithm.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
