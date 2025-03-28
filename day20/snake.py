from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-16, 0), (-32, 0)]
MOVE_DISTANCE = 16
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.back = self.segments[len(self.segments)-1]
        self.place = self.head.pos


    def create_snake(self):
        for position in STARTING_POSITIONS :
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def restart(self):
        for segment in self.segments :
            segment.hideturtle()
            segment.teleport(10000,10000)
        self.segments.clear()
        self.__init__()

    def grow(self):
        tail = Turtle("square")
        tail.color("white")
        tail.penup()
        tail.goto(self.back.position())
        self.segments.append(tail)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moving(self):
        for segment_number in range(len(self.segments)-1 , 0 , -1 ):
            new_x = self.segments[segment_number -1].xcor()
            new_y = self.segments[segment_number -1].ycor()
            self.segments[segment_number].goto(new_x , new_y)
        self.head.forward(MOVE_DISTANCE)

#