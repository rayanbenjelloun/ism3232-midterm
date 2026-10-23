# business_rules.py
# Ridgeline Tool Rental

SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7
NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.1
LONG_RENTAL_DISCOUNT = 0.2


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before any discount."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Returns the discount rate as a decimal"""
    if days >= LONG_RENTAL_DAYS:
        return LONG_RENTAL_DISCOUNT
    elif days >= SHORT_RENTAL_DAYS or contractor:
        return STANDARD_DISCOUNT
    else:
        return NO_DISCOUNT
