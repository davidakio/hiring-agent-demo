def log_decision(decision):
    trace_id = new_trace_id()   # <-- DELETE THIS LINE in test D5
    audit_log("hiring_decision", decision, trace_id)
