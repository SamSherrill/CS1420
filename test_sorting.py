"""Test script to verify sorting functionality."""

import sys

sys.path.insert(0, "dessert_shop")

from dessert import Candy, Cookie, IceCream, Sundae, Order
from payment import PayType
from tabulate import tabulate

print("=" * 70)
print("Testing Sorting Functionality")
print("=" * 70)

# Test 1: Create order with items in random order
print("\nTest 1: Adding items in non-sorted order")
order = Order()
order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))  # cost = 3.36
print(f"  Added Sundae (cost: ${order.order[-1].calculate_cost():.2f})")

order.add(Candy("Gummy Bears", 0.25, 0.35))  # cost = 0.09
print(f"  Added Candy (cost: ${order.order[-1].calculate_cost():.2f})")

order.add(Cookie("Chocolate Chip", 6, 3.99))  # cost = 2.0
print(f"  Added Cookie (cost: ${order.order[-1].calculate_cost():.2f})")

order.add(Candy("Candy Corn", 1.5, 0.25))  # cost = 0.38
print(f"  Added Candy (cost: ${order.order[-1].calculate_cost():.2f})")

order.add(IceCream("Pistachio", 2, 0.79))  # cost = 1.58
print(f"  Added IceCream (cost: ${order.order[-1].calculate_cost():.2f})")

# Test 2: Verify comparison operators work
print("\n" + "=" * 70)
print("Test 2: Comparison Operators")
print("=" * 70)

item1 = Candy("Item1", 1.0, 1.0)  # cost = 1.0
item2 = Candy("Item2", 1.0, 2.0)  # cost = 2.0
item3 = Candy("Item3", 1.0, 1.0)  # cost = 1.0

print(f"\nItem1 cost: ${item1.calculate_cost():.2f}")
print(f"Item2 cost: ${item2.calculate_cost():.2f}")
print(f"Item3 cost: ${item3.calculate_cost():.2f}")

print(f"\nitem1 == item3: {item1 == item3} (expected: True)")
print(f"item1 != item2: {item1 != item2} (expected: True)")
print(f"item1 < item2: {item1 < item2} (expected: True)")
print(f"item1 <= item2: {item1 <= item2} (expected: True)")
print(f"item1 <= item3: {item1 <= item3} (expected: True)")
print(f"item2 > item1: {item2 > item1} (expected: True)")
print(f"item2 >= item1: {item2 >= item1} (expected: True)")
print(f"item2 >= item2: {item2 >= item2} (expected: True)")

# Test 3: Sort the order
print("\n" + "=" * 70)
print("Test 3: Sorting Order")
print("=" * 70)

print("\nBefore sorting:")
for i, item in enumerate(order.order):
    print(f"  {i+1}. {item.name}: ${item.calculate_cost():.2f}")

order.sort()

print("\nAfter sorting:")
for i, item in enumerate(order.order):
    print(f"  {i+1}. {item.name}: ${item.calculate_cost():.2f}")

# Verify sorted order
costs = [item.calculate_cost() for item in order.order]
assert costs == sorted(costs), "Items are not in ascending order!"
print("\n✓ Items are correctly sorted in ascending order by cost")

# Test 4: Full receipt with sorted items
print("\n" + "=" * 70)
print("Test 4: Full Receipt with Sorted Items")
print("=" * 70)

order.set_pay_type(PayType.CARD)
print(tabulate(order.to_list(), tablefmt="fancy_grid"))

print("\n" + "=" * 70)
print("All sorting tests passed!")
print("=" * 70)
