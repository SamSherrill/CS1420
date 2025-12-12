"""dessert.py

Abstract DessertItem hierarchy for Dessert Shop project.

Part 10: This module implements an abstract base class `DessertItem` that
inherits from the Packaging Protocol. DessertItem implements comparison
operators to enable sorting by cost. The Order class implements the Payable
Protocol to track payment methods and includes a sort() method. Candy and
Cookie classes implement the Combinable Protocol to allow combining like items.
Order is iterable via __iter__() and __next__(). It has a `tax_percent`
attribute and abstract `calculate_cost` method. Concrete subclasses implement
cost calculation, set their packaging type, and inherit `calculate_tax` which
computes tax from the cost and `tax_percent`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
from decimal import Decimal, ROUND_HALF_UP
from packaging import Packaging
from payment import PayType, Payable
from combine import Combinable


class DessertItem(ABC, Packaging):
    """Abstract base class for dessert items.

    Attributes
    ----------
    name: str
        Name of the dessert item (default empty string)
    tax_percent: float
        Sales tax percent to apply to the item (default 7.25)
    packaging: str
        Type of packaging for the item (default None)
    """

    tax_percent: float = 7.25

    def __init__(self, name: str = "") -> None:
        self.name: str = name
        # instance-level copy so tests/instances can override if needed
        self.tax_percent = float(self.tax_percent)
        self.packaging: str = None

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

    def __eq__(self, other: object) -> bool:
        """Check if two dessert items have equal cost."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other: object) -> bool:
        """Check if two dessert items have different cost."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() != other.calculate_cost()

    def __lt__(self, other: object) -> bool:
        """Check if this item costs less than another."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() < other.calculate_cost()

    def __le__(self, other: object) -> bool:
        """Check if this item costs less than or equal to another."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() <= other.calculate_cost()

    def __gt__(self, other: object) -> bool:
        """Check if this item costs more than another."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() > other.calculate_cost()

    def __ge__(self, other: object) -> bool:
        """Check if this item costs more than or equal to another."""
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.calculate_cost() >= other.calculate_cost()


class Candy(DessertItem):
    """Candy sold by the pound."""

    def __init__(
        self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0
    ) -> None:
        super().__init__(name)
        self.candy_weight: float = float(candy_weight)
        self.price_per_pound: float = float(price_per_pound)
        self.packaging = "Bag"

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self) -> str:
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n-    {self.candy_weight} lbs. @ ${self.price_per_pound:.2f}/lb:, ${cost:.2f}, [Tax: ${tax:.2f}]"

    def can_combine(self, other: "Candy") -> bool:
        """Check if this candy can be combined with another candy.

        Parameters
        ----------
        other : Candy
            The other candy to check for compatibility

        Returns
        -------
        bool
            True if both are Candy instances with same name and price per pound
        """
        return (
            isinstance(other, Candy)
            and self.name == other.name
            and self.price_per_pound == other.price_per_pound
        )

    def combine(self, other: "Candy") -> "Candy":
        """Combine this candy with another candy by adding weights.

        Parameters
        ----------
        other : Candy
            The other candy to combine with this one

        Returns
        -------
        Candy
            The modified self after combining

        Raises
        ------
        TypeError
            If other is not a Candy instance
        """
        if not isinstance(other, Candy):
            raise TypeError("Can only combine with another Candy instance")
        self.candy_weight += other.candy_weight
        return self


class Cookie(DessertItem):
    """Cookie sold by the dozen."""

    def __init__(
        self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0
    ) -> None:
        super().__init__(name)
        self.cookie_quantity: int = int(cookie_quantity)
        self.price_per_dozen: float = float(price_per_dozen)
        self.packaging = "Box"

    def calculate_cost(self) -> float:
        dozens = float(self.cookie_quantity) / 12.0
        return round(dozens * self.price_per_dozen, 2)

    def __str__(self) -> str:
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} Cookies ({self.packaging})\n-    {self.cookie_quantity} cookies. @ ${self.price_per_dozen:.2f}/dozen:, ${cost:.2f}, [Tax: ${tax:.2f}]"

    def can_combine(self, other: "Cookie") -> bool:
        """Check if this cookie can be combined with another cookie.

        Parameters
        ----------
        other : Cookie
            The other cookie to check for compatibility

        Returns
        -------
        bool
            True if both are Cookie instances with same name and price per dozen
        """
        return (
            isinstance(other, Cookie)
            and self.name == other.name
            and self.price_per_dozen == other.price_per_dozen
        )

    def combine(self, other: "Cookie") -> "Cookie":
        """Combine this cookie with another cookie by adding quantities.

        Parameters
        ----------
        other : Cookie
            The other cookie to combine with this one

        Returns
        -------
        Cookie
            The modified self after combining

        Raises
        ------
        TypeError
            If other is not a Cookie instance
        """
        if not isinstance(other, Cookie):
            raise TypeError("Can only combine with another Cookie instance")
        self.cookie_quantity += other.cookie_quantity
        return self


