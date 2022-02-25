from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

okay = CoffeeMaker()
money = MoneyMachine()
drink = Menu()
start = True
while start:

    print(f"This is our menu: {drink.get_items()}")
    what = input('Which Drink Do You Want? ').lower()
    if what == 'off':
        # print("why")
        start = False
    elif what == 'report':
        okay.report()
        money.report()
        # start = False
    else:
        # start = False
        choice = drink.find_drink(what)
        if choice and okay.is_resource_sufficient(choice):
            if money.make_payment(choice.cost):
                # print('yayy')
                okay.make_coffee(choice)
