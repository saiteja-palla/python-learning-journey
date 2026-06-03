"""
Coffee Machine Simulator — Day 15 Project
100 Days of Code: The Complete Python Pro Bootcamp (Angela Yu)

A terminal-based coffee machine that handles drink selection, resource
management, coin processing and change calculation.
"""

from data import MENU, resources

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

money = 0

choices_list = ['espresso', 'latte', 'cappuccino']

def get_user_choice():
    user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    try:
        if user_choice == 'report':
            resources_report(resources)
        elif user_choice == 'off':
            exit(0)
        elif user_choice not in choices_list:
            raise ValueError
        else:
            return user_choice
    except ValueError:
        print("Invalid option. You have to select any of (Espresso/Latte/Cappuccino): ")
        return None
    
def ask_for_coins():
    penny = int(input("How many penny? "))
    dime = int(input("How many dime? "))
    nickel = int(input("How many nickel? "))
    quarter = int(input("How many quarter? "))
    return penny, dime, nickel, quarter

def resources_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def monetory_value(penny, dime, nickel, quarter):
    return sum([penny * PENNY, dime * DIME, 
            nickel * NICKEL, quarter * QUARTER])

def is_coins_enough(amount, user_choice):
    if amount >= MENU[user_choice]['cost']:
        return True
    else:
        return False
    
def process_change(amount, user_choice):
    if amount > MENU[user_choice]['cost']:
        return amount - MENU[user_choice]['cost']
    else:
        return None

def is_resources_sufficient(user_choice, resources):
    required = MENU[user_choice].get("ingredients")
    if required.get('water') > resources.get('water'):
        print("Sorry, there is not enough water.")
        return False
    if required.get('coffee') > resources.get('coffee'):
        print("Sorry, there is not enough coffee.")
        return False
    if required.get('milk') is not None:
        if required.get('milk') > resources.get('milk'):
            print("Sorry, there is not enough milk.")
            return False
    return True

def deduct_resources(drink, resources):   
    for item, amount in MENU[drink]['ingredients'].items():
        resources[item] -= amount
    return resources

if __name__ == "__main__":
    while True:
        drink = get_user_choice()
        if drink == None:
            continue
        else:
            if not is_resources_sufficient(drink, resources):
                print("Sorry there is not enough water.")
            else:
                penny, dime, nickel, quarter = ask_for_coins()
                total_input_amount = monetory_value(penny, dime, nickel, quarter)
                if not is_coins_enough(total_input_amount, drink):
                    if total_input_amount > 0:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        print("Sorry that's not enough money.")
                else:
                    change = process_change(total_input_amount, drink)
                    money += MENU[drink]['cost']
                    if change:
                        print(f"Here is ${round(change, 2)} dollars in change.")
                    resources = deduct_resources(drink, resources)
                    print(f"Here is your {drink}☕. Enjoy!")
                    


