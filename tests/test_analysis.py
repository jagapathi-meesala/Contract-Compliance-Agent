from core.analysis import review_contract_obligations, map_compliance_evidence, prepare_compliance_action_plan


def test_obligations_missing_fields():
    result = review_contract_obligations([{"id": "C1", "description": "Submit report"}])
    assert "due_date" in result["obligations"][0]["missing_fields"]


def test_obligations_count():
    assert review_contract_obligations([{}, {}])["obligation_count"] == 2


def test_evidence_gap():
    result = map_compliance_evidence([{"id": "O1"}], [])
    assert result["obligations_without_evidence"] == ["O1"]


def test_evidence_mapping():
    result = map_compliance_evidence(
        [{"id": "O1"}],
        [{"obligation_id": "O1", "name": "Report"}],
    )
    assert result["mappings"][0]["evidence_gap"] is False


def test_unmatched_evidence():
    result = map_compliance_evidence([], [{"obligation_id": "unknown"}])
    assert len(result["unmatched_evidence"]) == 1


def test_action_priority():
    result = prepare_compliance_action_plan([
        {"name": "Routine", "priority": "low"},
        {"name": "Urgent review", "priority": "urgent"},
    ])
    assert result["actions"][0]["name"] == "Urgent review"


def test_action_defaults():
    result = prepare_compliance_action_plan([{"name": "Check clause"}])
    assert result["actions"][0]["owner"] == "Unspecified"
