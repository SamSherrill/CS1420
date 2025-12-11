try:
    from dessert_shop import dessert as ds
except Exception:  # pragma: no cover
    import dessert as ds


def test_sundae_defaults():
    s = ds.Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0


def test_sundae_provided():
    s = ds.Sundae("Strawberry", 2, 1.0, "Sprinkles", 0.25)
    assert s.name == "Strawberry"
    assert s.scoop_count == 2
    assert s.price_per_scoop == 1.0
    assert s.topping_name == "Sprinkles"
    assert s.topping_price == 0.25


def test_sundae_updated():
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


def test_sundae_calculate_cost_and_tax():
    s = ds.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    # ice cost = 3 * 0.69 = 2.07; total = 2.07 + 1.29 = 3.36
    assert s.calculate_cost() == 3.36
    # tax = round(3.36 * 0.0725, 2) = 0.24
    assert s.calculate_tax() == 0.24
