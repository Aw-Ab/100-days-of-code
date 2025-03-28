from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(0 ,270)
        self.color("white")
        with open("scores.txt" ) as file:
             self.highest = int(file.read())
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highest}", False, "center" , ('Arial' ,20 ,'normal'))

    def increase(self):
        self.score += 1
        self.update_board()

    def restart(self):
        if self.score > self.highest:
            self.highest = self.score
            with open("scores.txt" , 'w') as file :
                file.write(str(self.highest))
        self.score = 0
        self.update_board()

"""   def game_over(self):
        self.clear()
        self.home()
        self.color("red")
        self.write(f"Game Over ! \nFinal score : {self.score}" , False , "center" ,('countiria' ,20 ,'bold') )
"""
