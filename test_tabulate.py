from tabulate import tabulate
from dessert_shop.dessert import Candy, Cookie, IceCream, Sundae, Order

order = Order()
order.add(Candy('Candy Corn', 1.5, 0.25))
order.add(Candy('Gummy Bears', 0.25, 0.35))
order.add(Cookie('Chocolate Chip', 6, 3.99))
order.add(IceCream('Pistachio', 2, 0.79))
order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
order.add(Cookie('Oatmeal Raisin', 2, 3.45))

print("With fancy_grid:")
print(tabulate(order.to_list(), tablefmt="fancy_grid"))
