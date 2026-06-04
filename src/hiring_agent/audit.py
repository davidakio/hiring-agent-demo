"""Audit log for hiring decisions. Every decision carries a trace id so it can be
reconstructed and reviewed later — this is the audit trail the business relies on."""

import uuid

_AUDIT_SINK: list[dict] = []


def new_trace_id() -> str:
    return uuid.uuid4().hex


def audit_log(event: str, trace_id: str, payload: dict) -> None:
    _AUDIT_SINK.append({"event": event, "trace_id": trace_id, "payload": payload})


def record_decision(decision: dict) -> str:
    trace_id = new_trace_id()   # <-- Test D5: delete this line to remove trace logging
    audit_log(event="hiring_decision", trace_id=trace_id, payload=decision)
    return trace_id
