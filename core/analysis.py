from typing import Any, Dict, List


def review_contract_obligations(obligations: List[Dict[str, Any]]) -> Dict[str, Any]:
    results = []
    for index, raw in enumerate(obligations or []):
        obligation = dict(raw or {})
        missing = [
            key for key in ("description", "clause_reference", "responsible_party", "due_date")
            if not obligation.get(key)
        ]
        results.append({
            "obligation_id": obligation.get("id", f"obligation-{index + 1}"),
            "description": obligation.get("description", "Not supplied"),
            "clause_reference": obligation.get("clause_reference", "Not supplied"),
            "responsible_party": obligation.get("responsible_party", "Unspecified"),
            "due_date": obligation.get("due_date", "Unspecified"),
            "missing_fields": missing,
        })
    return {
        "obligation_count": len(results),
        "obligations": results,
        "note": "Structured tracking only; ambiguous terms require qualified review.",
    }


def map_compliance_evidence(
    obligations: List[Dict[str, Any]],
    evidence_records: List[Dict[str, Any]],
) -> Dict[str, Any]:
    obligations = list(obligations or [])
    evidence_records = list(evidence_records or [])
    mappings = []
    for index, obligation in enumerate(obligations):
        obligation = dict(obligation or {})
        oid = str(obligation.get("id", f"obligation-{index + 1}"))
        matched = [
            dict(evidence) for evidence in evidence_records
            if str((evidence or {}).get("obligation_id", "")) == oid
        ]
        mappings.append({
            "obligation_id": oid,
            "evidence_records": matched,
            "evidence_gap": not bool(matched),
        })
    matched_ids = {
        str((evidence or {}).get("obligation_id", ""))
        for evidence in evidence_records
    }
    known_ids = {
        str((obligation or {}).get("id", f"obligation-{index + 1}"))
        for index, obligation in enumerate(obligations)
    }
    unmatched = [
        dict(evidence) for evidence in evidence_records
        if str((evidence or {}).get("obligation_id", "")) not in known_ids
    ]
    return {
        "mappings": mappings,
        "obligations_without_evidence": [item["obligation_id"] for item in mappings if item["evidence_gap"]],
        "unmatched_evidence": unmatched,
        "note": "Evidence presence does not prove that the evidence is sufficient or authentic.",
    }


def prepare_compliance_action_plan(actions: List[Dict[str, Any]]) -> Dict[str, Any]:
    actions = list(actions or [])
    rank = {"urgent": 0, "high": 1, "medium": 2, "low": 3}
    indexed = list(enumerate(actions))
    indexed.sort(key=lambda pair: (
        rank.get(str((pair[1] or {}).get("priority", "")).lower(), 4),
        pair[0],
    ))
    plan = []
    for _, raw in indexed:
        action = dict(raw or {})
        action.setdefault("owner", "Unspecified")
        action.setdefault("due_date", "Unspecified")
        action.setdefault("status", "Open")
        action.setdefault("priority", "Unspecified")
        plan.append(action)
    return {"action_count": len(plan), "actions": plan}
