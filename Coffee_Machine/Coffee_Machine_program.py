from Coffee_Machine_data import *
from Coffee_Machine_art import *

print(coffee_machine)
print(write)


def make_coffee(type_coffee):
    recipe = type_coffee["ingredients"]
    make = True

    if recipe["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        make = False
    if recipe["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        make = False
    if recipe["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        make = False

    if make == 1:
        return 1
    else:
        return 0


def process_coin(type_coffee):
    cost = type_coffee["cost"]
    print("Please insert coins.")
    quarter = float(input("How many quarters?: "))*0.25
    dime = float(input("How many dimes?: "))*0.1
    nickle = float(input("How many nickles?: "))*0.05
    penny = float(input("How many pennies?: "))*0.01

    total = quarter + dime + nickle + penny

    if total >= cost:
        print(f"Here is ${round(total-cost,1)} in change.")
        return True
    else:
        return False


off = False
while off != 1:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        off = True

    elif choice == 'espresso':
        coffee = MENU[choice]
        is_make_coffee = make_coffee(coffee)
        if is_make_coffee == 1:
            if process_coin(coffee) == 1:
                print(f"Here is your {choice} ☕️☕️☕︎️. Enjoy!")
                resources["water"] -= coffee["ingredients"]["water"]
                resources["milk"] -= coffee["ingredients"]["milk"]
                resources["coffee"] -= coffee["ingredients"]["coffee"]
                resources["money"] += coffee["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == 'latte':
        coffee = MENU[choice]
        is_make_coffee = make_coffee(coffee)
        if is_make_coffee == 1:
            if process_coin(coffee) == 1:
                print(f"Here is your {choice} ☕️☕️☕︎️. Enjoy!")
                resources["water"] -= coffee["ingredients"]["water"]
                resources["milk"] -= coffee["ingredients"]["milk"]
                resources["coffee"] -= coffee["ingredients"]["coffee"]
                resources["money"] += coffee["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == 'cappuccino':
        coffee = MENU[choice]
        is_make_coffee = make_coffee(coffee)
        if is_make_coffee == 1:
            if process_coin(coffee) == 1:
                print(f"Here is your {choice} ☕️☕️☕︎️. Enjoy!")
                resources["water"] -= coffee["ingredients"]["water"]
                resources["milk"] -= coffee["ingredients"]["milk"]
                resources["coffee"] -= coffee["ingredients"]["coffee"]
                resources["money"] += coffee["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    else:
        print("Undefined. Please input again!")

    print()
