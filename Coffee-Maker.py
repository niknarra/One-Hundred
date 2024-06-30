# Day 15 - Jun 30 '24
# Coffee Maker Program

logo=r'''
 ______     _                                            __  _           
|_   _ `.  (_)                                          |  ]| |          
  | | `. \ __   ,--.   _ .--..--.   .--.   _ .--.   .--.| | \_|  .--.    
  | |  | |[  | `'_\ : [ `.-. .-. |/ .'`\ \[ `.-. |/ /'`\' |     ( (`\]   
 _| |_.' / | | // | |, | | | | | || \__. | | | | || \__/  |      `'.'.   
|______.' [___]\'-;__/[___||__||__]'.__.' [___||__]'.__.;__]    [\__) )  
                          ______             ___    ___                  
                        .' ___  |          .' ..] .' ..]                 
                       / .'   \_|  .--.   _| |_  _| |_  .---.  .---.     
                       | |       / .'`\ \'-| |-''-| |-'/ /__\\/ /__\\    
                       \ `.___.'\| \__. |  | |    | |  | \__.,| \__.,    
                        `.____ .' '.__.'  [___]  [___]  '.__.' '.__.'    
'''

menu = {
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

registerCash = 0

def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${registerCash}")
    
def check_resources(order):
    for ingredient, amount in menu[order]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry! Not Enough {ingredient}.")
            return False
    return True

def process_coins(order):
    global registerCash
    print("Please insert Coins.")
    quarters = int(input("How many Quarters? "))
    dimes = int(input("How many Dimes? "))
    nickels = int(input("How many Nickels? "))
    pennies = int(input("How many Pennies? "))
    
    total = round((quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01),2)
    
    if total >= menu[order]["cost"]:
        change = round(total - menu[order]["cost"],2)
        if change > 0:
            print(f"Here's your change: ${change}")
    else:
        print(f"{order} costs ${menu[order]["cost"]} Sorry, that's not enough money. Money refunded.")
        return False
    
    registerCash += menu[order]["cost"]
    return True
        
def prepare_order(order):
    for ingredient, amount in menu[order]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {order}. Enjoy! ☕")

print(logo)

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == 'off':
        print("GoodBye!")
        break
        
    elif choice == 'report':
        generate_report()
        
    else:
        if check_resources(choice):
            if process_coins(choice):
                print("Your order is being prepared!")
                prepare_order(choice)
        else:
            break