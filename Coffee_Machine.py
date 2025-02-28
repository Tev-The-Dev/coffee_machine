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
    "money": 0.0
}

#TODO: Create a function that takes in 4 inputs for coins, does the math, and converts it to dollar syntax
def take_money(c):
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))
    quarters *= .25
    dimes *= .10
    nickels *= .05
    pennies *= .01

    amount = quarters + dimes + nickels + pennies
    amount = round(amount, 2)
    paid = True
    if check_customer_money(amount, c):
        resources["money"] += MENU[c]["cost"]
        return amount
    else:
        return

#TODO: access resources and subtract the amounts of the chosen drink from resources
def set_resources(coffee):
    if check_resources():
        print(f"Your {coffee} is ${MENU[coffee_choice]["cost"]:.2f}")
        if take_money(coffee):
            if coffee == "espresso":
                resources["water"] -= MENU[coffee]["ingredients"]["water"]
                resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            else:
                resources["water"] -= MENU[coffee]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


#TODO: Create a function that takes in the money the customer puts in and subtracts it from the cost of the coffee. Check if the customer put in the correct or more than required amount of money
def check_customer_money(a, c):
    if a >= MENU[c]["cost"]:
        if a == MENU[c]["cost"]:
            print("Enjoy your coffee!")
        else:
            a = (MENU[c]["cost"] - a)*-1
            print(f"Your change is ${a:.2f}")
            print("Enjoy your coffee")
        return a
    else:
        print(f"You do not have enough money. Returning ${a:.2f}")
        return False

#TODO: Create a function that checks the resources and makes sure a drink can be ordered. If not, do not accept any money AKA end the program
def check_resources():
    if resources["water"] < 250 or resources["milk"] < 150 or resources["coffee"] < 24:
        print("Sorry, this machine does not have enough resources to make that coffee. Pick something else")
        return False
    else:
        return True
def report():
    for i in resources:
        if i == "water" or i == "milk":
            print(f"{i.capitalize()}: {resources[i]}ml")
        if i == "coffee":
            print(f"{i.capitalize()}: {resources[i]}g")
        if i == "money":
            print(f"{i.capitalize()}: ${resources[i]:.2f}")
def refill_resources():
    continue_refilling = True
    while continue_refilling:
        try:
            resource = str(input("Which resource would you like to refill?\n"))
            if resource not in resources:
                raise ValueError(f"Invalid resource")
            print(f"You chose to refill {resource}")
            amount_to_refill = int(input(f"How much {resource} are you putting in?").lower())
            resources[resource] += amount_to_refill
        except ValueError as e:
            print(e)
        finished_refilling = str(input("Are you finished refilling resources? yes/no "))
        if finished_refilling == "yes":
            continue_refilling = False

order_coffee = True
while order_coffee:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino) or quit to end: ").lower()
    if coffee_choice == "off":
        maintain = True
        print("Putting the machine in maintenance mode:")
        while maintain:
            #TODO: put this in a loop to allow the continuation until done
            maintenance_mode = str(input(" Choose Option: report | refill | exit \n"))
            if maintenance_mode == "report":
                report()
            elif maintenance_mode == "refill":
                refill_resources()
            else:
                print("Turning machine on for use")
                maintain = False
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        set_resources(coffee_choice)
    elif coffee_choice == "quit":
        order_coffee = False
    else:
        print("That is not one of your options. Try again!")
    print('\n'*5)



