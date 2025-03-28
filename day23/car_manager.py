from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self , group):
        self.create()
        group.append(self)


    def  create(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(0.9 , 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.speed("fastest")
        self.setx(340)
        self.sety(random.randint(-250 , 250 ))
        self.showturtle()

    def moveing(self):
        self.backward(random.randint(MOVE_INCREMENT,STARTING_MOVE_DISTANCE))

    def next_level(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
