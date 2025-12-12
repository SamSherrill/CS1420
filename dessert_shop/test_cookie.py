try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds

import pytest


def test_cookie_defaults():
    k = ds.Cookie()
    assert k.name == ""
    assert k.cookie_quantity == 0
    assert k.price_per_dozen == 0.0


def test_cookie_provided():
    k = ds.Cookie("ChocChip", 12, 3.99)
    assert k.name == "ChocChip"
    assert k.cookie_quantity == 12
    assert k.price_per_dozen == 3.99


def test_cookie_updated():
    k = ds.Cookie()
    k.name = "Oatmeal"
    k.cookie_quantity = 24
    k.price_per_dozen = 4.5
    assert k.name == "Oatmeal"
    assert k.cookie_quantity == 24
    assert k.price_per_dozen == 4.5


def test_cookie_calculate_cost_and_tax():
    # 6 cookies -> 0.5 dozen * 3.99 = 1.995 -> 2.0
    k = ds.Cookie("TestCookie", 6, 3.99)
    assert k.calculate_cost() == 2.0
    # tax = round(2.0 * 0.0725, 2) = 0.15
    assert k.calculate_tax() == 0.15


def test_cookie_packaging():
    k = ds.Cookie("ChocChip", 12, 3.99)
    assert k.packaging == "Box"


def test_cookie_can_combine_true():
    """Test that can_combine returns True for cookies with same name and price per dozen."""
    cookie1 = ds.Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = ds.Cookie("Chocolate Chip", 12, 3.99)
    assert cookie1.can_combine(cookie2) is True


def test_cookie_can_combine_false_different_price():
    """Test that can_combine returns False for cookies with same name but different price."""
    cookie1 = ds.Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = ds.Cookie("Chocolate Chip", 12, 4.99)
    assert cookie1.can_combine(cookie2) is False


def test_cookie_can_combine_false_different_name():
    """Test that can_combine returns False for cookies with different names but same price."""
    cookie1 = ds.Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = ds.Cookie("Oatmeal Raisin", 12, 3.99)
    assert cookie1.can_combine(cookie2) is False


def test_cookie_can_combine_false_not_cookie():
    """Test that can_combine returns False when other item is not a Cookie."""
    cookie = ds.Cookie("Chocolate Chip", 6, 3.99)
    candy = ds.Candy("Gummy Bears", 0.5, 0.25)
    assert cookie.can_combine(candy) is False


def test_cookie_combine_success():
    """Test that combine correctly combines two Cookie items."""
    cookie1 = ds.Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = ds.Cookie("Chocolate Chip", 12, 3.99)
    result = cookie1.combine(cookie2)
    assert result is cookie1  # Returns self
    assert cookie1.cookie_quantity == 18  # 6 + 12
    assert cookie1.calculate_cost() == 5.99  # 18/12 * 3.99 = 5.985 rounded to 5.99


def test_cookie_combine_type_error():
    """Test that combine raises TypeError when other item is not a Cookie."""
    cookie = ds.Cookie("Chocolate Chip", 6, 3.99)
    candy = ds.Candy("Gummy Bears", 0.5, 0.25)
    with pytest.raises(TypeError):
        cookie.combine(candy)
