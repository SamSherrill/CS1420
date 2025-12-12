"""Application driver for the Dessert Shop.

Part 5: Terminal-based user interface for building orders.
"""

from __future__ import annotations

from tabulate import tabulate

try:
    from dessert_shop.dessert import Candy, Cookie, IceCream, Sundae, Order
except Exception:  # pragma: no cover - allow running as script from package dir
    from dessert import Candy, Cookie, IceCream, Sundae, Order


class DessertShop:
    """Dessert shop with methods to prompt user for dessert items."""

    def user_prompt_candy(self) -> Candy:
        """Prompt user for candy details, validate, and return a Candy object."""
        name = input("Enter name of candy: ")

        while True:
            try:
                weight = float(input("Enter weight (lbs): "))
                if weight < 0:
                    print("Weight cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                price = float(input("Enter price per pound: "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        return Candy(name, weight, price)

    def user_prompt_cookie(self) -> Cookie:
        """Prompt user for cookie details, validate, and return a Cookie object."""
        name = input("Enter name of cookie: ")

        while True:
            try:
                quantity = int(input("Enter quantity (cookies): "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                price = float(input("Enter price per dozen: "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        return Cookie(name, quantity, price)

    def user_prompt_icecream(self) -> IceCream:
        """Prompt user for ice cream details, validate, and return an IceCream object."""
        name = input("Enter the type of ice cream: ")

        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    print("Number of scoops cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                price = float(input("Enter the price per scoop: "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        return IceCream(name, scoops, price)

    def user_prompt_sundae(self) -> Sundae:
        """Prompt user for sundae details, validate, and return a Sundae object."""
        name = input("Enter the type of ice cream: ")

        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    print("Number of scoops cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                price = float(input("Enter the price per scoop: "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        topping_name = input("Enter the topping: ")

        while True:
            try:
                topping_price = float(input("Enter the price for the topping: "))
                if topping_price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        return Sundae(name, scoops, price, topping_name, topping_price)


def print_receipt(order: Order) -> None:
    """Print the order receipt in tabular format."""
    rows = []
    display_tax_total = 0.0
    for item in order.order:
        cost = item.calculate_cost()
        # display uses banker's rounding to match sample receipt
        display_tax = round(cost * (item.tax_percent / 100.0), 2)
        display_tax_total += display_tax
        rows.append([item.name, f"{cost:.2f}", f"{display_tax:.2f}"])

    subtotal = order.order_cost()
    total = round(subtotal + display_tax_total, 2)

    # Add summary rows
    rows.append(["Subtotal", f"{subtotal:.2f}", f"{display_tax_total:.2f}"])
    rows.append(["Total", f"{total:.2f}", ""])
    rows.append(["Total number of items in order:", f"{len(order)}", ""])

    print(tabulate(rows, headers=["Dessert", "Cost", "Tax"], tablefmt="plain"))


def main() -> None:
    """Main function with UI loop for building orders."""
    shop = DessertShop()
    order = Order()

    # Main UI loop
    while True:
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")

        choice = input(
            "\nWhat would you like to add to the order? (1-4, Enter for done): "
        )

        if choice == "":
            break
        elif choice == "1":
            item = shop.user_prompt_candy()
            order.add(item)
            print()
        elif choice == "2":
            item = shop.user_prompt_cookie()
            order.add(item)
            print()
        elif choice == "3":
            item = shop.user_prompt_icecream()
            order.add(item)
            print()
        elif choice == "4":
            item = shop.user_prompt_sundae()
            order.add(item)
            print()
        else:
            print("Invalid choice. Please enter 1-4 or press Enter to finish.")

    # Print receipt at the end
    print()
    print_receipt(order)


if __name__ == "__main__":
    main()
