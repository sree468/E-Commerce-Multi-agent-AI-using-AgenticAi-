from typing import List, Optional

from pydantic import BaseModel, Field


class Evidence(BaseModel):

    source: str

    record_id: str

    information: str

    confidence: float = Field(
        ge=0,
        le=1
    )


class AgentPlan(BaseModel):

    intent: str

    tasks: List[str]


class Recommendation(BaseModel):

    action: str

    reason: str

    confidence: float = Field(
        ge=0,
        le=1
    )

    requires_approval: bool = False


class FinalResponse(BaseModel):

    answer: str

    confidence: float = Field(
        ge=0,
        le=1
    )

    evidence: List[Evidence] = []


class ApprovalRequest(BaseModel):

    required: bool

    reason: Optional[str] = None