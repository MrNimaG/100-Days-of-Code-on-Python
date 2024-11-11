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

input_choices = ["report", "off", "espresso", "latte", "cappuccino"]
condition = True
profit = 0

# TODO: Verify user input

def input_verification(var):
    if var not in input_choices:
        global condition
        condition = False
        print("wrong input! Please try again")
        return condition

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)":

def user_decision():
    global user_input
    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()
    return user_input


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

def off(var):
    if var == 'off':
        global condition
        condition = False
        return condition


# TODO: 3. Print report

def report(var):
    global profit
    if var == 'report':
        print(f'Water = {resources["water"]}')
        print(f'Milk = {resources["milk"]}')
        print(f'Coffee = {resources["coffee"]}')
        print(f'Money = ${profit}')


# TODO: 4. Check resources sufficient?

def resource(var):
    global condition
    if var == 'latte' or var == 'cappuccino':
        if resources["water"] < MENU[var]["ingredients"]["water"]:
            condition = False
            print("Sorry, There is not enough water")
            return condition
        elif resources["coffee"] < MENU[var]["ingredients"]["coffee"]:
            condition = False
            print("Sorry, There is not enough coffee")
            return condition
        elif resources["milk"] < MENU[var]["ingredients"]["milk"]:
            condition = False
            print("Sorry, There is not enough milk")
            return condition
    elif var == 'espresso':
        if resources["water"] < MENU[var]["ingredients"]["water"]:
            condition = False
            print("Sorry, There is not enough water")
            return condition
        elif resources["coffee"] < MENU[var]["ingredients"]["coffee"]:
            condition = False
            print("Sorry, There is not enough coffee")
            return condition





# TODO: 5. Process coins.

def coin():
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.1
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    total_inserted_coins = pennies + nickles + dimes + quarters
    return total_inserted_coins


# TODO: 6. Check transaction successful?

def money(var, coins):
    global condition
    global profit
    if coins < MENU[var]["cost"]:
        condition = False
        print("Sorry, That's not enough money. Money refunded.")
        return condition
    elif coins == MENU[var]["cost"]:
        profit += coins
    elif coins > MENU[var]["cost"]:
        profit += MENU[var]["cost"]
        change = round((coins - MENU[var]["cost"]), 2)
        print(f"Here is ${change} dollars for change.")




# TODO: 7. Make Coffee.

def make(var):
    global resources
    if var != 'espresso':
        resources["water"] -= MENU[var]["ingredients"]["water"]
        resources["coffee"] -= MENU[var]["ingredients"]["coffee"]
        resources["milk"] -= MENU[var]["ingredients"]["milk"]
        print(f"Here is your {var}")
    else:
        resources["water"] -= MENU[var]["ingredients"]["water"]
        resources["coffee"] -= MENU[var]["ingredients"]["coffee"]
        print(f"Here is your {var}")




while condition:
    user_input = ""
    user_decision()
    input_verification(user_input)
    if not condition:
        continue
    off(user_input)
    if not condition:
        break
    if user_input == 'report':
        report(user_input)
        continue
    resource(user_input)
    if not condition:
        break
    inserted_coins = coin()
    money(user_input, inserted_coins)
    make(user_input)


