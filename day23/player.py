from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(STARTING_POSITION)
        self.turtle.showturtle()


    def reset(self):
        self.turtle.goto(STARTING_POSITION)


    def up(self):
        self.turtle.forward(MOVE_DISTANCE)

    def down(self):
        self.turtle.back(MOVE_DISTANCE)