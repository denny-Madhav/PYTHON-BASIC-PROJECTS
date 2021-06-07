from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.xm = 10
        self.ym  = 10
        self.ms=0.1

    def move(self):
        nx = self.xcor() + self.xm
        ny = self.ycor() + self.ym
        self.goto(nx, ny)

    def bounce_y(self):
        self.ym *= -1
        self.ms *= 0.9

    def bounce_x(self):
        self.xm *= -1
        self.ms *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ms = 0.1



