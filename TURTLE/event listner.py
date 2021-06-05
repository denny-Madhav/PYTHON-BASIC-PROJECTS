from turtle import Turtle, Screen


tut = Turtle()
screen = Screen()

def front():
    tut.fd(10)


def back():
    tut.back(10)


def left():
    tut.left(10)


def right():
    tut.right(10)


def clear():
    tut.home()
    tut.clear()



screen.listen()
screen.onkey(fun=front, key="w")
screen.onkey(fun=back, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()