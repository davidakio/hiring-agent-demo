from hiring_agent.oversight import Decision, apply_decision, needs_human_approval


def test_rejection_needs_human_approval():
    decision = Decision(candidate_id="c1", score=20, action="reject")
    assert needs_human_approval(decision) is True
    assert apply_decision(decision) == "pending_human_review"


def test_advance_is_applied():
    decision = Decision(candidate_id="c2", score=90, action="advance")
    assert needs_human_approval(decision) is False
    assert apply_decision(decision) == "applied"
