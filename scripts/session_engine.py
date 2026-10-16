#!/usr/bin/env python3
"""Pure, dependency-free policy helpers for Musk Algorithm v1.3 sessions.

The host agent remains responsible for judgment and conversation. These helpers make
the ordinary limits, stage gates and preservation rules executable and testable.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable, Mapping

DEFAULT_DIMENSIONS = (
    "modelo_de_negocio", "clientes_y_valor", "procesos_operativos",
    "reglas_comerciales", "tecnologia_e_integraciones", "responsabilidades",
    "excepciones_y_riesgos", "objetivos_y_metricas",
)
STAGES = ("QUESTION", "DELETE", "SIMPLIFY", "ACCELERATE", "AUTOMATE")
DECISION_STATES = {"PROPOSED", "APPROVED", "REJECTED", "NEEDS_EVIDENCE", "BLOCKED"}


def evaluate_discovery(scores: Mapping[str, int], *, essential: Iterable[str],
                       question_count: int, flow_coherent: bool,
                       requirements_identified: bool,
                       unresolved_contradiction: bool = False,
                       explicit_extension: bool = False,
                       recent_information_gain: Iterable[bool] = ()) -> dict[str, Any]:
    """Return a recommendation; scores guide judgment rather than fake precision."""
    if question_count < 0 or any(v not in range(5) for v in scores.values()):
        raise ValueError("question_count must be positive and scores must be 0..4")
    essential = tuple(essential)
    missing = [name for name in essential if scores.get(name, 0) < 3]
    capped = question_count >= 60 and not explicit_extension
    low_yield = len(tuple(recent_information_gain)) >= 3 and not any(tuple(recent_information_gain)[-3:])
    ready = not missing and flow_coherent and requirements_identified and not unresolved_contradiction
    if ready:
        recommendation = "ADVANCE_TO_DELETE"
    elif capped:
        recommendation = "INVESTIGATE_BLOCKER" if unresolved_contradiction else "ADVANCE_WITH_UNCERTAINTIES"
    elif unresolved_contradiction or (missing and question_count >= 30):
        recommendation = "INVESTIGATE_BLOCKER"
    elif low_yield and flow_coherent and requirements_identified:
        recommendation = "ADVANCE_WITH_UNCERTAINTIES"
    else:
        recommendation = "CONTINUE_DISCOVERY"
    return {
        "recommendation": recommendation,
        "missing_essential": missing,
        "question_count": question_count,
        "may_ask_ordinary_question": not capped,
        "extension_requires_authorization": capped,
        "sufficient": ready,
    }


def transition_stage(stage: str, *, deliverable_ready: bool, confirmed: bool,
                     auto_advance_enabled: bool = False) -> dict[str, Any]:
    if stage not in STAGES:
        raise ValueError(f"unknown stage: {stage}")
    if stage == "AUTOMATE" or not deliverable_ready:
        return {"stage": stage, "awaiting_confirmation": False,
                "technical_permission_granted": False}
    advance = confirmed or auto_advance_enabled
    return {"stage": STAGES[STAGES.index(stage) + 1] if advance else stage,
            "awaiting_confirmation": not advance,
            "technical_permission_granted": False}


def merge_session(existing: Mapping[str, Any], updates: Mapping[str, Any]) -> dict[str, Any]:
    """Resume without resetting history or silently changing decision states."""
    merged = deepcopy(dict(existing))
    historical = {d.get("id"): deepcopy(d) for d in merged.get("decisions", [])}
    for key, value in updates.items():
        if key != "decisions":
            merged[key] = deepcopy(value)
    for decision in updates.get("decisions", []):
        old = historical.get(decision.get("id"))
        if old and old.get("status") in {"APPROVED", "REJECTED"}:
            continue
        if decision.get("status") not in DECISION_STATES:
            raise ValueError("invalid decision state")
        historical[decision.get("id")] = deepcopy(decision)
    merged["decisions"] = list(historical.values())
    return merged


def assess_automation(*, stable: bool, repetitive: bool, rules_clear: bool,
                      technical_path: bool, reversible: bool,
                      repository_access: bool = True,
                      edit_authorized: bool = True) -> dict[str, Any]:
    if not stable or not rules_clear:
        decision = "VALIDATE_FIRST"
    elif not repetitive:
        decision = "KEEP_MANUAL"
    elif not technical_path or not reversible:
        decision = "SIMPLIFY_AGAIN"
    else:
        decision = "AUTOMATE_NOW"
    if not repository_access:
        mode = "HANDOFF"
    elif decision != "AUTOMATE_NOW" or not edit_authorized:
        mode = "DESIGN"
    else:
        mode = "BUILD"
    return {"decision": decision, "recommended_mode": mode,
            "may_edit": bool(repository_access and edit_authorized),
            "may_deploy": False}
