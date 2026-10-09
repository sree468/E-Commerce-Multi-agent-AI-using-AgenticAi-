from app.database.seed import (
    seed_database
)

from app.main import run_agent


def test_graph():

    seed_database()

    result = run_agent(

        user_query=(
            "Where is my order?"
        ),

        customer_id=1,

        order_id=1001
    )

    assert result is not None

    assert (
        "intent"
        in result
    )

    assert (
        "analysis"
        in result
    )