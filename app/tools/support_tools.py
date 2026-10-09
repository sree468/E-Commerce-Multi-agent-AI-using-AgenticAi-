from app.database.connection import SessionLocal

from app.database.models import SupportCase


def get_support_cases(
    customer_id: int
):

    db = SessionLocal()

    cases = (
        db.query(SupportCase)
        .filter(
            SupportCase.customer_id == customer_id
        )
        .all()
    )

    results = []

    for case in cases:

        results.append({

            "id": case.id,

            "customer_id": (
                case.customer_id
            ),

            "issue": case.issue,

            "status": case.status
        })

    db.close()

    return results