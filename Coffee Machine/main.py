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
    "money": 0,
}

required_water = 0
required_milk = 0
required_coffee = 0

# TODO: 5. A function to check if present resources are sufficient to get the drink. If no enough resources, "Sorry not enough water/ milk/ coffee."
def get_resources():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${resources['money']}")


def are_enough_resources(drink):
    global required_water, required_coffee, required_milk
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient in drink_ingredients:
        if ingredient == "water":
            required_water = drink_ingredients[ingredient]
        elif ingredient == "coffee":
            required_coffee = drink_ingredients[ingredient]
        else:
            required_milk = drink_ingredients[ingredient]
    available_water = resources["water"]
    available_milk = resources["milk"]
    available_coffee = resources["coffee"]
    if required_water > available_water:
        print("Sorry, there is not enough water in the machine.")
        return False
    elif required_milk > available_milk:
        print("Sorry, there is not enough milk in the machine.")
        return False
    elif required_coffee > available_coffee:
        print("Sorry, there is not enough coffee in the machine.")
        return False
    else:
        return True


# TODO: 6. If enough resources are available, then only prompt user to insert coins.
def user_provides_money():
    print("Please insert coins.")
    quarters_inserted = int(input("how many quarters ?: "))
    dimes_inserted = int(input("how many dimes ?: "))
    nickles_inserted = int(input("how many nickles ?: "))
    pennies_inserted = int(input("how many pennies ?: "))
    return quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted


# TODO: 7. Calculate the value of inserted coins
def calculate_value_of_coins():
    quarters, dimes, nickles, pennies = user_provides_money()
    total_input_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_input_money

# TODO: 9. If money is enough, cost of drink is added to the money in resources dictionary and this should reflect in report
# TODO: 10. If money is more than required, calculate change to be given (Change to be rounded to 2 decimal places). "Here is $2.45 dollars in change."
def money_and_change_adjustment(user_money, drink_cost):
    change = 0.0
    resources["money"] += drink_cost
    if user_money > drink_cost:
        change = round(user_money - drink_cost, 2)
    print(f"Here is ${change} dollars in change.")

# TODO: 8. Check if inserted money is enough for drink or not. If money is not enough, print "Sorry that's not enough money. Money refunded."
def is_money_enough(drink):
    input_money = calculate_value_of_coins()
    drink_cost = MENU[drink]["cost"]
    if input_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money_and_change_adjustment(user_money = input_money,drink_cost = drink_cost)
        return True

# TODO: 11. After money is enough, resources are enough, then deduct resources needed for drink and update remaining resources.
def deduct_resources():
    resources["water"] -= required_water
    resources["milk"] -= required_milk
    resources["coffee"] -= required_coffee

#TODO: Last - Reset the used global variables again if any towards the end of the while loop
def reset_required_drink_values():
    global required_water, required_coffee, required_milk
    required_water = 0
    required_milk = 0
    required_coffee = 0


# TODO: 1. Create a user input prompt to get user response to decide what is to be done. TODO: 2. This prompt should
#  be there even after an action is done or even after resources are gone - continuous while loop
coffee_machine_on = True
while coffee_machine_on:
    user_prompt = input("   What would you like? (espresso/latte/cappuccino): ")
    # TODO: 3. Coffe machine should only be turned off using 'off' keyword. while loop should stop only after 'off'
    #  is entered.
    if user_prompt == "off":
        coffee_machine_on = False
    # TODO: 4. When 'report' is entered , we should get current resource values from resources dictionary
    elif user_prompt == "report":
        get_resources()
    elif user_prompt == "espresso" or user_prompt == "latte" or user_prompt == "cappuccino":
        resources_available = are_enough_resources(user_prompt)
        if resources_available:
            if is_money_enough(user_prompt):
                deduct_resources()
                # TODO: 12. At last, print message for user - "Here is your {drink}. Enjoy!"
                print(f"Here is your {user_prompt}. Enjoy! ☕")
    else:
        print("Sorry, we don't have this in our menu !!!")
    reset_required_drink_values()
