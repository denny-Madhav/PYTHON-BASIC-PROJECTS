from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("PING PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
points = Score()


screen.listen()
screen.onkey(r_paddle.Up,"Up")
screen.onkey(r_paddle.Down,"Down")
screen.onkey(l_paddle.Up,"w")
screen.onkey(l_paddle.Down,"s")


game = True
while game:
    time.sleep(ball.ms)
    screen.update()
    ball.move()

    #collision with top or bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

   #collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
        print("contact")
        ball.bounce_x()

    # R paddle
    if ball.xcor() > 380:
        ball.reset()
        points.lp()
    # L paddle
    if ball.xcor() < -380:
        ball.reset()
        points.rp()


screen.exitonclick()