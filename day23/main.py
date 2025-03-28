import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
cars = []
screen = Screen()
screen.setup(width=600, height=600)
player = Player()
scoreboard = Scoreboard()
screen.tracer(0)

screen.listen()
screen.onkey(player.up , "Up")
#screen.onkey(player.down , "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    mybe = random.randint(0 ,5)

    if mybe == 0 :
         carmanager = CarManager(cars)

    for car in cars :
        car.moveing()

        if car.distance(player.turtle.position()) < 28 :
            scoreboard.game_over()
            screen.exitonclick()
            game_is_on = False

    if player.turtle.ycor() > 280 :
        time.sleep(1.5)
        carmanager.next_level()
        scoreboard.levelup()
        player.reset()
