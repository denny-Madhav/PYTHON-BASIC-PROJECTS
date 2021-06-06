from turtle import Turtle, Screen
screen=Screen()
NPOS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():

    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head=self.segs[0]

    def create_snake(self):
        for pos in NPOS:
            self.addsegment(pos)

    def addsegment(self, pos):
        news = Turtle("square")
        news.color("white")
        news.penup()
        news.goto(pos)
        self.segs.append(news)

    def extend(self):
        self.addsegment(pos=self.segs[-1].position())

    def move(self):
        for seg in range(len(self.segs) - 1, 0, -1):
            newx = self.segs[seg - 1].xcor()
            newy = self.segs[seg - 1].ycor()
            self.segs[seg].goto(newx, newy)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)









