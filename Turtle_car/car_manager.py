from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car=[]
        self.cspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rc = randint(1,6)
        if rc == 1:
            nc = Turtle("square")
            nc.shapesize(stretch_wid=1, stretch_len=2)
            nc.penup()
            nc.color(choice(COLORS))
            ry = randint(-240,240)
            nc.goto(x=300,y=ry)
            self.car.append(nc)

    def move(self):
        for c in self.car:
            c.backward(STARTING_MOVE_DISTANCE)

    def level(self):
        self.cspeed += MOVE_INCREMENT





