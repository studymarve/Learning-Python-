"""
Poti Pizza Delivery Program 🍕🚚

This script simulates a simple pizza ordering system.
- The user can choose pizza size (Small, Medium, Large).
- Extra toppings and options include: Pepperoni, Extra Cheese, and Drinks.
- Each order is stored in a dictionary with full details.
- Multiple pizzas can be ordered in one session.
- At the end, a detailed receipt is printed showing all pizzas and the final total.

Author: Your Name
Date: 2025-09-29
"""

print("Thanks for choosing Poti Pizza 🍕 🍕 Delivery 🚚🚚")

# ---------------- Functions ---------------- #

def get_pizza_size():
    """
    Ask the user for a pizza size and return the standardized size code (S, M, L)
    along with the base price.
    """
    valid_sizes = {
        "l": "L", "large": "L",
        "m": "M", "medium": "M",
        "s": "S", "small": "S",
    }

    standard_pizza_prices = {"L": 25, "M": 20, "S": 15}

    while True:
        # prompt until valid size is entered
        choice = input(
            "Which pizza size do you want? We have Large(L), Medium(M) and Small(S): "
        ).lower().strip()

        if choice in valid_sizes:
            pizza_size = valid_sizes[choice]         # normalize input
            pizza_price = standard_pizza_prices[pizza_size]
            return pizza_size, pizza_price
        else:
            print("Please type a valid option.")


def pepperoni(choice):
    """
    Ask if user wants pepperoni. 
    Cost: $2 for Small, $3 for Medium/Large. Returns the extra price.
    """
    while True:
        additional = input("Do you need pepperoni (y/n): ").lower().strip()
        if additional == "y":
            if choice == "S":
                return 2
            elif choice in ("M", "L"):
                return 3
        elif additional == "n":
            return 0
        else:
            print("Please type a valid input.")


def cheese():
    """
    Ask if user wants extra cheese.
    Cost: $1 flat for any pizza size. Returns the extra price.
    """
    while True:
        extra = input("Do you want extra cheese (y/n): ").lower().strip()
        if extra == "y":
            return 1
        elif extra == "n":
            return 0
        else:
            print("Please type a valid input.")


def drinks():
    """
    Ask if user wants a drink.
    Options: Small = $2, Large = $3, None = $0. Returns the extra price.
    """
    valid_drinks = {
        "s": 2, "small": 2,
        "l": 3, "large": 3,
        "n": 0, "none": 0
    }

    while True:
        choice = input("Do you want a drink? Small(S) = $2, Large(L) = $3, None(N): ").lower().strip()
        if choice in valid_drinks:
            return valid_drinks[choice]
        else:
            print("Please type a valid option.")


# ---------------- Main Program ---------------- #

if __name__ == "__main__":
    all_orders = []   # list to hold every pizza order as a dictionary
    total_bill = 0    # running total
    pizza_number = 1  # order counter

    while True:
        # get base pizza
        choice, pizza_price = get_pizza_size()
        print(f"Base price: ${pizza_price}")

        # ask for add-ons
        pepperoni_price = pepperoni(choice)
        cheese_price = cheese()
        drink_price = drinks()

        # calculate subtotal for this pizza
        pizza_total = pizza_price + pepperoni_price + cheese_price + drink_price
        total_bill += pizza_total

        # store order details in a dictionary
        order = {
            "Pizza #": pizza_number,
            "Size": choice,
            "Base": pizza_price,
            "Pepperoni": pepperoni_price,
            "Cheese": cheese_price,
            "Drink": drink_price,
            "Total": pizza_total
        }
        all_orders.append(order)

        print(f"Subtotal for this pizza: ${pizza_total}")
        pizza_number += 1

        # check if user wants to continue ordering
        more = input("Do you want to order another pizza? (y/n): ").lower().strip()
        if more != "y":
            break

    # ----------- Receipt ----------- #
    print("\n----- 🧾 Receipt -----")
    for order in all_orders:
        print(
            f"Pizza {order['Pizza #']} ({order['Size']}): "
            f"Base=${order['Base']}, Pepperoni=${order['Pepperoni']}, "
            f"Cheese=${order['Cheese']}, Drink=${order['Drink']} → "
            f"Subtotal=${order['Total']}"
        )
    print("----------------------")
    print(f"🍕 Final Total Bill = ${total_bill}")