from turtle import Turtle, Screen
class Paddle(Turtle):

    def __init__(self, postion):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(postion)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def Up(self):
        ny = self.ycor() + 35
        self.goto(x=self.xcor(), y=ny)

    def Down(self):
        ny = self.ycor() - 35
        self.goto(x=self.xcor(), y=ny)






