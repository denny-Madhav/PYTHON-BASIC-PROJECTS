from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()