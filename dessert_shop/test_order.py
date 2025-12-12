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
