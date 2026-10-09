from app.database.connection import SessionLocal

from app.database.models import Product


def search_products(
    query: str,
    max_price: float | None = None
):

    db = SessionLocal()

    products = (
        db.query(Product)
        .all()
    )

    results = []

    query = query.lower()

    for product in products:

        matches_query = (
            query in product.name.lower()
            or query in product.category.lower()
            or query in product.description.lower()
        )

        matches_price = (
            max_price is None
            or product.price <= max_price
        )

        if matches_query and matches_price:

            results.append({

                "id": product.id,

                "name": product.name,

                "category": product.category,

                "price": product.price,

                "stock": product.stock,

                "rating": product.rating,

                "description": product.description
            })

    db.close()

    return results