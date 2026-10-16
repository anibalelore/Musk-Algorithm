"""Smoke tests using only Python stdlib."""
from __future__ import annotations
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillTests(unittest.TestCase):
    def test_validator(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_five_steps(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        steps = ["QUESTION", "DELETE", "SIMPLIFY", "ACCELERATE", "AUTOMATE"]
        first = [text.index(f"### {idx} · {step}") for idx, step in enumerate(steps, 1)]
        self.assertEqual(first, sorted(first))
        self.assertIn("sin afiliación", text.lower())
        self.assertIn("autorización", text.lower())

    def test_conversational_mode(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        interview = (ROOT / "references/interactive-interview.md").read_text(encoding="utf-8")
        system = (ROOT / "references/live-system-audit.md").read_text(encoding="utf-8")
        self.assertIn("Modo principal: consultoría interactiva", text)
        self.assertIn("una cuestión prioritaria por turno", text)
        self.assertIn("no modificaré", interview.lower())
        self.assertIn("PROPOSED", interview)
        self.assertIn("APPROVED", interview)
        self.assertIn("No declarar", system)
        self.assertTrue((ROOT / "assets/decision-session-template.md").is_file())
        self.assertIn('version: "1.3.0"', text)
        self.assertIn("Adaptive Discovery Engine", text)
        self.assertIn("Smart Stage Gate Manager", text)

    def test_automation_execution(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        execution = (ROOT / "references/automation-execution.md").read_text(encoding="utf-8")
        for mode in ["DESIGN", "BUILD", "PILOT", "HANDOFF"]:
            self.assertIn(mode, skill)
            self.assertIn(mode, execution)
        self.assertIn("no desplegar", skill.lower())
        self.assertIn("idempotencia", execution.lower())
        self.assertIn("sin permiso", execution.lower())
        self.assertTrue((ROOT / "assets/automation-blueprint.md").exists())
        self.assertTrue((ROOT / "assets/automation-handoff.md").exists())

    def test_v13_resources_and_demonstrations(self):
        for relative in [
            "references/adaptive-discovery.md", "references/stage-gates.md",
            "references/sufficiency-evaluation.md", "references/automation-coordinator.md",
            "references/v1.3-demonstrations.md", "scripts/session_engine.py",
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)
        demo = (ROOT / "references/v1.3-demonstrations.md").read_text(encoding="utf-8")
        for stage in ["QUESTION", "DELETE", "SIMPLIFY", "ACCELERATE", "AUTOMATE"]:
            self.assertIn(stage, demo)

    def test_personal_install(self):
        with tempfile.TemporaryDirectory() as folder:
            env = os.environ.copy()
            env["HOME"] = folder
            env["USERPROFILE"] = folder
            installer = str(ROOT / "scripts/install.py")
            run = subprocess.run([sys.executable, installer, "--agent", "both", "--scope", "user"],
                                 env=env, capture_output=True, text=True, check=False)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            for location in [".claude/skills", ".agents/skills"]:
                path = Path(folder) / location / "musk-algorithm"
                self.assertTrue((path / "SKILL.md").is_file())
                self.assertTrue((path / "references/examples.md").is_file())
            duplicate = subprocess.run([sys.executable, installer, "--agent", "both"],
                                       env=env, capture_output=True, text=True)
            self.assertEqual(duplicate.returncode, 3)

    def test_project_dry_run(self):
        with tempfile.TemporaryDirectory() as folder:
            installer = str(ROOT / "scripts/install.py")
            run = subprocess.run([sys.executable, installer, "--agent", "codex", "--scope", "project",
                                  "--project", folder, "--dry-run"], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertFalse((Path(folder) / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
