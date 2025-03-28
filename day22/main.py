#Pong game
from turtle import Screen
from paddles import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

right = 560
playing = True

screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 800)
screen.title("| Pong |")
bot = Paddle((560 , 0))
player = Paddle((-560 , 0))
scoreboard = Scoreboard()
ball = Ball()
line = ball.line()
screen.listen()
screen.onkey(player.up , "Up")
screen.onkey(player.down , "Down")

while playing :
    screen.update()
    ball.move()

    if ball.circle.ycor() < -360 or ball.circle.ycor() > 360:
        ball.bounce_y()

    if ball.circle.xcor() < -540 and ball.circle.distance(player) < 40 or ball.circle.xcor() > 540  and ball.circle.distance(bot) < 40:
        ball.bounce_x()

    elif ball.circle.xcor() < -620 :
        scoreboard.left_goal()
        time.sleep(1)
        ball.reset()

    elif ball.circle.xcor() > 620 :
        scoreboard.right_goal()
        time.sleep(1)
        ball.reset()


    time.sleep(0.08)
    screen.tracer(0)
    bot.moving()















screen.exitonclick()