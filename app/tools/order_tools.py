from app.database.connection import SessionLocal

from app.database.models import Order


def get_order(order_id: int):

    db = SessionLocal()

    order = (
        db.query(Order)
        .filter(
            Order.id == order_id
        )
        .first()
    )

    if not order:

        db.close()

        return None

    result = {

        "id": order.id,

        "customer_id": order.customer_id,

        "product_id": order.product_id,

        "quantity": order.quantity,

        "status": order.status,

        "payment_status": order.payment_status,

        "delivery_status": order.delivery_status,

        "total_amount": order.total_amount
    }

    db.close()

    return result


def get_customer_orders(
    customer_id: int
):

    db = SessionLocal()

    orders = (
        db.query(Order)
        .filter(
            Order.customer_id == customer_id
        )
        .all()
    )

    results = []

    for order in orders:

        results.append({

            "id": order.id,

            "status": order.status,

            "payment_status": (
                order.payment_status
            ),

            "delivery_status": (
                order.delivery_status
            ),

            "total_amount": (
                order.total_amount
            )
        })

    db.close()

    return results