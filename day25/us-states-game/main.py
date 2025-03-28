import turtle
import pandas
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.setup(725 , 491)
screen.title("U.S states game")
screen.bgpic(image)
data = pandas.read_csv("50_states.csv")
states_names = data.state.to_list()
print(states_names)
game_on = True
guessed = []




while len(guessed) < 50:
    answer = screen.textinput(f"{len(guessed)} / 50 correct" , "what is another state name").title()
    if answer == "Exit":
        missed = []
        for name in states_names :
            if name not in guessed:
                missed.append(name)
        missing = pandas.DataFrame(missed)
        missing.to_csv("to learn states.csv")
        break
    elif answer in states_names and answer not in guessed :
               guessed.append(answer)
               name = turtle.Turtle()
               name.hideturtle()
               name.penup()
               state = data[data.state == answer]
               name.goto(int(state.x) , int(state.y))
               name.write(f"{answer}", True, "center")


