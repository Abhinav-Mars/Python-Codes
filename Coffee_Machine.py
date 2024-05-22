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
}

continue_serving = True
on_machine = True
total_profit = 0

def take_order():
    order = input("\nWhat would you like? (espresso/latte/cappuccino) : ")
    return order

def ask_and_cal_payment(order):
    print(f"Hey your {order} costs ${MENU[order]['cost']}")
    total = int(input("How many quarters?\n"))*0.25
    total += int(input("How many dimes?\n"))*0.10
    total += int(input("How many nickles?\n"))*0.05
    total += int(input("How many pennies?\n"))*0.01
    return total

def check_payment(order):
    given_money = ask_and_cal_payment(order)
    profit = 0
    if given_money > MENU[order]['cost'] :
        update_resources(order)
        print(f"\nHey! Here is your {order}...Enjoy your drink☕\n")
        change = given_money - MENU[order]['cost']
        rounded_change = round(change,2)
        print(f"Andddd...Here is your change {rounded_change}\n")
        profit += MENU[order]['cost']
        
    elif given_money == MENU[order]['cost'] :
        update_resources(order)
        print(f"\nHey! Here is your {order}...Enjoy your drink☕\n")
        profit += MENU[order]['cost']
    elif given_money < MENU[order]['cost'] :
        print(f"\nThe amount paid is insufficient...Returning the amount")
    
    return profit

def update_resources(order):
    if order == "latte" or order == "cappuccino":
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    elif order == "espresso":
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

def print_resources():
    print("Resources Report :")
    print(f"Remaining Water = {resources['water']}")
    print(f"Remaining Milk  = {resources['milk']}")
    print(f"Remaining Coffee = {resources['coffee']}")
    print(f"Total Cash = ${total_profit}")

while continue_serving and on_machine :
    order = take_order()
    if order == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            total_profit = total_profit + check_payment("espresso")
        else:
            print("Sorry...insufficient resources\n")
    elif order == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            total_profit = total_profit + check_payment("latte")   
        else:
            print("Sorry...insufficient resources\n")
    elif order == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            total_profit = total_profit + check_payment("cappuccino")  
        else:
            print("Sorry...insufficient resources\n")
    elif order == "off":
        print("Turning off....")
        break
    elif order == "report":
        print_resources()
    else:
        print("That item is not available")
    
        
        
         
            
            
            