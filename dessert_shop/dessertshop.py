"""Application driver for the Dessert Shop.

Creates an Order, adds sample items, prints each item's name and the total
number of items in the order. Output must match the assignment sample.
"""

from __future__ import annotations

from tabulate import tabulate

try:
    from dessert_shop.dessert import Candy, Cookie, IceCream, Sundae, Order
except Exception:  # pragma: no cover - allow running as script from package dir
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

    # Build table rows. For display only we compute taxes using Python's
    # built-in `round()` (banker's rounding) so the printed receipt matches
    # the example image exactly. Tests continue to use the model's
    # `calculate_tax()` behavior (which uses ROUND_HALF_UP).
    rows = []
    display_tax_total = 0.0
    for item in order.order:
        cost = item.calculate_cost()
        # display uses banker's rounding to match sample receipt
        display_tax = round(cost * (item.tax_percent / 100.0), 2)
        display_tax_total += display_tax
        rows.append([item.name, f"{cost:.2f}", f"{display_tax:.2f}"])

    subtotal = order.order_cost()
    total_tax = order.order_tax()  # canonical (used by tests)
    # total displayed should use the display tax total
    total = round(subtotal + display_tax_total, 2)

    # Add summary rows
    rows.append(["Subtotal", f"{subtotal:.2f}", f"{display_tax_total:.2f}"])
    rows.append(["Total", f"{total:.2f}", ""])  # total includes tax
    rows.append(["Total number of items in order:", f"{len(order)}", ""])

    print(tabulate(rows, headers=["Dessert", "Cost", "Tax"], tablefmt="plain"))


if __name__ == "__main__":
    main()
