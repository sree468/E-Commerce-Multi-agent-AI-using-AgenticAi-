from app.tools.action_tools import (
    create_return,
    cancel_order
)

from app.services.audit import (
    add_audit_log
)


def action_agent(state):

    intent = state["intent"]

    order_id = state.get(
        "order_id"
    )

    # -----------------------------
    # Approval protection
    # -----------------------------

    if state.get(
        "approval_required",
        False
    ):

        result = {

            "success": False,

            "message": (
                "Human approval is "
                "required before "
                "this action."
            )
        }

        state["action_result"] = result

        return add_audit_log(

            state,

            "action",

            "action_blocked",

            "Human approval required."
        )

    # -----------------------------
    # Return
    # -----------------------------

    if intent == "return_request":

        if not order_id:

            result = {

                "success": False,

                "message": (
                    "Order ID is required."
                )
            }

        else:

            result = create_return(
                order_id
            )

    # -----------------------------
    # Cancellation
    # -----------------------------

    elif intent == "cancellation":

        if not order_id:

            result = {

                "success": False,

                "message": (
                    "Order ID is required."
                )
            }

        else:

            result = cancel_order(
                order_id
            )

    # -----------------------------
    # Other operations
    # -----------------------------

    else:

        result = {

            "success": True,

            "message": (
                "No direct business "
                "action was executed."
            )
        }

    state["action_result"] = result

    return add_audit_log(

        state,

        "action",

        "action_completed",

        str(result)
    )