from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from app.state import AgentState

from app.agents.supervisor import supervisor_agent
from app.agents.retrieval import retrieval_agent
from app.agents.analysis import analysis_agent
from app.agents.validation import validation_agent
from app.agents.action import action_agent
from app.agents.escalation import escalation_agent

from app.services.response import create_final_response


def route_after_validation(state):

    if state.get("approval_required", False):

        return "escalation"

    return "action"


def build_graph():

    workflow = StateGraph(AgentState)

    # -----------------------------------------
    # Nodes
    # -----------------------------------------

    workflow.add_node(
        "supervisor",
        supervisor_agent
    )

    workflow.add_node(
        "retrieval",
        retrieval_agent
    )

    workflow.add_node(
        "analysis",
        analysis_agent
    )

    workflow.add_node(
        "validation",
        validation_agent
    )

    workflow.add_node(
        "action",
        action_agent
    )

    workflow.add_node(
        "escalation",
        escalation_agent
    )

    workflow.add_node(
        "final_response",
        create_final_response
    )

    # -----------------------------------------
    # Flow
    # -----------------------------------------

    workflow.add_edge(
        START,
        "supervisor"
    )

    workflow.add_edge(
        "supervisor",
        "retrieval"
    )

    workflow.add_edge(
        "retrieval",
        "analysis"
    )

    workflow.add_edge(
        "analysis",
        "validation"
    )

    workflow.add_conditional_edges(
        "validation",
        route_after_validation,
        {
            "action": "action",
            "escalation": "escalation"
        }
    )

    workflow.add_edge(
        "action",
        "final_response"
    )

    workflow.add_edge(
        "escalation",
        "final_response"
    )

    workflow.add_edge(
        "final_response",
        END
    )

    # -----------------------------------------
    # Checkpoint memory
    # -----------------------------------------

    memory = MemorySaver()

    return workflow.compile(
        checkpointer=memory
    )