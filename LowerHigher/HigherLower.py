#IMPORT WHAT ARE IMPORTANT
import random
import info
score=0
game = True
B=random.choice(info.data)
while game:
    #Generate a random account
    def rand():
        return random.choice(info.data)

    def assign(one):
        # Format the account data to printable format
        name = one["name"]
        desc = one["description"]
        coun = one["country"]
        return f"Name : {name} Country : {coun} Description : {desc} "

    def check(answer,a_follow,b_follow):
        if a_follow > b_follow:
            if answer == "a":
                return True
            else:
                return False
        elif b_follow > a_follow:
            if answer == "b":
                return True
            else:
                return False


    ##Use if statement to check if user is correct

    A=B
    B=random.choice(info.data)
    while A == B:
        B = random.choice(info.data)
    print(assign(A))
    print(assign(B))

    #user input
    answer = input("Who do you think has more followers A or B : ").lower()
    #check if user is correct.
    ##Get follower count of each account.
    a_follow = A["follower_count"]
    b_follow = B["follower_count"]
    print(a_follow)
    print(b_follow)

    correct = check(answer,a_follow,b_follow)
    #give user feedback on there guess.
    if correct:
        score +=1
        print(f"you are correct, current score : {score}")
    else:
        game=False
        print(f"you are wrong.final Score : {score}")


    #score keeping

    #make the game repeatable

    #making account at pos B become nect account pos A.