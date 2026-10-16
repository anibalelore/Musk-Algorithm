"""Behavior tests for v1.3 automation eligibility and action modes."""
from __future__ import annotations

import unittest

from scripts.session_engine import assess_automation


class AutomationExecutionTests(unittest.TestCase):
    def test_stable_repetitive_process_can_be_automated(self):
        result = assess_automation(stable=True, repetitive=True, rules_clear=True,
                                   technical_path=True, reversible=True)
        self.assertEqual(result["decision"], "AUTOMATE_NOW")
        self.assertEqual(result["recommended_mode"], "BUILD")

    def test_unstable_process_is_not_automated(self):
        result = assess_automation(stable=False, repetitive=True, rules_clear=False,
                                   technical_path=True, reversible=True)
        self.assertEqual(result["decision"], "VALIDATE_FIRST")

    def test_no_access_produces_handoff(self):
        result = assess_automation(stable=True, repetitive=True, rules_clear=True,
                                   technical_path=True, reversible=True,
                                   repository_access=False)
        self.assertEqual(result["recommended_mode"], "HANDOFF")

    def test_build_requires_edit_authorization(self):
        result = assess_automation(stable=True, repetitive=True, rules_clear=True,
                                   technical_path=True, reversible=True,
                                   repository_access=True, edit_authorized=False)
        self.assertEqual(result["recommended_mode"], "DESIGN")
        self.assertFalse(result["may_edit"])


if __name__ == "__main__":
    unittest.main()
