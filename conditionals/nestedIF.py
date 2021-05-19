print("welcome to water ride ticker counter.!!")
h=int(input("mention your height in cm : "))
a = int(input("mention your age : "))

if h>=120:
    print("\nyou are eligible to enter water ride.")
    if a>=18:
        print("please pay 150 rupees to generate ticket.\n")
        print("\tstay safe and enjoy the ride.")
    else:
        print("please pay 100 rupees to generate ticket.\n")
        print("\tstay safe and enjoy the ride.")

else:
    print("better luck next year kiddo")