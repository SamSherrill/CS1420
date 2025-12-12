try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds


def test_icecream_defaults():
    i = ds.IceCream()
    assert i.name == ""
    assert i.scoop_count == 0
    assert i.price_per_scoop == 0.0


def test_icecream_provided():
    i = ds.IceCream("Vanilla", 2, 1.25)
    assert i.name == "Vanilla"
    assert i.scoop_count == 2
    assert i.price_per_scoop == 1.25


def test_icecream_updated():
    i = ds.IceCream()
    i.name = "Chocolate"
    i.scoop_count = 3
    i.price_per_scoop = 0.99
    assert i.name == "Chocolate"
    assert i.scoop_count == 3
    assert i.price_per_scoop == 0.99


def test_icecream_calculate_cost_and_tax():
    i = ds.IceCream("Pistachio", 2, 0.79)
    # cost = 2 * 0.79 = 1.58
    assert i.calculate_cost() == 1.58
    # tax = round(1.58 * 0.0725, 2) = 0.11
    assert i.calculate_tax() == 0.11


def test_icecream_packaging():
    i = ds.IceCream("Vanilla", 2, 1.25)
    assert i.packaging == "Bowl"
