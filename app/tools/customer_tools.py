from app.database.connection import SessionLocal

from app.database.models import Customer


def get_customer(
    customer_id: int
):

    db = SessionLocal()

    customer = (
        db.query(Customer)
        .filter(
            Customer.id == customer_id
        )
        .first()
    )

    if not customer:

        db.close()

        return None

    result = {

        "id": customer.id,

        "name": customer.name,

        "email": customer.email,

        "city": customer.city
    }

    db.close()

    return result