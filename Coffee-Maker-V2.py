from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

diamondCoffee = CoffeeMaker()
diamondRegister = MoneyMachine()
diamondMenu = Menu()

while True:
    options = diamondMenu.get_items()
    choice = input(f"What would you like? {options}: ").lower()

    if choice == 'off':
        print("GoodBye!")
        break
    elif choice == 'report':
        diamondCoffee.report()
        diamondRegister.report()
    else:
        drink = diamondMenu.find_drink(choice)
        drinkCost = drink.cost
        if diamondCoffee.is_resource_sufficient(drink) and diamondRegister.make_payment(drinkCost):
            diamondCoffee.make_coffee(drink)

