try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds


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
