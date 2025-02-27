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

#TODO: Create a function that takes in 4 inputs for coins, does the math, and converts it to dollar syntax
def take_money():
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))
    quarters *= 25
    dimes *= 10
    nickels *= 5

    amount = quarters + dimes + nickels + pennies
    if amount >= 100:
        amount /= 100
    return amount


coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
print(MENU[coffee_choice])
print(take_money())

