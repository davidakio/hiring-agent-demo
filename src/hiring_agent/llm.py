"""Screens a candidate with the model, routes the decision through the oversight gate,
and writes it to the audit log."""

import re
from pathlib import Path

from openai import OpenAI

from .audit import record_decision
from .config import load_model_config
from .oversight import Decision, apply_decision

_PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "hiring_agent.prompt.md"


def _load_prompt() -> str:
    return _PROMPT_PATH.read_text(encoding="utf-8")


def _extract_score(text: str) -> int:
    match = re.search(r"\b(\d{1,3})\b", text)
    return int(match.group(1)) if match else 0


def screen_candidate(cv_text: str, role: str) -> dict:
    cfg = load_model_config()
    client = OpenAI()
    response = client.chat.completions.create(
        model=cfg["model"],
        temperature=cfg["temperature"],
        max_tokens=cfg["max_tokens"],
        top_p=cfg["top_p"],
        messages=[
            {"role": "system", "content": _load_prompt()},
            {"role": "user", "content": f"Role: {role}\n\nCV:\n{cv_text}"},
        ],
    )
    summary = response.choices[0].message.content or ""
    score = _extract_score(summary)
    action = "reject" if score < cfg["auto_reject_below_score"] else "advance"
    decision = Decision(candidate_id="unknown", score=score, action=action)
    status = apply_decision(decision)
    trace_id = record_decision(
        {"role": role, "score": score, "action": action, "status": status}
    )
    return {
        "score": score,
        "action": action,
        "status": status,
        "trace_id": trace_id,
        "summary": summary,
    }
