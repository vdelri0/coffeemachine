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

def check_resources(option):
    def check(option):
        """Validate the given option returns Boolean." """
        global profit
        data = MENU[option]
        ingredients = data['ingredients'].values()

        water = 0
        milk = 0
        coffee = 0

        if option == 'espresso':
            water, coffee = ingredients
        elif option == 'latte' or option == 'cappuccino':
            water, milk, coffee = ingredients

        if resources['water'] - water >= 0:
            resources['water'] -= water
        else:
            print(f"Sorry there is not enough water.")
            return False

        if milk:
            if(resources['milk'] - milk >= 0):
                resources['milk'] -= milk
            else:
                print(f"Sorry there is not enough milk.")
                return False
        if resources['coffee'] - coffee >= 0:
            resources['coffee'] -= coffee
        else:
            print(f"Sorry there is not enough coffee.")
            return False

        return True

    def purchase(option):
        """If there's enough money It will purchase"""
        global profit
        data = MENU[option]
        cost = data.get('cost')

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        quarters *= 0.25
        dimes *= 0.10
        nickles *= 0.05
        pennies *= 0.01

        coins = quarters + dimes + nickles + pennies
        coins -= cost
        coins = round(coins, 2)

        if coins >= 0:
            profit += cost
            print(f"Here is ${coins} in change.")
            print(f"Here is your {option} Enjoy!.")
        else:
            print(f"Sorry that's not enough money. Money refunded.")

    check = check(option)
    if check:
        return purchase(option)

while on:
    espresso = MENU['espresso'].get('cost')
    latte = MENU['latte'].get('cost')
    cappuccino = MENU['cappuccino'].get('cost')

    option = input(f"​What would you like? (espresso ${espresso}/latte ${latte}/cappuccino ${cappuccino}): ").lower()

    if option == 'off':
        on = False
        print("I'm gonna turn off, bye bye!")
    elif option == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif option in ('espresso', 'latte', 'cappuccino'):
        check_resources(option)
    else:
        print("Please select a valid option.")