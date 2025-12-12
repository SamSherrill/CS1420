"""Quick test script to verify __str__ output."""
from dessert_shop.dessert import Candy, Cookie, IceCream, Sundae, Order

# Create items and print their string representations
candy = Candy('Candy Corn', 1.5, 0.25)
print(candy)
print()

cookie = Cookie('Chocolate Chip', 6, 3.99)
print(cookie)
print()

icecream = IceCream('Pistachio', 2, 0.79)
print(icecream)
print()

sundae = Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29)
print(sundae)
print()

# Test full order
order = Order()
order.add(Candy('Candy Corn', 1.5, 0.25))
order.add(Candy('Gummy Bears', 0.25, 0.35))
order.add(Cookie('Chocolate Chip', 6, 3.99))
order.add(IceCream('Pistachio', 2, 0.79))
order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
order.add(Cookie('Oatmeal Raisin', 2, 3.45))

print("Order string representation:")
print(order)
print()

print("Order as list:")
print(order.to_list())
