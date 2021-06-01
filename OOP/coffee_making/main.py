from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
on = True

while on:
    options = menu.get_items()
    user=input(f"what would you like  {options}")
    if user == "off":
        on =False
    elif user =="report":
        coffee.report()
        my_money.report()
    else:
        drink=menu.find_drink(user)
        if coffee.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            coffee.make_coffee(drink)





