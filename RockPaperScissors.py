import random

list=["ROCK","PAPER","SCISSOR"]
print("pick a number \n0:ROCK\n1:PAPER\n2:SCISSOR")

uip=int(input("Enter here:"))
if uip>2:
    print("it's an invalid number you lose")
    exit()
cip=random.randint(0,2)

print(f"\nYou choose :{list[uip]}\nComputer choose:{list[cip]}")

if list[uip] == list[cip]:
    print("it's a draw")
elif uip == 0 and cip == 2:
    print("You won")
elif uip == 1 and cip == 0:
    print("You won")
elif uip == 2 and cip == 1:
    print("you won")
else:
    print("you lose and computer won")

