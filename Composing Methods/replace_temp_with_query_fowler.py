"""This program takes in a quantity and item price
    and then returns the discounted price of said item"""


def get_price(quantity, item_price):
    """Gets discounted price"""
    base_price = quantity * item_price
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor
