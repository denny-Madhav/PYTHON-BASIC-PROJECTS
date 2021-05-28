print("Hello and welcome to number guessing game")
def hello():
    game = False
    while not game:
        # picking a random number
        import random

        number = [0]
        for n in range(100):
            number.append(n + 1)
        print("I'm choosing a number between 1 - 100, you need to guess it.")
        choosen_number = random.choice(number)
       # print(choosen_number)

        # Game_hardness
        lives = 0
        difficulty = input("Choose difficulty - type 'easy' or 'hard' : ")
        if difficulty == "easy":
            lives = 10
        elif difficulty == "hard":
            lives = 5
        else:
            print("you have entered an invalid input try again")
            exit()
        print(f"you have {lives} chances to guess the correct number")

        # logic loop
        loop = False
        while not loop:
            guess = int(input("\nEnter guessing number : "))
            if guess == choosen_number:
                print("WOW you made it, its a correct guess")
                loop = True
            elif lives == 0:
                print(f"you ran out of lives, the number i have chossed is {choosen_number} try again")
                loop = True
            elif guess > choosen_number:
                print("Wrong ,Guessed value is high")
                lives = lives - 1
                print(f"no.of chances left : {lives}")
            elif guess < choosen_number:
                print("Wrong ,Guessed value is Low")
                lives = lives - 1
                print(f"no.of chances left : {lives}")

        # exit or retry
        gamee = input("Do u wanna play again, Type 'yes' or 'no' :")
        if gamee == "yes":
            hello()
        elif gamee == "no":
            exit()
        else:
            print("entered an invalid input, Try again")
hello()




