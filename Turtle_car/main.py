import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


tut = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tut.up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1 )
    screen.update()

    cars.create_car()
    cars.move()

    #detect collision
    for i in cars.car:
        if i.distance(tut) < 20:
            game_is_on = False
            score.gdone()
    #levelUP
    if tut.finish():
       tut.hstart()
       cars.level()
       score.levelup()




screen.exitonclick()