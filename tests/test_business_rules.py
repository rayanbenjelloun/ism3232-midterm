from business_rules import calculate_rental_cost, get_rental_discount


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
