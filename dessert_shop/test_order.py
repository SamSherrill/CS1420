"""Test cases for Order class payment functionality."""

try:
    from dessert_shop import dessert as ds
    from dessert_shop.payment import PayType
except Exception:  # pragma: no cover
    import dessert as ds
    from payment import PayType

import pytest


def test_order_default_payment():
    """Test that Order defaults to CASH payment."""
    order = ds.Order()
    assert order.get_pay_type() == PayType.CASH


def test_order_set_payment_cash():
    """Test setting payment type to CASH."""
    order = ds.Order()
    order.set_pay_type(PayType.CASH)
    assert order.get_pay_type() == PayType.CASH


def test_order_set_payment_card():
    """Test setting payment type to CARD."""
    order = ds.Order()
    order.set_pay_type(PayType.CARD)
    assert order.get_pay_type() == PayType.CARD


def test_order_set_payment_phone():
    """Test setting payment type to PHONE."""
    order = ds.Order()
    order.set_pay_type(PayType.PHONE)
    assert order.get_pay_type() == PayType.PHONE


def test_order_set_invalid_payment():
    """Test that setting an invalid payment type raises ValueError."""
    order = ds.Order()
    with pytest.raises(ValueError):
        order.set_pay_type("INVALID")  # type: ignore


def test_order_get_invalid_payment():
    """Test that getting an invalid payment type raises ValueError."""
    order = ds.Order()
    # Directly set an invalid payment type (bypassing the setter)
    order._pay_type = "INVALID"  # type: ignore
    with pytest.raises(ValueError):
        order.get_pay_type()


def test_order_sort():
    """Test that Order.sort() sorts items by cost in ascending order."""
    order = ds.Order()
    # Add items in non-sorted order
    order.add(ds.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))  # cost = 3.36
    order.add(ds.Candy("Candy Corn", 1.5, 0.25))  # cost = 0.38
    order.add(ds.Cookie("Chocolate Chip", 6, 3.99))  # cost = 2.0
    order.add(ds.IceCream("Pistachio", 2, 0.79))  # cost = 1.58

    # Sort the order
    order.sort()

    # Verify items are in ascending order by cost
    assert order.order[0].calculate_cost() == 0.38  # Candy
    assert order.order[1].calculate_cost() == 1.58  # IceCream
    assert order.order[2].calculate_cost() == 2.0  # Cookie
    assert order.order[3].calculate_cost() == 3.36  # Sundae


def test_order_iterator():
    """Test that Order implements __iter__() and __next__() correctly."""
    order = ds.Order()
    order.add(ds.Candy("Candy Corn", 1.5, 0.25))
    order.add(ds.Cookie("Chocolate Chip", 6, 3.99))
    order.add(ds.IceCream("Pistachio", 2, 0.79))

    # Test using for loop (uses __iter__ and __next__ implicitly)
    items = []
    for item in order:
        items.append(item)

    assert len(items) == 3
    assert isinstance(items[0], ds.Candy)
    assert isinstance(items[1], ds.Cookie)
    assert isinstance(items[2], ds.IceCream)

    # Test explicit iterator usage
    iterator = iter(order)
    first = next(iterator)
    assert isinstance(first, ds.Candy)
    second = next(iterator)
    assert isinstance(second, ds.Cookie)
    third = next(iterator)
    assert isinstance(third, ds.IceCream)

    # Test StopIteration when exhausted
    with pytest.raises(StopIteration):
        next(iterator)
