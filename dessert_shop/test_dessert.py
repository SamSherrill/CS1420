"""Pytest unit tests for Dessert Shop classes (Part 3).

Tests cover default values, provided values, and updated values for each
of the following classes: DessertItem, Candy, Cookie, IceCream, Sundae.
"""

from __future__ import annotations

try:
    # When running pytest from repository root
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover - fallback for running tests from package dir
    # When running pytest from the dessert_shop directory
    import dessert as ds


def test_dessertitem_tax_and_instance() -> None:
    # DessertItem is abstract; test via concrete subclass (Candy)
    c = ds.Candy("Candy Corn", 1.5, 0.25)
    # default tax_percent should be present and default to 7.25
    assert hasattr(c, "tax_percent")
    assert float(c.tax_percent) == 7.25
    # calculate_tax should use calculate_cost and tax_percent
    cost = c.calculate_cost()
    tax = c.calculate_tax()
    assert tax == round(cost * (c.tax_percent / 100.0), 2)


def test_candy_defaults() -> None:
    c = ds.Candy()
    assert c.name == ""
    assert c.candy_weight == 0.0
    assert c.price_per_pound == 0.0


def test_candy_provided() -> None:
    c = ds.Candy("Candy Corn", 1.5, 0.25)
    assert c.name == "Candy Corn"
    assert c.candy_weight == 1.5
    assert c.price_per_pound == 0.25


def test_candy_updated() -> None:
    c = ds.Candy()
    c.name = "Gumdrops"
    c.candy_weight = 2.0
    c.price_per_pound = 0.5
    assert c.name == "Gumdrops"
    assert c.candy_weight == 2.0
    assert c.price_per_pound == 0.5


def test_cookie_defaults() -> None:
    k = ds.Cookie()
    assert k.name == ""
    assert k.cookie_quantity == 0
    assert k.price_per_dozen == 0.0


def test_cookie_provided() -> None:
    k = ds.Cookie("ChocChip", 12, 3.99)
    assert k.name == "ChocChip"
    assert k.cookie_quantity == 12
    assert k.price_per_dozen == 3.99


def test_cookie_updated() -> None:
    k = ds.Cookie()
    k.name = "Oatmeal"
    k.cookie_quantity = 24
    k.price_per_dozen = 4.5
    assert k.name == "Oatmeal"
    assert k.cookie_quantity == 24
    assert k.price_per_dozen == 4.5


def test_icecream_defaults() -> None:
    i = ds.IceCream()
    assert i.name == ""
    assert i.scoop_count == 0
    assert i.price_per_scoop == 0.0


def test_icecream_provided() -> None:
    i = ds.IceCream("Vanilla", 2, 1.25)
    assert i.name == "Vanilla"
    assert i.scoop_count == 2
    assert i.price_per_scoop == 1.25


def test_icecream_updated() -> None:
    i = ds.IceCream()
    i.name = "Chocolate"
    i.scoop_count = 3
    i.price_per_scoop = 0.99
    assert i.name == "Chocolate"
    assert i.scoop_count == 3
    assert i.price_per_scoop == 0.99


def test_sundae_defaults() -> None:
    s = ds.Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0


def test_sundae_provided() -> None:
    s = ds.Sundae("Strawberry", 2, 1.0, "Sprinkles", 0.25)
    assert s.name == "Strawberry"
    assert s.scoop_count == 2
    assert s.price_per_scoop == 1.0
    assert s.topping_name == "Sprinkles"
    assert s.topping_price == 0.25


def test_sundae_updated() -> None:
    s = ds.Sundae()
    s.name = "Banana"
    s.scoop_count = 1
    s.price_per_scoop = 0.75
    s.topping_name = "Caramel"
    s.topping_price = 0.5
    assert s.name == "Banana"
    assert s.scoop_count == 1
    assert s.price_per_scoop == 0.75
    assert s.topping_name == "Caramel"
    assert s.topping_price == 0.5


def test_dessert_item_comparison_eq() -> None:
    """Test == operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 2.0)  # cost = 2.0
    candy2 = ds.Candy("Candy2", 1.0, 2.0)  # cost = 2.0
    assert candy1 == candy2


def test_dessert_item_comparison_ne() -> None:
    """Test != operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 2.0)  # cost = 2.0
    candy2 = ds.Candy("Candy2", 1.0, 3.0)  # cost = 3.0
    assert candy1 != candy2


def test_dessert_item_comparison_lt() -> None:
    """Test < operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 2.0)  # cost = 2.0
    candy2 = ds.Candy("Candy2", 1.0, 3.0)  # cost = 3.0
    assert candy1 < candy2


def test_dessert_item_comparison_le() -> None:
    """Test <= operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 2.0)  # cost = 2.0
    candy2 = ds.Candy("Candy2", 1.0, 3.0)  # cost = 3.0
    candy3 = ds.Candy("Candy3", 1.0, 2.0)  # cost = 2.0
    assert candy1 <= candy2
    assert candy1 <= candy3


def test_dessert_item_comparison_gt() -> None:
    """Test > operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 3.0)  # cost = 3.0
    candy2 = ds.Candy("Candy2", 1.0, 2.0)  # cost = 2.0
    assert candy1 > candy2


def test_dessert_item_comparison_ge() -> None:
    """Test >= operator for dessert items."""
    candy1 = ds.Candy("Candy1", 1.0, 3.0)  # cost = 3.0
    candy2 = ds.Candy("Candy2", 1.0, 2.0)  # cost = 2.0
    candy3 = ds.Candy("Candy3", 1.0, 3.0)  # cost = 3.0
    assert candy1 >= candy2
    assert candy1 >= candy3
