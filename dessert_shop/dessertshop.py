"""Application driver for the Dessert Shop.

Part 7: Adding Packaging Protocol (mixin interface) to dessert items.
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


def main():
    shop = DessertShop()
    order = Order()

    # order.add(Candy('Candy Corn', 1.5, 0.25))
    # order.add(Candy('Gummy Bears', 0.25, 0.35))
    # order.add(Cookie('Chocolate Chip', 6, 3.99))
    # order.add(IceCream('Pistachio', 2, 0.79))
    # order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    # order.add(Cookie('Oatmeal Raisin', 2, 3.45))

    done: bool = False
    # build the prompt string once
    prompt = "\n".join(
        [
            "\n",
            "1: Candy",
            "2: Cookie",
            "3: Ice Cream",
            "4: Sundae",
            "\nWhat would you like to add to the order? (1-4, Enter for done): ",
        ]
    )

    while not done:
        choice = input(prompt)
        match choice:
            case "":
                done = True
            case "1":
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "2":
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "3":
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "4":
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case _:
                print(
                    "Invalid response:  Please enter a choice from the menu (1-4) or Enter"
                )
    print()

    # Print receipt using tabulate with order.to_list()
    print(tabulate(order.to_list(), tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
