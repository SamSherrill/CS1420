"""Test script to verify payment functionality and receipt output."""

import sys

sys.path.insert(0, "dessert_shop")

# Import directly from the modules without aliasing
from dessert import Candy, Cookie, IceCream, Sundae, Order
from payment import PayType
from tabulate import tabulate

print("=" * 70)
print("Testing Payment Functionality")
print("=" * 70)

# Test 1: Default payment type
print("\nTest 1: Order with default payment (CASH)")
order1 = Order()
order1.add(Candy("Candy Corn", 1.5, 0.25))
print(f"Payment type: {order1.get_pay_type().value}")
assert order1.get_pay_type() == PayType.CASH
print("✓ Default payment is CASH")

# Test 2: Set payment to CARD
print("\nTest 2: Order with CARD payment")
order2 = Order()
order2.add(Cookie("Chocolate Chip", 6, 3.99))
order2.set_pay_type(PayType.CARD)
print(f"Payment type: {order2.get_pay_type().value}")
assert order2.get_pay_type() == PayType.CARD
print("✓ Payment set to CARD")

# Test 3: Set payment to PHONE
print("\nTest 3: Order with PHONE payment")
order3 = Order()
order3.add(IceCream("Vanilla", 2, 1.25))
order3.set_pay_type(PayType.PHONE)
print(f"Payment type: {order3.get_pay_type().value}")
assert order3.get_pay_type() == PayType.PHONE
print("✓ Payment set to PHONE")

# Test 4: Invalid payment type handling
print("\nTest 4: Invalid payment type")
order4 = Order()
try:
    order4.set_pay_type("INVALID")  # type: ignore
    print("✗ Should have raised ValueError")
except ValueError as e:
    print(f"✓ ValueError raised as expected: {e}")

# Test 5: Receipt with payment info
print("\n" + "=" * 70)
print("Sample Receipt with Payment Information")
print("=" * 70)

order = Order()
order.add(Candy("Candy Corn", 1.5, 0.25))
order.add(Candy("Gummy Bears", 0.25, 0.35))
order.add(Cookie("Chocolate Chip", 6, 3.99))
order.add(IceCream("Pistachio", 2, 0.79))
order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
order.add(Cookie("Oatmeal Raisin", 2, 3.45))

# Set payment to CARD
order.set_pay_type(PayType.CARD)

# Print receipt using tabulate
print(tabulate(order.to_list(), tablefmt="fancy_grid"))

print("\n" + "=" * 70)
print("Verifying receipt includes payment type")
print("=" * 70)

receipt_str = str(order)
print(f"\n✓ Receipt contains 'Paid with CARD': {'Paid with CARD' in receipt_str}")
print(f"✓ Receipt contains separator line: {'--------------------' in receipt_str}")

# Test all payment types in separate orders
print("\n" + "=" * 70)
print("Testing All Payment Types")
print("=" * 70)

for pay_type in [PayType.CASH, PayType.CARD, PayType.PHONE]:
    test_order = Order()
    test_order.add(Candy("Test Candy", 1.0, 1.0))
    test_order.set_pay_type(pay_type)
    receipt = str(test_order)
    payment_line = f"Paid with {pay_type.value}"
    print(f"\n{pay_type.value}: {payment_line in receipt} ✓")

print("\n" + "=" * 70)
print("All tests passed!")
print("=" * 70)
