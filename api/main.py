from fastapi import FastAPI

from pydantic import BaseModel

from app.main import run_agent


app = FastAPI(

    title=(
        "E-Commerce Multi-Agent "
        "Operations API"
    ),

    version="1.0.0"
)


class QueryRequest(BaseModel):

    query: str

    customer_id: int | None = None

    order_id: int | None = None


@app.get("/")
def home():

    return {

        "message": (
            "E-Commerce Multi-Agent "
            "Operations API"
        )
    }


@app.post(
    "/agent/run"
)
def execute_agent(
    request: QueryRequest
):

    result = run_agent(

        user_query=request.query,

        customer_id=request.customer_id,

        order_id=request.order_id
    )

    return {

        "intent": result.get(
            "intent"
        ),

        "analysis": result.get(
            "analysis"
        ),

        "validation": result.get(
            "validation"
        ),

        "action_result": result.get(
            "action_result"
        ),

        "evidence": result.get(
            "evidence"
        ),

        "audit_log": result.get(
            "audit_log"
        )
    }