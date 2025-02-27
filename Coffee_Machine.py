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
    quarters *= .25
    dimes *= .10
    nickels *= .05
    pennies *= .01

    amount = quarters + dimes + nickels + pennies/ 100
    amount = round(amount, 2)
    check_customer_money(amount)
    return amount

#TODO: access resources and subtract the amounts of the chosen drink from resources
def set_resources(coffee):
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    return resources

#TODO: Create a function that takes in the money the customer puts in and subtracts it from the cost of the coffee. Check if the customer put in the correct or more than required amount of money
def check_customer_money(a):
    if a >= MENU[coffee_choice]["cost"]:
        if a == MENU[coffee_choice]["cost"]:
            print("Enjoy your coffee!")
        else:
            print(f"Your change is ${(MENU[coffee_choice]["cost"] - a)*-1:.2}")
            print("Enjoy your coffee")
    else:
        print(f"You do not have enough money. Returning ${a:.2}")


coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
print(f"Your {coffee_choice} is ${MENU[coffee_choice]["cost"]:.2f}")
take_money()


