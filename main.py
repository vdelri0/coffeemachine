from data import MENU, resources

"""
Program Requirements

1. Print report.
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make Coffee.
"""
on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

while on:
    espresso = MENU['espresso'].get('cost')
    latte = MENU['latte'].get('cost')
    cappuccino = MENU['cappuccino'].get('cost')

    choice = input(f"​What would you like? (espresso ${espresso}/latte ${latte}/cappuccino ${cappuccino}): ").lower()

    if choice == 'off':
        on = False
        print("I'm gonna turn off, bye bye!")
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in ('espresso', 'latte', 'cappuccino'):
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("Please select a valid option.")