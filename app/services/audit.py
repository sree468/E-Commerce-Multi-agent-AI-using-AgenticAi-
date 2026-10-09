from datetime import datetime


def add_audit_log(
    state,
    agent,
    event,
    details
):

    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent,
        "event": event,
        "details": details
    }

    state.setdefault(
        "audit_log",
        []
    )

    state["audit_log"].append(
        log
    )

    return state