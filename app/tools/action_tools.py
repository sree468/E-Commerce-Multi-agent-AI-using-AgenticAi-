from app.database.connection import SessionLocal

from app.database.models import Order


def create_return(
    order_id: int
):

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

        return {
            "success": False,
            "message": "Order not found."
        }

    if order.status == "Cancelled":

        db.close()

        return {
            "success": False,
            "message": (
                "Cancelled order cannot "
                "be returned."
            )
        }

    order.status = "Return Requested"

    db.commit()

    db.close()

    return {

        "success": True,

        "message": (
            f"Return request created "
            f"for order {order_id}."
        )
    }


def cancel_order(
    order_id: int
):

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

        return {
            "success": False,
            "message": "Order not found."
        }

    if order.status == "Delivered":

        db.close()

        return {
            "success": False,
            "message": (
                "Delivered orders "
                "cannot be cancelled."
            )
        }

    order.status = "Cancelled"

    db.commit()

    db.close()

    return {

        "success": True,

        "message": (
            f"Order {order_id} "
            "cancelled successfully."
        )
    }