"""payment.py

Protocol class and enumeration for payment methods.

This module defines a Protocol (interface) for payment functionality and
an enumeration of valid payment types.
"""

from enum import Enum
from typing import Protocol


class PayType(Enum):
    """Enumeration of valid payment types.

    Attributes
    ----------
    CASH : str
        Cash payment
    CARD : str
        Card payment (credit/debit)
    PHONE : str
        Phone payment (mobile payment)
    """

    CASH = "CASH"
    CARD = "CARD"
    PHONE = "PHONE"


class Payable(Protocol):
    """Protocol defining payment interface for orders.

    Methods
    -------
    get_pay_type() -> PayType
        Return the payment type for this order
    set_pay_type(payment_method: PayType) -> None
        Set the payment type for this order
    """

    def get_pay_type(self) -> PayType:
        """Return the payment type for this order."""
        ...

    def set_pay_type(self, payment_method: PayType) -> None:
        """Set the payment type for this order."""
        ...
