from turtle import Turtle
from random import choice

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(("circle"))
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")


    def refresh(self):
        x = choice(range(-270, 270))
        y = choice(range(-270, 270))
        self.goto(x, y)


