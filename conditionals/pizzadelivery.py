#small = 110
#medium = 160
#large = 220
#small pep =15
#med large pep = 30;
#cheese = 20

size=input("choose a size of pizza S M OR L : ")
pep=input("do u want peproni on it Y or N : ")
che=input("do u want extra cheese Y or N : ")
bill = 0

if size =="s":
    bill=bill+110
elif size == "m":
    bill=bill+160
elif size == "l":
    bill=bill+220

if pep == "y":
    if size == "s":
        bill = bill +15
    else:
        bill = bill + 30

if che =="y":
    bill=bill+20
    print(f"TOTAL BILL AMOUNT IS {bill}")

