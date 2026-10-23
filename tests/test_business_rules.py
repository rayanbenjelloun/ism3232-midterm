from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    get_rental_discount,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def test_calculate_rental_cost():
    assert round(calculate_rental_cost(60.00, 2), 2) == 120.00


def test_rental_discount_below_three_days():
    assert get_rental_discount(2) == 0.0


def test_rental_discount_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_rental_discount_at_six_days():
    assert get_rental_discount(6) == 0.10


def test_rental_discount_at_seven_days():
    assert get_rental_discount(7) == 0.20


def test_rental_discount_contractor_two_days():
    assert get_rental_discount(2, contractor=True) == 0.10


def test_rental_discount_contractor_seven_days():
    assert get_rental_discount(7, contractor=True) == 0.20


def test_quote_adds_damage_waiver():
    assert round(calculate_quote(60.00, 2), 2) == 145.00


def test_quote_at_damage_waiver_limit():
    assert round(calculate_quote(150.00, 1), 2) == 150.00


def test_quote_one_cent_below_damage_waiver_limit():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_quote_applies_ten_percent_discount():
    assert round(calculate_quote(85.00, 4), 2) == 306.00


def test_quote_applies_twenty_percent_discount():
    assert round(calculate_quote(120.00, 10), 2) == 960.00


def test_quote_contractor_discount_before_damage_waiver():
    assert round(calculate_quote(60.00, 2, contractor=True), 2) == 133.00


def test_deposit_below_limit():
    assert requires_deposit(999.99) is False


def test_deposit_at_limit():
    assert requires_deposit(1000.00) is True


def test_deposit_above_limit():
    assert requires_deposit(1000.01) is True


def test_inspection_below_required_days():
    assert needs_inspection(4, 800.01) is False


def test_inspection_at_required_days():
    assert needs_inspection(5, 800.01) is True


def test_inspection_at_quote_limit():
    assert needs_inspection(5, 800.00) is False


def test_inspection_below_quote_limit():
    assert needs_inspection(5, 799.99) is False


def test_total_quoted_empty():
    assert round(total_quoted([]), 2) == 0.00


def test_total_quoted_one_rental():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    ]
    assert round(total_quoted(rentals), 2) == 145.00


def test_total_quoted_multiple_rentals():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    ]
    assert round(total_quoted(rentals), 2) == 584.00
