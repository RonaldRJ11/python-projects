from data import menu # type: ignore

resource = {"water" : 3000,
            "coffee" : 100,
            "milk" : 2000}
def drink():
    global resource
    need = input("What would you like to drink from the below list? [espresso/latte/cappuccino] ")
    if need == "report":
        for item in resource:
            print(f"{item} : {resource[item]} ml")
        drink()
    elif need == "off":
        print("Thankyou!!!")
    elif need in ["espresso", "latte", "cappuccino"]:
        temp = True
        for item in menu[need]["ingredients"]:
            if menu[need]["ingredients"][item] > resource[item]:
                temp = False
                break
        if temp == True:
            print(f"Your {need} costs ${menu[need]["cost"]} Please insert coins.")
            total = int(input("How many Quarter($0.25) would you like to insert : ")) * 0.25
            total += int(input("How many Dime($0.1) would you like to insert : ")) * 0.10
            total += int(input("How many Nickel($0.05) would you like to insert : ")) * 0.05
            total += int(input("How many Penny($0.01) would you like to insert : ")) * 0.01
            if total >= menu[need]["cost"]:
                if total > menu[need]["cost"]:
                    print(f"Here is ${round((total - menu[need]['cost']),2)} in change.", end = " ")
                else:
                    print(f"Thanks for giving the right change.", end = " ")
                print(f"Here is your {need}, Enjoy!!!")
                for item in menu[need]["ingredients"]:
                    resource[item] -= menu[need]["ingredients"][item]
                drink()
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {item}.")
            drink()
    else:
        print("Please enter the right input.")
        drink()

drink()