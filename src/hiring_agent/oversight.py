"""Human-in-the-loop oversight. High-impact decisions (auto-rejections) must be
approved by a person before they take effect."""

from dataclasses import dataclass


@dataclass
class Decision:
    candidate_id: str
    score: int
    action: str  # "advance" | "reject"


def needs_human_approval(decision: Decision) -> bool:
    # Auto-rejections are high-impact and require a human sign-off.
    approval_required = decision.action == "reject"   # <-- Test D4: delete this line to remove the gate
    return approval_required


def apply_decision(decision: Decision) -> str:
    if needs_human_approval(decision):
        return "pending_human_review"
    return "applied"
