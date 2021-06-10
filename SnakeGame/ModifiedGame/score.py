from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s = 0
        with open("data.txt") as data:
            self.hs = int(data.read())
        self.penup()
        self.goto(x=0,y=250)
        self.color("red")
        self.hideturtle()
        self.uscore()

    def uscore(self):
        self.clear()
        self.write(f"Score : {self.s}  HighScore : {self.hs}", align="center", font=("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    def s_hs(self):
        if self.s > self.hs:
            self.hs = self.s
            with open("data.txt", mode="w") as data:
                data.write(f"{self.hs}")
        self.s = 0
        self.uscore()

    def increase(self):
        self.s += 1
        self.uscore()

