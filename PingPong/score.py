from turtle import Turtle, Screen

screen = Screen()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Ls = 0
        self.Rs = 0
        self.us()

    def us(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.Ls, align = "center", font=("lato",60,"bold"))
        self.goto(100, 200)
        self.write(self.Rs, align="center", font=("lato", 60, "bold"))

    def lp(self):
        self.Ls += 1
        self.us()

    def rp(self):
        self.Rs += 1
        self.us()

