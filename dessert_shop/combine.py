"""combine.py

Protocol class for combining similar dessert items.

This module defines a Protocol (interface) for items that can be combined
if they meet certain criteria (e.g., same name and price).
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Combinable(Protocol):
    """Protocol defining interface for items that can be combined.

    Items implementing this protocol can be merged together if they
    are similar enough (e.g., same product at same price).

    Methods
    -------
    can_combine(other: "Combinable") -> bool
        Check if this item can be combined with another item
    combine(other: "Combinable") -> "Combinable"
        Combine this item with another item (destructive operation)
    """

    def can_combine(self, other: "Combinable") -> bool:
        """Check if this item can be combined with another item.

        Parameters
        ----------
        other : Combinable
            The other item to check for compatibility

        Returns
        -------
        bool
            True if items can be combined, False otherwise
        """
        ...

    def combine(self, other: "Combinable") -> "Combinable":
        """Combine this item with another item.

        This is a destructive operation that modifies self by adding
        the quantity/weight from other.

        Parameters
        ----------
        other : Combinable
            The other item to combine with this one

        Returns
        -------
        Combinable
            The modified self after combining

        Raises
        ------
        TypeError
            If other is not the same type as self
        """
        ...
