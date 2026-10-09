from app.database.seed import (
    seed_database
)

from app.tools.order_tools import (
    get_order
)

from app.tools.catalog_tools import (
    search_products
)


def test_order():

    seed_database()

    order = get_order(
        1001
    )

    assert order is not None

    assert order["id"] == 1001


def test_product_search():

    seed_database()

    products = search_products(
        "mobile"
    )

    assert len(products) > 0