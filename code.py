

print("Well come to split bill and tip calculator.\n")

bill= input("What is total bill amount ")

tip = input("What percent of bill you want to give as tip 5 , 10 or 15?? ")

n_o = input("How many people to split the bill ")

ttip=round((float(bill)*float(tip))/100,2);

print(f"Total tip = {ttip}")

epay=round((ttip+float(bill))/float(n_o),2);

print(f"Each person should pay {epay}")