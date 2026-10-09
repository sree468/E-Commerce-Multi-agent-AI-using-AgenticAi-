from app.services.audit import add_audit_log


def detect_intent(query: str) -> str:

    query = query.lower().strip()

    # Product related
    product_words = [
        "product",
        "phone",
        "mobile",
        "laptop",
        "buy",
        "purchase",
        "price",
        "catalog",
        "available",
        "recommend"
    ]

    # Order tracking
    order_words = [
        "where is my order",
        "track my order",
        "order status",
        "order tracking",
        "delivery",
        "delayed",
        "shipped",
        "shipping"
    ]

    # Return
    return_words = [
        "return",
        "damaged",
        "defective",
        "replacement"
    ]

    # Cancellation
    cancel_words = [
        "cancel",
        "cancellation"
    ]

    # Refund
    refund_words = [
        "refund",
        "money back",
        "refund amount"
    ]

    # Support
    support_words = [
        "support",
        "complaint",
        "issue",
        "problem",
        "help"
    ]

    if any(word in query for word in product_words):
        return "product_search"

    if any(word in query for word in order_words):
        return "order_tracking"

    if any(word in query for word in return_words):
        return "return_request"

    if any(word in query for word in cancel_words):
        return "cancellation"

    if any(word in query for word in refund_words):
        return "refund"

    if any(word in query for word in support_words):
        return "support"

    return "general"


def supervisor_agent(state):

    query = state.get("user_query", "")

    intent = detect_intent(query)

    state["intent"] = intent

    state["plan"] = {
        "intent": intent,
        "tasks": [
            "Retrieve relevant e-commerce information",
            "Analyze the customer request",
            "Validate the recommendation",
            "Execute action if allowed"
        ]
    }

    state = add_audit_log(
        state,
        "Supervisor Agent",
        "Intent detected",
        {
            "query": query,
            "intent": intent
        }
    )

    return state