from items import menu,resource,profit


def availabe(check):
    """checks weather resources are availabe or not"""
    enough=True
    for item in check:
       if check[item] >=resource[item]:
           print(f"Sorry there is no enough {item} ")
           enough= False
    return enough


def coins():
    """Returns the total calculated from coins inserted."""
    print("please insert coins.")
    total = int(input("How many one rupee coins : "))
    total = total+(2*int(input("How many two rupee coins : ")))
    total = total+(5*int(input("How many five rupee coins : ")))
    return total


def transaction(money,cost):
    """this is true if the payment is successful"""
    if money >= cost:
        change = money - cost
        print(f"cost of the {user} is {cost}")
        print(f"here is the change {change}")
        global profit
        profit=profit+cost
        return True

    else:
        print("sorry that is not enough money,Money refunded.")
        return False


def make_coffee(dname,items):
    """reduces resources resources after giving coffee"""
    for item in items:
        resource[item] -= items[item]
    print(f"Here is your {dname}")


print("This is coffee machine program")
on=True

while on:
    print("What would like to have?\n\tcoffee\n\tstrong coffee\n\tsugarless coffee\n\tblack coffee")
    user = input("\nEnter here : ").lower()
    if user =="off":
        on = False
    elif user == "report":
        print(f"water : {resource['water']}ml")
        print(f"milk : {resource['milk']}ml")
        print(f"sugar : {resource['sugar']}gm")
        print(f"coffee : {resource['coffee powder']}gm")
        print(f"money : {profit} rupees")
    else:
        drink = menu[user]
        if availabe(drink["ingredients"]):
         payment = coins()
         if transaction(payment,drink["cost"]):
             make_coffee(user,drink["ingredients"])











