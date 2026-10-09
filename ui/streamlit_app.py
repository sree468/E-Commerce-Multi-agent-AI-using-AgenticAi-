import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


import streamlit as st

from app.main import run_agent
from app.database.seed import seed_database


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="E-Commerce AI Assistant",
    page_icon="🛒",
    layout="wide"
)


# ---------------------------------------------------------
# DATABASE INITIALIZATION
# ---------------------------------------------------------

try:
    seed_database()

except Exception as e:
    st.error(
        f"Database initialization failed: {e}"
    )
    st.stop()


# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------

st.title("🛒 E-Commerce AI Assistant")

st.caption(
    "AI-powered customer support and e-commerce operations assistant"
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("Customer Details")

    customer_id = st.number_input(
        "Customer ID",
        min_value=1,
        value=1,
        step=1
    )

    order_id = st.number_input(
        "Order ID",
        min_value=1001,
        value=1001,
        step=1
    )

    st.markdown("---")

    st.subheader("Agent Architecture")

    st.write("🧠 Supervisor")
    st.write("🔎 Retrieval")
    st.write("📊 Analysis")
    st.write("✅ Validation")
    st.write("⚡ Action")
    st.write("👤 Escalation")
    st.write("💬 Response")


# ---------------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------------

st.subheader("How can I help you?")

user_query = st.chat_input(
    "Ask about your order, products, returns or support..."
)


# ---------------------------------------------------------
# PROCESS USER QUERY
# ---------------------------------------------------------

if user_query:

    # ---------------------------------------------
    # USER MESSAGE
    # ---------------------------------------------

    with st.chat_message("user"):
        st.write(user_query)


    # ---------------------------------------------
    # ASSISTANT RESPONSE
    # ---------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Checking your request..."):

            try:

                result = run_agent(
                    user_query=user_query,
                    customer_id=int(customer_id),
                    order_id=int(order_id)
                )


                # -----------------------------------------
                # CUSTOMER-FACING RESPONSE
                # -----------------------------------------

                final_response = result.get(
                    "final_response"
                )

                if final_response:

                    st.markdown(final_response)

                else:

                    st.warning(
                        "I could not generate a response."
                    )


                # -----------------------------------------
                # DEVELOPER DETAILS
                # -----------------------------------------

                with st.expander(
                    "🔧 Developer / Agent Details"
                ):

                    # =====================================
                    # INTENT
                    # =====================================

                    st.markdown(
                        "### 🎯 Detected Intent"
                    )

                    st.code(
                        str(
                            result.get(
                                "intent",
                                "Unknown"
                            )
                        )
                    )


                    # =====================================
                    # ANALYSIS
                    # =====================================

                    st.markdown(
                        "### 📊 Analysis"
                    )

                    analysis = result.get(
                        "analysis",
                        {}
                    )

                    if isinstance(
                        analysis,
                        dict
                    ):

                        analysis_result = analysis.get(
                            "result",
                            ""
                        )

                        st.write(
                            analysis_result
                        )

                    else:

                        st.write(
                            analysis
                        )


                    # =====================================
                    # VALIDATION
                    # =====================================

                    st.markdown(
                        "### ✅ Validation"
                    )

                    validation = result.get(
                        "validation",
                        {}
                    )

                    if isinstance(
                        validation,
                        dict
                    ):

                        st.json(
                            validation
                        )

                    else:

                        st.write(
                            validation
                        )


                    # =====================================
                    # ACTION RESULT
                    # =====================================

                    st.markdown(
                        "### ⚡ Action Result"
                    )

                    action_result = result.get(
                        "action_result",
                        {}
                    )

                    if isinstance(
                        action_result,
                        dict
                    ):

                        st.json(
                            action_result
                        )

                    else:

                        st.write(
                            action_result
                        )


                    # =====================================
                    # EVIDENCE
                    # =====================================

                    st.markdown(
                        "### 📚 Evidence"
                    )

                    evidence = result.get(
                        "evidence",
                        []
                    )

                    if evidence:

                        for item in evidence:

                            if isinstance(
                                item,
                                dict
                            ):

                                st.json(
                                    item
                                )

                            else:

                                st.write(
                                    item
                                )

                    else:

                        st.write(
                            "No evidence."
                        )


                    # =====================================
                    # AUDIT TRAIL
                    # =====================================

                    st.markdown(
                        "### 📋 Audit Trail"
                    )

                    audit_log = result.get(
                        "audit_log",
                        []
                    )

                    if not audit_log:

                        st.write(
                            "No audit events."
                        )

                    else:

                        for log in audit_log:

                            if not isinstance(
                                log,
                                dict
                            ):
                                st.write(log)
                                continue


                            agent = log.get(
                                "agent",
                                "Unknown Agent"
                            )

                            event = log.get(
                                "event",
                                "Unknown Event"
                            )

                            details = log.get(
                                "details"
                            )


                            st.write(
                                f"**{agent}** → {event}"
                            )


                            # ---------------------------------
                            # IMPORTANT:
                            # Do NOT use json.loads()
                            # ---------------------------------

                            if isinstance(
                                details,
                                dict
                            ):

                                st.json(
                                    details
                                )

                            elif isinstance(
                                details,
                                list
                            ):

                                st.write(
                                    details
                                )

                            elif details is not None:

                                st.write(
                                    details
                                )

                            else:

                                st.write(
                                    "No additional details."
                                )


            # ---------------------------------------------
            # ERROR HANDLING
            # ---------------------------------------------

            except Exception as e:

                error_message = str(e)

                if (
                    "504" in error_message
                    or
                    "DEADLINE_EXCEEDED"
                    in error_message
                ):

                    st.error(
                        "The AI service timed out. "
                        "Please try again."
                    )

                else:

                    st.error(
                        "Something went wrong while "
                        "processing your request."
                    )

                    with st.expander(
                        "Technical error"
                    ):

                        st.code(
                            error_message
                        )