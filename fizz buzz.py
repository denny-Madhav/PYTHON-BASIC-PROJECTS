

for number in range(1,101):
    if number%3==0 and number %5==0:
         print("'FizzBuzz' divisible by both 3 and 5")
    elif number%3==0:
        print("'Fizz' only divisible by 3")
    elif number%5==0:
        print("'Buzz' only divisible by 5")
    else:
        print(number)
