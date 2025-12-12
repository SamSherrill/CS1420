try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds

import pytest


def test_candy_defaults():
    c = ds.Candy()
    assert c.name == ""
    assert c.candy_weight == 0.0
    assert c.price_per_pound == 0.0


def test_candy_provided():
    c = ds.Candy("Candy Corn", 1.5, 0.25)
    assert c.name == "Candy Corn"
    assert c.candy_weight == 1.5
    assert c.price_per_pound == 0.25


def test_candy_updated():
    c = ds.Candy()
    c.name = "Gumdrops"
    c.candy_weight = 2.0
    c.price_per_pound = 0.5
    assert c.name == "Gumdrops"
    assert c.candy_weight == 2.0
    assert c.price_per_pound == 0.5


def test_candy_calculate_cost_and_tax():
    c = ds.Candy("Candy Corn", 1.5, 0.25)
    # cost = 1.5 * 0.25 = 0.375 -> 0.38
    assert c.calculate_cost() == 0.38
    # tax = round(0.38 * 0.0725, 2) = 0.03
    assert c.calculate_tax() == 0.03


def test_candy_packaging():
    c = ds.Candy("Candy Corn", 1.5, 0.25)
    assert c.packaging == "Bag"


def test_candy_can_combine_true():
    """Test that can_combine returns True for candies with same name and price."""
    candy1 = ds.Candy("Gummy Bears", 0.5, 0.25)
    candy2 = ds.Candy("Gummy Bears", 1.0, 0.25)
    assert candy1.can_combine(candy2) is True


def test_candy_can_combine_false_different_price():
    """Test that can_combine returns False for candies with same name but different price."""
    candy1 = ds.Candy("Gummy Bears", 0.5, 0.25)
    candy2 = ds.Candy("Gummy Bears", 1.0, 0.35)
    assert candy1.can_combine(candy2) is False


def test_candy_can_combine_false_different_name():
    """Test that can_combine returns False for candies with different names but same price."""
    candy1 = ds.Candy("Gummy Bears", 0.5, 0.25)
    candy2 = ds.Candy("Candy Corn", 1.0, 0.25)
    assert candy1.can_combine(candy2) is False


def test_candy_can_combine_false_not_candy():
    """Test that can_combine returns False when other item is not a Candy."""
    candy = ds.Candy("Gummy Bears", 0.5, 0.25)
    cookie = ds.Cookie("Chocolate Chip", 12, 3.99)
    assert candy.can_combine(cookie) is False


def test_candy_combine_success():
    """Test that combine correctly combines two Candy items."""
    candy1 = ds.Candy("Gummy Bears", 0.5, 0.25)
    candy2 = ds.Candy("Gummy Bears", 1.0, 0.25)
    result = candy1.combine(candy2)
    assert result is candy1  # Returns self
    assert candy1.candy_weight == 1.5  # 0.5 + 1.0
    assert candy1.calculate_cost() == 0.38  # 1.5 * 0.25 rounded


def test_candy_combine_type_error():
    """Test that combine raises TypeError when other item is not a Candy."""
    candy = ds.Candy("Gummy Bears", 0.5, 0.25)
    cookie = ds.Cookie("Chocolate Chip", 12, 3.99)
    with pytest.raises(TypeError):
        candy.combine(cookie)
