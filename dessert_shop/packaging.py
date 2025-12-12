"""packaging.py

Protocol class defining packaging attribute for dessert items.

This module defines a Protocol (interface) that requires an implementing
class to have a packaging attribute of type str.
"""

from typing import Protocol


class Packaging(Protocol):
    """Protocol defining packaging attribute for items.

    Attributes
    ----------
    packaging: str
        The type of packaging used for the item (e.g., "Bag", "Box", "Bowl", "Boat")
    """

    packaging: str
