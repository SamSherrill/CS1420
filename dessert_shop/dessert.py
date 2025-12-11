"""dessert.py

Module providing DessertItem class hierarchy for the Dessert Shop project (Part 1).

Classes:
 - DessertItem (superclass)
 - Candy (inherits DessertItem)
 - Cookie (inherits DessertItem)
 - IceCream (inherits DessertItem)
 - Sundae (inherits IceCream)

Each subclass defines attributes and a constructor that initializes all
attributes and calls the superclass constructor as required by the assignment.
"""

from __future__ import annotations


class DessertItem:
    """Superclass for dessert shop items.

    Attributes
    ----------
    name: str
        The name of the dessert item (default empty string).
    """

    def __init__(self, name: str = "") -> None:
        self.name: str = name


class Candy(DessertItem):
    """Candy sold by the pound.

    Attributes
    ----------
    candy_weight: float
        Weight in pounds (default 0.0)
    price_per_pound: float
        Price per pound (default 0.0)
    """

    def __init__(
        self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0
    ) -> None:
        super().__init__(name)
        self.candy_weight: float = candy_weight
        self.price_per_pound: float = price_per_pound


class Cookie(DessertItem):
    """Cookie sold by the dozen.

    Attributes
    ----------
    cookie_quantity: int
        Quantity (number of cookies) (default 0)
    price_per_dozen: float
        Price per dozen (default 0.0)
    """

    def __init__(
        self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0
    ) -> None:
        super().__init__(name)
        self.cookie_quantity: int = cookie_quantity
        self.price_per_dozen: float = price_per_dozen


class IceCream(DessertItem):
    """Ice cream sold by the scoop.

    Attributes
    ----------
    scoop_count: int
        Number of scoops (default 0)
    price_per_scoop: float
        Price per scoop (default 0.0)
    """

    def __init__(
        self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0
    ) -> None:
        super().__init__(name)
        self.scoop_count: int = scoop_count
        self.price_per_scoop: float = price_per_scoop


class Sundae(IceCream):
    """Sundae: ice cream with a topping.

    Attributes
    ----------
    topping_name: str
        Name of the topping (default empty string)
    topping_price: float
        Price of the topping (default 0.0)
    """

    def __init__(
        self,
        name: str = "",
        scoop_count: int = 0,
        price_per_scoop: float = 0.0,
        topping_name: str = "",
        topping_price: float = 0.0,
    ) -> None:
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name: str = topping_name
        self.topping_price: float = topping_price


__all__ = ["DessertItem", "Candy", "Cookie", "IceCream", "Sundae"]


class Order:
    """Order is a container for DessertItem objects.

    Attributes
    ----------
    order: list
        List of DessertItem instances.
    """

    def __init__(self) -> None:
        self.order: list[DessertItem] = []

    def add(self, item: DessertItem) -> None:
        """Add a DessertItem to the order."""
        self.order.append(item)

    def __len__(self) -> int:
        """Return the number of items in the order."""
        return len(self.order)
