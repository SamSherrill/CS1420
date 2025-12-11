"""Application driver for the Dessert Shop (Part 2).

Creates an Order, adds sample items, prints each item's name and the total
number of items in the order. Output must match the assignment sample.
"""

from __future__ import annotations

from dessert import Candy, Cookie, IceCream, Sundae, Order


def main() -> None:
    order = Order()

    # Add required items to the order in the specified order
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Gummy Bears", 0.25, 0.35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, 0.79))
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    # Print each item's name
    for item in order.order:
        print(item.name)

    # Print total number of items
    print(f"Total number of items in order: {len(order)}")


if __name__ == "__main__":
    main()
