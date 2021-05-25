print("Hello welcome to bidding project")
values={}
bid= False

def high(record):
    hb=0
    for bidder in record:
        higha = record[bidder]
        if higha > hb:
            hb = higha
            winner=bidder
    print(f"The winner is {winner} with price {hb}")

while not bid:
    name = input("Enter your name :")
    price = int(input("Enter the ammount for bidding"))
    values[name]=price
    asks= input("are there any other bidders 'yes' or 'no'")
    if asks == "no":
        bid=True
        high(values)









