MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order: str) -> bool:    
    is_sufficient = True
    for ingredient in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            is_sufficient = False
    return is_sufficient

    
def process_coins() -> float:
    print("Please insert coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = quaters * 0.25 + dimes *  0.10 + nickles * 0.05 + pennies * 0.01
    return amount


def is_transaction_successful(order: str, money: float) -> bool:
    cost = MENU[order]["cost"]
    change = money - cost
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    elif change > 0:
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True
    else:
        return True


def make_drink(order):
    global resources
    global revenue

    # update resources of ingredients
    for ingredient in MENU[order]["ingredients"]:
        usage_amount = MENU[order]["ingredients"][ingredient]
        remaining_amount = resources[ingredient] - usage_amount
        resources[ingredient] = remaining_amount

    # update revenue
    revenue += MENU[order]["cost"]

    print(f"Here is your {order}. Enjoy!")


revenue = 0
deposit = 0

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        print("Under maintanance")
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${revenue}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if is_resource_sufficient(order):
            deposit = process_coins()
            if is_transaction_successful(order, deposit):
                make_drink(order)
    else:
        continue