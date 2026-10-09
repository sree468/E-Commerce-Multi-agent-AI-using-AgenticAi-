from app.services.audit import add_audit_log


def create_final_response(state):

    intent = state.get("intent")
    analysis = state.get("analysis", {})
    retrieved_data = state.get("retrieved_data", {})
    validation = state.get("validation", {})
    action_result = state.get("action_result", {})

    answer = analysis.get("result", "")

    # -----------------------------------------
    # Order tracking
    # -----------------------------------------

    if intent == "order_tracking":

        order = retrieved_data.get("order")

        if order:

            order_id = order.get("id")
            status = order.get("status")
            delivery_status = order.get("delivery_status")
            payment_status = order.get("payment_status")

            answer = (
                f"Your order #{order_id} is currently "
                f"{status.lower()}. "
                f"The delivery status is "
                f"{delivery_status.lower()}. "
                f"Your payment status is "
                f"{payment_status.lower()}."
            )

            if delivery_status == "Delayed":

                answer += (
                    " We apologize for the delay."
                )

    # -----------------------------------------
    # Product search
    # -----------------------------------------

    elif intent == "product_search":

        products = retrieved_data.get(
            "products",
            []
        )

        if products:

            product_lines = []

            for product in products[:5]:

                product_lines.append(
                    f"{product['name']} - "
                    f"₹{product['price']:,.0f} "
                    f"(Rating: {product['rating']})"
                )

            answer = (
                "Here are the products I found:\n\n"
                + "\n".join(product_lines)
            )

        else:

            answer = (
                "I couldn't find a matching product."
            )

    # -----------------------------------------
    # Return
    # -----------------------------------------

    elif intent == "return_request":

        if state.get("approval_required"):

            answer = (
                "Your return request requires human approval "
                "before it can be processed."
            )

        else:

            if action_result.get("success"):

                answer = action_result.get(
                    "message",
                    "Your return request has been created."
                )

    # -----------------------------------------
    # Cancellation
    # -----------------------------------------

    elif intent == "cancellation":

        if state.get("approval_required"):

            answer = (
                "This cancellation requires human approval "
                "before it can be processed."
            )

        elif action_result.get("success"):

            answer = action_result.get(
                "message",
                "Your order has been cancelled."
            )

    # -----------------------------------------
    # Refund
    # -----------------------------------------

    elif intent == "refund":

        answer = (
            "Your refund request requires human approval "
            "before it can be processed."
        )

    # -----------------------------------------
    # Support
    # -----------------------------------------

    elif intent == "support":

        answer = analysis.get(
            "result",
            "I can help you with your support request."
        )

    # -----------------------------------------
    # General
    # -----------------------------------------

    elif intent == "general":

        answer = analysis.get(
            "result",
            "How can I help you today?"
        )

    state["final_response"] = answer

    state = add_audit_log(
        state,
        "Response Agent",
        "Final response generated",
        {
            "intent": intent
        }
    )

    return state