from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict, total=False):

    user_query: str

    customer_id: int | None

    order_id: int | None

    intent: str

    plan: Dict[str, Any]

    retrieved_data: Dict[str, Any]

    analysis: Dict[str, Any]

    validation: Dict[str, Any]

    recommendation: Dict[str, Any]

    approval_required: bool

    human_approved: bool

    action_result: Dict[str, Any]

    final_response: str

    evidence: List[Dict[str, Any]]

    audit_log: List[Dict[str, Any]]

    error: str