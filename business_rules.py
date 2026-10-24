# business_rules.py
# Ridgeline Tool Rental

SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7
NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.1
LONG_RENTAL_DISCOUNT = 0.2
DAMAGE_WAIVER_LIMIT = 150.00
DAMAGE_WAIVER_FEE = 25.00
DEPOSIT_LIMIT = 1000.00
INSPECTION_DAYS = 5
INSPECTION_QUOTE_LIMIT = 800.00


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


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the discounted rental cost plus any damage waiver."""
    rental_cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    quote = rental_cost * (1 - discount)

    if quote < DAMAGE_WAIVER_LIMIT:
        quote += DAMAGE_WAIVER_FEE
    return quote


def requires_deposit(quote: float) -> bool:
    """Return whether the quote requires a deposit."""
    return quote >= DEPOSIT_LIMIT


def needs_inspection(days: int, quote: float) -> bool:
    """Return whether the rental requires an inspection."""
    return days >= INSPECTION_DAYS and quote > INSPECTION_QUOTE_LIMIT


def total_quoted(rentals: list) -> float:
    """Return the total quoted amount for all rentals"""
    total = 0.0

    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        total += quote
    return total


def largest_rental(rentals: list) -> str:
    """Return the customer with the largest quote, keeping the first tie."""
    if not rentals:
        return ""

    largest_customer = rentals[0]["customer"]
    largest_quote = calculate_quote(
        rentals[0]["daily_rate"], rentals[0]["days"], rentals[0]["contractor"]
    )

    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        if quote > largest_quote:
            largest_quote = quote
            largest_customer = rental["customer"]
    return largest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Return a formatted rental report line."""
    if deposit:
        deposit_text = "yes"
    else:
        deposit_text = "no"

    if inspection:
        inspection_text = "yes"
    else:
        inspection_text = "no"
    return (
        f"{customer}: ${quote:.2f} | deposit: {deposit_text} | "
        f"inspection: {inspection_text}"
    )
