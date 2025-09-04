def create_product(name: str, price: float, quantity: int):
    """
    Create a product with a name, price, and quantity.
    Returns two functions:
    - get_info() -> shows current product info
    - update(price) -> updates price
    """
    current_price = price

    def get_info():
        return f"Product: {name}, Price: {current_price}"

    def update(new_price, new_quantity):
        nonlocal current_price
        current_price = new_price

    return get_info, update
