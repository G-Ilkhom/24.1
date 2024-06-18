import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создание продукта в страйпе"""
    title_product = f"{instance.course}" if instance.course else instance.lesson
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def create_stripe_price(amount, stripe_product_id):
    """Создание цены в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=stripe_product_id,
    )


def create_stripe_session(price):
    """Создание сессии на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
