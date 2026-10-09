from app.tools.order_tools import (
    get_order,
    get_customer_orders
)

from app.tools.customer_tools import (
    get_customer
)

from app.tools.catalog_tools import (
    search_products
)

from app.tools.support_tools import (
    get_support_cases
)

from app.services.audit import (
    add_audit_log
)


def retrieval_agent(state):

    intent = state["intent"]

    data = {}

    customer_id = state.get(
        "customer_id"
    )

    order_id = state.get(
        "order_id"
    )

    # -----------------------------
    # Customer information
    # -----------------------------

    if customer_id:

        customer = get_customer(
            customer_id
        )

        data["customer"] = customer

    # -----------------------------
    # Product search
    # -----------------------------

    if intent == "product_search":

        products = search_products(
            state["user_query"]
        )

        data["products"] = products

    # -----------------------------
    # Order information
    # -----------------------------

    if intent in [

        "order_tracking",

        "return_request",

        "cancellation",

        "refund"
    ]:

        if order_id:

            order = get_order(
                order_id
            )

            data["order"] = order

        elif customer_id:

            orders = get_customer_orders(
                customer_id
            )

            data["orders"] = orders

    # -----------------------------
    # Support information
    # -----------------------------

    if intent == "support":

        if customer_id:

            cases = get_support_cases(
                customer_id
            )

            data["support_cases"] = cases

    state["retrieved_data"] = data

    # -----------------------------
    # Evidence
    # -----------------------------

    state.setdefault(
        "evidence",
        []
    )

    for key, value in data.items():

        state["evidence"].append({

            "source": key,

            "record_id": "database",

            "information": str(value),

            "confidence": 0.95
        })

    return add_audit_log(

        state,

        "retrieval",

        "data_retrieved",

        f"Retrieved data for {intent}"
    )