try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds


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
