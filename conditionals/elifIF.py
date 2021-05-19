print("welcome to water ride ticker counter.!!")
h=int(input("mention your height in cm : "))
a = int(input("mention your age : "))
bill = 0;
if h>=120:
    print("\nyou are eligible to enter water ride.")
    if a<18:
        bill=130;
        print(f"You need to  pay {bill} rupees to generate ticket.\n")

    elif a>=18:
        bill =150;
        print(f"You need to  {bill} rupees to generate ticket.\n")

    else:
        bill = 100;
        print("You need to  {bill} rupees to generate ticket.\n")

    pic=input("do you want pictures of your water ride.? Y or N :")
    if pic =="y":
       bill=bill+50;
       print(f"\ttotal amount to be paid {bill}")
       print("\n\t STAY SAFE AND ENJOY THE RIDE")
    else:
        print(f"\n\ttotal amount to be paid {bill}")
        print("\t STAY SAFE AND ENJOY THE RIDE")
else:
    print("better luck next year kiddo")