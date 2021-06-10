from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time
score=0
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
point = Score()

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


    #detect collusion with food
    if snake.head.distance(food) < 15:
        print("collided")
        food.refresh()
        snake.extend()
        point.increase()


    #detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < - 295 or snake.head.ycor() > 295 or snake.head.ycor() < - 295:
        point.s_hs()
        snake.game_restart()


    #detect collision with tail
    for seg in snake.segs[1:]:
        if snake.head.distance(seg) < 10:
            point.s_hs()
            snake.game_restart()











screen.exitonclick()