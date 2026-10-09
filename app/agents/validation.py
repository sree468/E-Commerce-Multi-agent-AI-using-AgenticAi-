from app.services.audit import add_audit_log


def validation_agent(state):

    intent = state.get("intent", "")
    analysis = state.get("analysis", {})
    retrieved_data = state.get("retrieved_data", {})

    approval_required = False

    reason = "Operation can proceed."

    # Refunds require human approval
    if intent == "refund":

        approval_required = True

        reason = (
            "Refund operations require human approval."
        )

    # Check cancellation
    elif intent == "cancellation":

        order = retrieved_data.get("order")

        if not order:

            approval_required = True

            reason = "Order was not found."

        elif order.get("status") == "Delivered":

            approval_required = True

            reason = (
                "Delivered orders cannot be cancelled automatically."
            )

    # Return
    elif intent == "return_request":

        order = retrieved_data.get("order")

        if not order:

            approval_required = True

            reason = "Order was not found."

    validation_status = (
        "REQUIRES_HUMAN_APPROVAL"
        if approval_required
        else "VALID"
    )

    state["validation"] = {
        "status": validation_status,
        "reason": reason,
        "analysis_available": bool(analysis)
    }

    state["approval_required"] = approval_required

    state = add_audit_log(
        state,
        "Validation Agent",
        "Validation completed",
        {
            "status": validation_status,
            "approval_required": approval_required
        }
    )

    return state