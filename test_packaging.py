"""Test script to verify packaging appears correctly in receipt output."""

import sys
sys.path.insert(0, 'dessert_shop')

from dessert_shop.dessert import Candy, Cookie, IceCream, Sundae, Order
from tabulate import tabulate

# Create an order with various items
order = Order()
order.add(Candy("Candy Corn", 1.5, 0.25))
order.add(Candy("Gummy Bears", 0.25, 0.35))
order.add(Cookie("Chocolate Chip", 6, 3.99))
order.add(IceCream("Pistachio", 2, 0.79))
order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
order.add(Cookie("Oatmeal Raisin", 2, 3.45))

# Print using tabulate
print(tabulate(order.to_list(), tablefmt="fancy_grid"))

print("\n" + "="*60)
print("Verifying packaging attributes:")
print("="*60)

# Test individual items
candy = Candy("Test Candy", 1.0, 1.0)
print(f"Candy packaging: {candy.packaging} (expected: Bag)")

cookie = Cookie("Test Cookie", 12, 4.0)
print(f"Cookie packaging: {cookie.packaging} (expected: Box)")

icecream = IceCream("Test Ice Cream", 2, 1.0)
print(f"IceCream packaging: {icecream.packaging} (expected: Bowl)")

sundae = Sundae("Test", 3, 1.0, "Topping", 0.5)
print(f"Sundae packaging: {sundae.packaging} (expected: Boat)")

print("\n" + "="*60)
print("Verifying __str__ includes packaging:")
print("="*60)
print("\nCandy:")
print(str(candy))
print("\nCookie:")
print(str(cookie))
print("\nIce Cream:")
print(str(icecream))
print("\nSundae:")
print(str(sundae))
