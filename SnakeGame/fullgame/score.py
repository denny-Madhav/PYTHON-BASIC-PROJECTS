from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s = 0
        self.penup()
        self.goto(x=0,y=250)
        self.color("red")
        self.write(f"Score : {self.s}", align="center", font=("Arial",24,"bold"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    def increase(self):
        self.s+=1
        self.clear()
        self.write(f"Score : {self.s}", align="center", font=("Arial", 24, "bold"))
