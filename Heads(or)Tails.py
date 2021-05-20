import random

def coin():
    print("welcome to heads or tails")
    print("\npress 1 for heads and 0  for tails : ")
    ip = input("choose")
    if ip=="1":
        print("your choice is Heads")
    elif ip=="0":
        print("your choice is Tails")
    elif ip!="0" and ip!="1":
        print("invalid input")
        okay=input("\nPress 1 to re-enter input || press 0 to exit")
        if okay =="1":
            coin()



    HorT = random.randint(0,1)
    if HorT ==0:
        print("well it's tails")
    elif HorT ==1:
        print("Hmm its Heads")

coin()