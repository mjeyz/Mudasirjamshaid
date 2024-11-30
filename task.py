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
profet = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 4. Check resources sufficient?
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! there in not enough {item}.")
            return False
    return True

# TODO 5. Process coins
def process_coin():
    print("Please insert coin.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

# TODO 6. Check transaction successful?
def  transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Hare is ${change} in change.")
        global profet
        profet += drink_cost
        return True
    else:
        print("Sorry! that not enough money. Money refunded.")
        return False

# TODO 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Hare is Your {drink_name} ☕. Enjoy!")


is_true = True
while is_true:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    print("Note! price of espresso is $1.5, latte is $2.5 and cappuccino is $3.0")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == "off":
        is_true = False
        # TODO 3. Print report.
    elif user_choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profet}")
    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
