import streamlit as st

from app.graph import build_graph


graph = build_graph()


def run_agent(
    user_query,
    customer_id=None,
    order_id=None
):

    state = {
        "user_query": user_query,
        "customer_id": customer_id,
        "order_id": order_id,
        "human_approved": False,
        "approval_required": False,
        "evidence": [],
        "audit_log": []
    }

    try:

        result = graph.invoke(
            state,
            config={
                "configurable": {
                    "thread_id": "streamlit-user"
                }
            }
        )

        return result

    except Exception as e:

        error_message = str(e)

        if "504" in error_message or "DEADLINE_EXCEEDED" in error_message:

            st.error(
                "Gemini API timed out. "
                "Please try again in a few seconds."
            )

            st.info(
                "The request took longer than the Gemini API deadline."
            )

        else:

            st.error(
                f"Agent execution failed: {error_message}"
            )