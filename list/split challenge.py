import random

print('Hai, welcome.!! Enter names of all customers with "," in between and let me choose one customer to pay the bill. \n ')
names=input("enter here : ")
sname=names.split(",")

print("\nThe name are : ")
print(*sname,sep="\n")

limit=len(sname)
ran=random.randint(0,limit-1)
print(f"\nWell i choose {sname[ran]} to pay the bill.!")



