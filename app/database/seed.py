from app.database.connection import engine, SessionLocal
from app.database.models import (
    Base,
    Customer,
    Product,
    Order,
    SupportCase
)


def seed_database():

    # Create database tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:

        # Check whether customers already exist
        if db.query(Customer).count() == 0:

            customers = [
                Customer(
                    id=1,
                    name="Rahul",
                    email="rahul@example.com",
                    city="Hyderabad"
                ),

                Customer(
                    id=2,
                    name="Priya",
                    email="priya@example.com",
                    city="Bangalore"
                ),

                Customer(
                    id=3,
                    name="Arjun",
                    email="arjun@example.com",
                    city="Chennai"
                )
            ]

            db.add_all(customers)

        # Check whether products already exist
        if db.query(Product).count() == 0:

            products = [

                Product(
                    id=101,
                    name="Samsung Galaxy S25",
                    category="Mobile",
                    price=69999,
                    stock=20,
                    rating=4.6,
                    description="Latest Samsung flagship smartphone"
                ),

                Product(
                    id=102,
                    name="iPhone 16",
                    category="Mobile",
                    price=79999,
                    stock=15,
                    rating=4.7,
                    description="Apple iPhone with advanced camera"
                ),

                Product(
                    id=103,
                    name="HP Pavilion Laptop",
                    category="Laptop",
                    price=59999,
                    stock=12,
                    rating=4.3,
                    description="HP laptop suitable for students and professionals"
                ),

                Product(
                    id=104,
                    name="Dell Inspiron Laptop",
                    category="Laptop",
                    price=64999,
                    stock=10,
                    rating=4.4,
                    description="Dell laptop for productivity and everyday work"
                )
            ]

            db.add_all(products)

        # Check whether orders already exist
        if db.query(Order).count() == 0:

            orders = [

                Order(
                    id=1001,
                    customer_id=1,
                    product_id=101,
                    quantity=1,
                    status="Shipped",
                    payment_status="Paid",
                    delivery_status="Delayed",
                    total_amount=69999
                ),

                Order(
                    id=1002,
                    customer_id=2,
                    product_id=103,
                    quantity=1,
                    status="Delivered",
                    payment_status="Paid",
                    delivery_status="Delivered",
                    total_amount=59999
                ),

                Order(
                    id=1003,
                    customer_id=3,
                    product_id=104,
                    quantity=1,
                    status="Processing",
                    payment_status="Paid",
                    delivery_status="Not Shipped",
                    total_amount=64999
                )
            ]

            db.add_all(orders)

        # Check whether support cases exist
        if db.query(SupportCase).count() == 0:

            support_cases = [

                SupportCase(
                    id=5001,
                    customer_id=1,
                    issue="Order delivery delayed",
                    status="Open"
                ),

                SupportCase(
                    id=5002,
                    customer_id=2,
                    issue="Product return request",
                    status="Open"
                )
            ]

            db.add_all(support_cases)

        # Save everything
        db.commit()

        print("==========================================")
        print("Database initialized successfully!")
        print("==========================================")
        print("Customers      :", db.query(Customer).count())
        print("Products       :", db.query(Product).count())
        print("Orders         :", db.query(Order).count())
        print("Support Cases  :", db.query(SupportCase).count())
        print("==========================================")

    except Exception as e:

        db.rollback()

        print("Database initialization failed!")
        print("Error:", e)

        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()