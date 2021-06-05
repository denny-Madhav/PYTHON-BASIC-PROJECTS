from turtle import Turtle, Screen
import turtle as t
import random

screen = Screen()
screen.setup(width=600, height=600)

color=["red","orange","yellow","green","blue","purple","black"]
hmm = 0
count=0
race = False
tuts=[]
for i in range (0,7):

    hmm += 35
    tut = Turtle(shape="turtle")
    tut.color(color[count])
    count+=1
    tut.penup()
    tut.goto(x=-285,y=-120+hmm)
    tuts.append(tut)


user=screen.textinput(title="Turtle race", prompt="which turtle will win the race:\nRed\tOrange\tYellow\nGreen\tBlue\tPurple\tBlack").lower()
print(f"you choose : {user}")
if user:
    race = True

while race:
    for i in tuts:
        if i.xcor()>=300:
            win = i.pencolor()
            if win == user:
                print(f"You won, {win} finished the race first")
                race=False
            else:
                print(f"You lose, {win} finished the race first")
                race = False
        dis = random.randint(0, 10)
        i.fd(dis)



screen.exitonclick()