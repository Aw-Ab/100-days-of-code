from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(340)
        self.right_goals = 0
        self.left_goals = 0
        self.score()
    def score(self):
        self.write(f"{self.right_goals}     {self.left_goals}" , False , "center" ,("Courier", 32, "bold" ))

    def right_goal(self):
        self.right_goals +=1
        self.clear()
        self.score()

    def left_goal(self):
        self.left_goals +=1
        self.clear()
        self.score()