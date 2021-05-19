height=input("your height in meters : ")
weight=input("your weight in kg : ")
bmi=float(weight)/float(height) ** 2

if bmi<=18.5:
    print(f"your are under weight your BMI is {round(bmi,2)}")
elif bmi<=25:
    print(f"your are normal weight your BMI is {round(bmi,2)}")
elif  bmi<=30:
    print(f"your are over weight your BMI is {round(bmi,2)}v")
elif  bmi<35:
    print(f"your are  Obese your BMI is {round(bmi,2)}")
else:
    print(f"OMG u are way too obese your BMI is {round(bmi,2)}")

