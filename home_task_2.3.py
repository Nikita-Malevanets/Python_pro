discount = 0.1  # Global discount


def create_order(price: float):
    # Calculate price after applying the global discount
    final_price = price * (1 - discount)
    print(f'Price after global discount {final_price}')

    def apply_additional_discount(discount_for_vip: float):
        nonlocal final_price  # Allows modification of final_price from the enclosing scope
        final_price = final_price * (1 - discount_for_vip)
        print(f'Price for VIP client is {final_price}')

    # Apply an additional 5% discount for VIP client
    apply_additional_discount(0.05)


# Example usage
create_order(1000)
