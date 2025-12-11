"""dessert.py

Abstract DessertItem hierarchy for Dessert Shop project.

This module implements an abstract base class `DessertItem` with a
`tax_percent` attribute and abstract `calculate_cost` method. Concrete
subclasses implement cost calculation and inherit `calculate_tax` which
computes tax from the cost and `tax_percent`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
from decimal import Decimal, ROUND_HALF_UP


class DessertItem(ABC):
    """Abstract base class for dessert items.

    Attributes
    ----------
    name: str
        Name of the dessert item (default empty string)
    tax_percent: float
        Sales tax percent to apply to the item (default 7.25)
    """

    tax_percent: float = 7.25

    def __init__(self, name: str = "") -> None:
        self.name: str = name
        # instance-level copy so tests/instances can override if needed
        self.tax_percent = float(self.tax_percent)

    @abstractmethod
    def calculate_cost(self) -> float:
        """Return the cost (dollars) for this item. Implemented by subclasses."""

    def calculate_tax(self) -> float:
        """Return the tax for this item (rounded to 2 decimals)."""
        # use Decimal with ROUND_HALF_UP to match expected monetary rounding
        cost_decimal = Decimal(str(self.calculate_cost()))
        tax_decimal = cost_decimal * (Decimal(str(self.tax_percent)) / Decimal("100"))
        tax_rounded = tax_decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return float(tax_rounded)


class Candy(DessertItem):
    """Candy sold by the pound."""

    def __init__(
        self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0
    ) -> None:
        super().__init__(name)
        self.candy_weight: float = float(candy_weight)
        self.price_per_pound: float = float(price_per_pound)

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)


class Cookie(DessertItem):
    """Cookie sold by the dozen."""

    def __init__(
        self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0
    ) -> None:
        super().__init__(name)
        self.cookie_quantity: int = int(cookie_quantity)
        self.price_per_dozen: float = float(price_per_dozen)

    def calculate_cost(self) -> float:
        dozens = float(self.cookie_quantity) / 12.0
        return round(dozens * self.price_per_dozen, 2)


class IceCream(DessertItem):
    """Ice cream sold by the scoop."""

    def __init__(
        self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0
    ) -> None:
        super().__init__(name)
        self.scoop_count: int = int(scoop_count)
        self.price_per_scoop: float = float(price_per_scoop)

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)


class Sundae(IceCream):
    """Sundae: ice cream with a topping."""

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
        self.topping_price: float = float(topping_price)

    def calculate_cost(self) -> float:
        ice_cost = super().calculate_cost()
        return round(ice_cost + self.topping_price, 2)


class Order:
    """Order container for DessertItem instances."""

    def __init__(self) -> None:
        self.order: List[DessertItem] = []

    def add(self, item: DessertItem) -> None:
        self.order.append(item)

    def __len__(self) -> int:
        return len(self.order)

    def order_cost(self) -> float:
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self) -> float:
        return round(sum(item.calculate_tax() for item in self.order), 2)


__all__ = ["DessertItem", "Candy", "Cookie", "IceCream", "Sundae", "Order"]
