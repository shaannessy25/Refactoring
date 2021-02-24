
"""This file finds adjusted capital"""


def get_adjusted_capital(capital, rate, duration, income):
    """This function calculates capital"""

    result = 0
    ADJUSTMENT_FACTOR = 0.7
    if (capital > 0 or (rate > 0 and duration > 0)):
        result = (income / duration) * ADJUSTMENT_FACTOR
    return result


adjusted_capital = get_adjusted_capital(50000, 4, 10, 10000)
print(adjusted_capital)
print(adjusted_capital)
