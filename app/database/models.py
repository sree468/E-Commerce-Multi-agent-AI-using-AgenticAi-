from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text
)

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Customer(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    email = Column(String)

    city = Column(String)


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    category = Column(String)

    price = Column(Float)

    stock = Column(Integer)

    rating = Column(Float)

    description = Column(Text)


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True
    )

    customer_id = Column(Integer)

    product_id = Column(Integer)

    quantity = Column(Integer)

    status = Column(String)

    payment_status = Column(String)

    delivery_status = Column(String)

    total_amount = Column(Float)


class SupportCase(Base):

    __tablename__ = "support_cases"

    id = Column(
        Integer,
        primary_key=True
    )

    customer_id = Column(Integer)

    issue = Column(Text)

    status = Column(String)