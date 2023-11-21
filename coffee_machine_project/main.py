from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
coffee_machine = CoffeeMaker()
coffee_menu = Menu()
coffee_money_machine = MoneyMachine()


while is_machine_on:
    menu_options = coffee_menu.get_items()
    user_choice = input(f"What would you like? ({menu_options}): ")
    if user_choice == "off":
        is_machine_on = False
        print("Turning off the coffee machine !!!!")
    elif user_choice == "report":
        coffee_machine.report()
        coffee_money_machine.report()
    else:
        drink_details = coffee_menu.find_drink(order_name=user_choice)
        if drink_details is not None:
            if coffee_machine.is_resource_sufficient(drink= drink_details) and coffee_money_machine.make_payment(cost= drink_details.cost):
                coffee_machine.make_coffee(order= drink_details)
