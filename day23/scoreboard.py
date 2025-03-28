from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(-280 , 260)
        self.level = 1
        self.score()

    def levelup(self):
        self.clear()
        self.level += 1
        self.score()

    def score(self):
        self.write(f"Level : {self.level}" , False , "left" , ("Arial" , 20  , "normal"))

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER !" , False , "center" , FONT)