class IceCream(DessertItem):
    """Ice cream sold by the scoop."""

    def __init__(
        self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0
    ) -> None:
        super().__init__(name)
        self.scoop_count: int = int(scoop_count)
        self.price_per_scoop: float = float(price_per_scoop)
        self.packaging = "Bowl"

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self) -> str:
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} Ice Cream ({self.packaging})\n-    {self.scoop_count} scoops. @ ${self.price_per_scoop:.2f}/scoop:, ${cost:.2f}, [Tax: ${tax:.2f}]"


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
        self.packaging = "Boat"

    def calculate_cost(self) -> float:
        ice_cost = super().calculate_cost()
        return round(ice_cost + self.topping_price, 2)

    def __str__(self) -> str:
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.topping_name} {self.name} Sundae ({self.packaging})\n-    {self.scoop_count} scoops. @ ${self.price_per_scoop:.2f}/scoop\n-    {self.topping_name} topping @ ${self.topping_price:.2f}:, ${cost:.2f}, [Tax: ${tax:.2f}]"


class Order(Payable):
    """Order container for DessertItem instances.

    Implements Payable interface for payment method tracking.
    Implements iterator protocol via __iter__() and __next__().
    Combines like items if they implement Combinable protocol.
    """

    def __init__(self) -> None:
        self.order: List[DessertItem] = []
        self._pay_type: PayType = PayType.CASH
        self._current_index: int = 0

    def add(self, item: DessertItem) -> None:
        """Add an item to the order, combining with existing items if possible.

        If the item implements Combinable protocol and can be combined with
        an existing item in the order, it will be merged. Otherwise, it will
        be added as a new item.

        Parameters
        ----------
        item : DessertItem
            The item to add to the order
        """
        # Check if item is Combinable
        if isinstance(item, Combinable):
            # Try to find an existing item to combine with
            for existing_item in self.order:
                if isinstance(existing_item, Combinable) and existing_item.can_combine(
                    item
                ):
                    # Combine the new item into the existing one
                    existing_item.combine(item)
                    return

        # If not combinable or no match found, add as new item
        self.order.append(item)

    def __iter__(self):
        """Return an iterator for the order.

        Returns
        -------
        Order
            Self, as Order implements the iterator protocol
        """
        self._current_index = 0
        return self

    def __next__(self) -> DessertItem:
        """Return the next item in the order.

        Returns
        -------
        DessertItem
            The next item in the order

        Raises
        ------
        StopIteration
            When there are no more items
        """
        if self._current_index >= len(self.order):
            raise StopIteration
        item = self.order[self._current_index]
        self._current_index += 1
        return item

    def __len__(self) -> int:
        return len(self.order)

    def order_cost(self) -> float:
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self) -> float:
        return round(sum(item.calculate_tax() for item in self.order), 2)

    def get_pay_type(self) -> PayType:
        """Return the payment type for this order.

        Returns
        -------
        PayType
            The payment type for this order

        Raises
        ------
        ValueError
            If the stored payment type is not a valid PayType
        """
        if not isinstance(self._pay_type, PayType):
            raise ValueError(f"Invalid payment type: {self._pay_type}")
        return self._pay_type

    def set_pay_type(self, payment_method: PayType) -> None:
        """Set the payment type for this order.

        Parameters
        ----------
        payment_method : PayType
            The payment method to use

        Raises
        ------
        ValueError
            If payment_method is not a valid PayType
        """
        if not isinstance(payment_method, PayType):
            raise ValueError(f"Invalid payment type: {payment_method}")
        self._pay_type = payment_method

    def sort(self) -> None:
        """Sort the order items by cost in ascending order."""
        self.order.sort()

    def __str__(self) -> str:
        """Return string representation of the order with header and items."""
        lines = []
        lines.append("Name, Cost, Tax")
        lines.append("----------, ----------, ----------")

        # Use banker's rounding for display (consistent with Part 5)
        for item in self.order:
            lines.append(str(item))

        lines.append("----------, ----------, ----------")
        lines.append(f"Total number of items in order:, {len(self.order)}")

        subtotal = self.order_cost()
        # Use banker's rounding for display tax
        display_tax = sum(
            round(item.calculate_cost() * (item.tax_percent / 100.0), 2)
            for item in self.order
        )
        total = round(subtotal + display_tax, 2)

        lines.append(f"Order Subtotals:, ${subtotal:.2f}, [Tax: ${display_tax:.2f}]")
        lines.append(f"Order Total:, , ${total:.2f}")
        lines.append("--------------------")
        lines.append(f"Paid with {self.get_pay_type().value}")

        return "\n".join(lines)

    def to_list(self) -> List[List[str]]:
        """Convert the string representation of the order to a 2D list."""
        order_str = str(self)
        lines = order_str.split("\n")
        return [line.split(", ") for line in lines]


__all__ = ["DessertItem", "Candy", "Cookie", "IceCream", "Sundae", "Order"]
