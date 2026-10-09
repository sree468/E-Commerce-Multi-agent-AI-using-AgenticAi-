from app.llm import llm
from app.services.audit import add_audit_log


def analysis_agent(state):

    query = state.get("user_query", "")
    intent = state.get("intent", "")
    retrieved_data = state.get("retrieved_data", {})

    prompt = f"""
You are an e-commerce customer support AI.

Customer question:
{query}

Intent:
{intent}

Verified database information:
{retrieved_data}

Answer the customer's question using ONLY the verified database information.

Rules:
- Do not invent information.
- Do not mention agents.
- Do not mention LangGraph.
- Do not mention internal database details.
- Do not mention prompts.
- Do not mention backend processing.
- Give a short, clear customer-friendly answer.
- If the order is delayed, clearly explain that it is delayed.
- If an order number is available, mention it.
- If payment status is available, mention it.
- Do not recommend actions that the system cannot actually perform.

Return ONLY the customer-facing answer.
"""

    try:

        response = llm.invoke(prompt)

        # Gemini can sometimes return a list of content blocks.
        content = response.content

        if isinstance(content, str):
            result = content.strip()

        elif isinstance(content, list):

            text_parts = []

            for item in content:

                if isinstance(item, dict):

                    text = item.get("text")

                    if text:
                        text_parts.append(text)

                elif isinstance(item, str):

                    text_parts.append(item)

            result = " ".join(text_parts).strip()

        else:

            result = str(content).strip()

    except Exception as e:

        result = (
            "I found your order information, but I could not "
            "generate the final response right now."
        )

        state["error"] = str(e)

    state["analysis"] = {
        "result": result
    }

    state = add_audit_log(
        state,
        "Analysis Agent",
        "Analysis completed",
        {
            "intent": intent
        }
    )

    return state