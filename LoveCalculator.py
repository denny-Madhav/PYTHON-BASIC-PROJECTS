print("welcome.")

me = input("Enter your full name : ")
you = input("Enter there full name : ")

print(f"\nYour name : {me}")
print(f"Their name : {you}")

com = me+you
lcom=com.lower()

t=lcom.count('t')
r=lcom.count('r')
u=lcom.count('u')
e=lcom.count('e')
true=t+r+u+e;

l=lcom.count('l')
o=lcom.count('o')
v=lcom.count('v')

love = l+o+v+e;

final=str(true)+str(love)
finalC=(int(final))
print("Your love percent is "+str(final)+"%")

if finalC >=90:
    print("You are just perfect for each other")
elif finalC <90 and finalC >=75:
    print("You are best together")
elif finalC <75 and finalC >50:
    print("you can make it work together")
elif finalC <50 and finalC >35:
    print("chances are less but still hope for the best")
elif finalC <35:
    print("you are like coke and mentos")

