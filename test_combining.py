"""Test script to verify combining functionality."""

import sys

sys.path.insert(0, "dessert_shop")

from dessert import Candy, Cookie, IceCream, Sundae, Order
from payment import PayType
from tabulate import tabulate

print("=" * 70)
print("Testing Combinable Functionality")
print("=" * 70)

# Test 1: Candy combining
print("\nTest 1: Combining Candy items")
candy1 = Candy("Gummy Bears", 0.5, 0.25)
candy2 = Candy("Gummy Bears", 1.0, 0.25)
print(f"  Candy 1: {candy1.name}, {candy1.candy_weight} lbs @ ${candy1.price_per_pound}/lb")
print(f"  Candy 2: {candy2.name}, {candy2.candy_weight} lbs @ ${candy2.price_per_pound}/lb")
print(f"  can_combine: {candy1.can_combine(candy2)}")

candy1.combine(candy2)
print(f"  After combine: {candy1.candy_weight} lbs (expected 1.5)")
assert candy1.candy_weight == 1.5
print("  ✓ Candy combined successfully")

# Test 2: Cookie combining
print("\nTest 2: Combining Cookie items")
cookie1 = Cookie("Chocolate Chip", 6, 3.99)
cookie2 = Cookie("Chocolate Chip", 12, 3.99)
print(f"  Cookie 1: {cookie1.name}, {cookie1.cookie_quantity} cookies @ ${cookie1.price_per_dozen}/dozen")
print(f"  Cookie 2: {cookie2.name}, {cookie2.cookie_quantity} cookies @ ${cookie2.price_per_dozen}/dozen")
print(f"  can_combine: {cookie1.can_combine(cookie2)}")

cookie1.combine(cookie2)
print(f"  After combine: {cookie1.cookie_quantity} cookies (expected 18)")
assert cookie1.cookie_quantity == 18
print("  ✓ Cookie combined successfully")

# Test 3: Different items cannot combine
print("\nTest 3: Different items cannot combine")
candy = Candy("Candy Corn", 1.0, 0.25)
cookie = Cookie("Chocolate Chip", 6, 3.99)
print(f"  Candy can_combine with Cookie: {candy.can_combine(cookie)}")
assert candy.can_combine(cookie) is False
print("  ✓ Different item types correctly cannot combine")

# Test 4: Same type but different prices cannot combine
print("\nTest 4: Same type but different prices cannot combine")
candy1 = Candy("Gummy Bears", 0.5, 0.25)
candy2 = Candy("Gummy Bears", 1.0, 0.35)  # Different price!
print(f"  Candy 1: {candy1.price_per_pound}/lb")
print(f"  Candy 2: {candy2.price_per_pound}/lb")
print(f"  can_combine: {candy1.can_combine(candy2)}")
assert candy1.can_combine(candy2) is False
print("  ✓ Same item with different price correctly cannot combine")

# Test 5: Order automatically combines items
print("\n" + "=" * 70)
print("Test 5: Order automatically combines like items")
print("=" * 70)

order = Order()

print("\nAdding items to order:")
order.add(Candy("Gummy Bears", 0.5, 0.25))
print(f"  Added: Gummy Bears 0.5 lbs @ $0.25/lb - Order size: {len(order.order)}")

order.add(Candy("Candy Corn", 1.5, 0.25))
print(f"  Added: Candy Corn 1.5 lbs @ $0.25/lb - Order size: {len(order.order)}")

order.add(Candy("Gummy Bears", 1.0, 0.25))  # Should combine with first Gummy Bears
print(f"  Added: Gummy Bears 1.0 lbs @ $0.25/lb - Order size: {len(order.order)}")

order.add(Cookie("Chocolate Chip", 6, 3.99))
print(f"  Added: Chocolate Chip 6 cookies @ $3.99/dozen - Order size: {len(order.order)}")

order.add(Cookie("Chocolate Chip", 12, 3.99))  # Should combine with first Chocolate Chip
print(f"  Added: Chocolate Chip 12 cookies @ $3.99/dozen - Order size: {len(order.order)}")

order.add(IceCream("Vanilla", 2, 1.0))
print(f"  Added: Vanilla Ice Cream 2 scoops - Order size: {len(order.order)}")

print(f"\nFinal order size: {len(order.order)} items (expected 4)")
assert len(order.order) == 4

# Verify the combined items
gummy_bears = order.order[0]
print(f"\nGummy Bears weight: {gummy_bears.candy_weight} lbs (expected 1.5)")
assert gummy_bears.candy_weight == 1.5

chocolate_chip = order.order[2]
print(f"Chocolate Chip quantity: {chocolate_chip.cookie_quantity} cookies (expected 18)")
assert chocolate_chip.cookie_quantity == 18

print("\n✓ Order correctly combined like items")

# Test 6: Iterator functionality
print("\n" + "=" * 70)
print("Test 6: Order iterator functionality")
print("=" * 70)

count = 0
for item in order:
    count += 1
    print(f"  Item {count}: {item.name}")

print(f"\nIterated through {count} items (expected 4)")
assert count == 4
print("✓ Iterator works correctly")

# Test 7: Full receipt with combined items
print("\n" + "=" * 70)
print("Test 7: Receipt with combined items")
print("=" * 70)

order.sort()
order.set_pay_type(PayType.CARD)
print(tabulate(order.to_list(), tablefmt="fancy_grid"))

print("\n" + "=" * 70)
print("All combining tests passed!")
print("=" * 70)
