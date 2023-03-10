MENU = {
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
    "money": 0,
}



def resource():
    """resource list with amount left & money made"""
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    money_amount = resources["money"]
    print(f"Water: {water_amount}ml")
    print(f"Milk: {milk_amount}ml")
    print(f"Coffee: {coffee_amount}g")
    print(f"Money: ${money_amount}")

def coin_value():
    """sum of all the coins the user input"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarter_value = 0.25 * quarters
    dimes_value = 0.10 * dimes
    nickles_value = 0.05 * nickles
    pennies_value = 0.01 * pennies
    return quarter_value + dimes_value + nickles_value + pennies_value

def espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            espresso_coins = coin_value()
            espresso_price = MENU["espresso"]["cost"]
            if espresso_coins >= espresso_price:
                change = round(espresso_coins - espresso_price, 2)
                resources["money"] += espresso_price
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is ${change} in change.")
                print("Here is your espresso. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")
    

def latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                latte_coins = coin_value()
                latte_price = MENU["latte"]["cost"]
                if latte_coins >= latte_price:
                    change = round(latte_coins - latte_price, 2)
                    resources["money"] += latte_price
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    print(f"Here is ${change} in change.")
                    print("Here is your latte. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")
    
        
def cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                cappuccino_coins = coin_value()
                cappuccino_price = MENU["cappuccino"]["cost"]
                if cappuccino_coins >= cappuccino_price:
                    change = round(cappuccino_coins - cappuccino_price, 2)
                    resources["money"] += cappuccino_price
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    print(f"Here is ${change} in change.")
                    print("Here is your cappuccino. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")
   

keep_running = True
while keep_running: 
    drink = input("What would you like? espresso($1.50), latte($2.50), cappuccino($3.00): ")
    if drink == "espresso":
        espresso()
    elif drink == "latte":
        latte()
    elif drink == "cappuccino":
        cappuccino()
    elif drink == "report":
        resource()
    elif drink == "off":
        keep_running = False
    else:
        print("Invalid input")