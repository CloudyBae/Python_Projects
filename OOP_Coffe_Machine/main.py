from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menuitem = MenuItem()    

is_on = True
while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    else:
        drink_info = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink_info) and money_machine.make_payment(drink_info.cost):
            coffee_maker.make_coffee(drink_info)
            
    