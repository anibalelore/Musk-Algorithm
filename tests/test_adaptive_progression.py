"""Behavior tests for the v1.3 adaptive discovery and stage gates."""
from __future__ import annotations

import unittest

from scripts.session_engine import (
    DEFAULT_DIMENSIONS,
    evaluate_discovery,
    transition_stage,
    merge_session,
)


class AdaptiveProgressionTests(unittest.TestCase):
    def scores(self, value: int) -> dict[str, int]:
        return {name: value for name in DEFAULT_DIMENSIONS}

    def test_small_business_can_finish_before_thirty_questions(self):
        result = evaluate_discovery(self.scores(3), essential=DEFAULT_DIMENSIONS[:5],
                                    question_count=15, flow_coherent=True,
                                    requirements_identified=True)
        self.assertEqual(result["recommendation"], "ADVANCE_TO_DELETE")

    def test_unknown_essential_dimension_blocks_advance(self):
        scores = self.scores(3)
        scores["procesos_operativos"] = 1
        result = evaluate_discovery(scores, essential=["procesos_operativos"],
                                    question_count=40, flow_coherent=False,
                                    requirements_identified=True)
        self.assertEqual(result["recommendation"], "INVESTIGATE_BLOCKER")

    def test_complex_business_can_finish_around_forty_five(self):
        result = evaluate_discovery(self.scores(3), essential=DEFAULT_DIMENSIONS,
                                    question_count=45, flow_coherent=True,
                                    requirements_identified=True,
                                    recent_information_gain=[True, False, False, False])
        self.assertEqual(result["recommendation"], "ADVANCE_TO_DELETE")

    def test_explicit_scoped_extension_allows_more_than_sixty(self):
        scores = self.scores(3)
        scores["excepciones_y_riesgos"] = 2
        result = evaluate_discovery(scores, essential=DEFAULT_DIMENSIONS,
                                    question_count=61, flow_coherent=True,
                                    requirements_identified=True,
                                    explicit_extension=True)
        self.assertTrue(result["may_ask_ordinary_question"])
        self.assertEqual(result["recommendation"], "INVESTIGATE_BLOCKER")

    def test_low_marginal_yield_advances_with_documented_uncertainty(self):
        result = evaluate_discovery(self.scores(2), essential=DEFAULT_DIMENSIONS,
                                    question_count=28, flow_coherent=True,
                                    requirements_identified=True,
                                    recent_information_gain=[False, False, False])
        self.assertEqual(result["recommendation"], "ADVANCE_WITH_UNCERTAINTIES")

    def test_sixty_is_an_ordinary_cap_not_question_sixty_one(self):
        result = evaluate_discovery(self.scores(2), essential=DEFAULT_DIMENSIONS,
                                    question_count=60, flow_coherent=True,
                                    requirements_identified=True)
        self.assertEqual(result["recommendation"], "ADVANCE_WITH_UNCERTAINTIES")
        self.assertFalse(result["may_ask_ordinary_question"])

    def test_stage_transition_requires_confirmation_by_default(self):
        pending = transition_stage("QUESTION", deliverable_ready=True, confirmed=False)
        self.assertEqual(pending["stage"], "QUESTION")
        self.assertTrue(pending["awaiting_confirmation"])
        advanced = transition_stage("QUESTION", deliverable_ready=True, confirmed=True)
        self.assertEqual(advanced["stage"], "DELETE")

    def test_auto_advance_does_not_grant_technical_permission(self):
        advanced = transition_stage("SIMPLIFY", deliverable_ready=True, confirmed=False,
                                    auto_advance_enabled=True)
        self.assertEqual(advanced["stage"], "ACCELERATE")
        self.assertFalse(advanced["technical_permission_granted"])

    def test_historical_decisions_are_preserved(self):
        old = {"decisions": [{"id": "M-1", "status": "APPROVED"},
                             {"id": "M-2", "status": "REJECTED"}],
               "question_count": 100, "stage": "SIMPLIFY"}
        resumed = merge_session(old, {"project_id": "voltriva"})
        self.assertEqual(resumed["stage"], "SIMPLIFY")
        self.assertEqual(resumed["question_count"], 100)
        self.assertEqual([d["status"] for d in resumed["decisions"]],
                         ["APPROVED", "REJECTED"])


if __name__ == "__main__":
    unittest.main()
