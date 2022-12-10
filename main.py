from data import menu, resources


profit = 0
resources = {
    "water": 1300,
    "milk": 1300,
    "coffee": 500,
}


def resource_sufficient(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry, there's not enough {i}")
            refresh = input(f"You wish to replenish resources? ")
            if refresh == "yes":
                resources[i] += 500
                print(f"{i.capitalize()} refilled")
            else:
                exit()
        else:
            return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    coins = quarters + dimes + nickles + pennies
    return coins


def successful_transaction(money_received, cost_coffee):
    if money_received > cost_coffee:
        change_coffee = round(money_received - cost_coffee, 2)
        print(f"You've entered ${money_received}.")
        print(f"${cost_coffee} is the cost of {user_coffee}")
        print(f"Here is ${change_coffee} in the change.")
        global profit
        profit += cost_coffee
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_coffee, ingredients):
    # deduct the required ingredients from the resources
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"And here is your {user_coffee}. Enjoy!")

is_on = True
while is_on:
    user_coffee = input("What would you like? ").lower()
    if user_coffee == "espresso" or user_coffee == "latte" or user_coffee == "cappuccino":
        drink = menu[user_coffee]
        # payment = money_received
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(user_coffee, drink["ingredients"])
    elif user_coffee == "off":
        is_on = False
    elif user_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")


