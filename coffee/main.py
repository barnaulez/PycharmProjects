import menu

def choose():
    print("What would you like?")
    print("1. Americano\n2. Espresso\n3. Double Americano\n4. Latte\n5. Capuccino")
    finish = False
    while not finish:
        res = input("Select number of desired drink: ")
        if res in ["1", "2", "3", "4", "5"]:
            finish = True
            return int(res)
        elif res.lower() in ["report", "off"]:
            finish = True
            if res == "report":
                return 100
            else:
                return 99
        else:
            finish = False

def prepare(drink):

    if drink[0]['coffee'] > menu.container['coffee']:
        print("There is no enough coffee...")
        return False
    elif drink[0]['milk'] > menu.container['milk']:
        print("There is no enough milk...")
        return False
    elif drink[0]['water'] > menu.container['water']:
        print("There is no enough water...")
        return False
    else:
        return True

def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * menu.coins['quarter'] + dimes * menu.coins['dime'] + nickles * menu.coins['nickel'] + pennies * menu.coins['penny']

def drink_contains(drink):
    return list(filter(lambda item: item['id'] == drink, menu.menu))

def report():
    for key in menu.container:
        print(f"{key.title()} - {'$' if key == 'money' else ''}{round(menu.container[key], 2)}{' ml' if key == 'water' or key == 'milk' else ' g' if key == 'coffee' else ''}")

def decrease_continer(drink):
    menu.container['water'] -= drink[0]['water']
    menu.container['milk'] -= drink[0]['milk']
    menu.container['coffee'] -= drink[0]['coffee']
    menu.container['money'] += drink[0]['price']

one_more = True
while one_more:
    coffee_to_go = []
    selected_drink_id = choose()
    if selected_drink_id == 100:
        report()
    elif selected_drink_id == 99:
        print("Coffee automat is switching off.")
        one_more = False
    else:
        coffee_to_go = drink_contains(selected_drink_id)
        if prepare(coffee_to_go):
            collected_money = coins()
            print(f"Here is ${round(collected_money, 2)}")
            if coffee_to_go[0]['price'] > collected_money:
                print(f"There is no enough money for {coffee_to_go[0]['name']}")
            elif coffee_to_go[0]['price'] < collected_money:
                print(f"Here is ${round(collected_money - coffee_to_go[0]['price'], 2)} in charge")
                print(f"Enjoy your {coffee_to_go[0]['name'].title()}!")
                decrease_continer(coffee_to_go)
            else:
                print("Enough money")