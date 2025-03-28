import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counter = None
# ---------------------------- TIMER RESET ------------------------------- #
def resetting():
    global marks,reps
    window.after_cancel(counter)
    title.config(text = "Timer")
    canvas.itemconfig(timer , text="00:00")
    marks = ""
    check()
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global marks,reps
    check()
    reps += 1
    if reps == 8:
        title.config(text="Break" , fg=RED)
        count_down(10)
    elif reps % 2 != 0 :
        title.config(text = "Work" , fg=GREEN)
        count_down(6)
        marks += "0"
    else :
        title.config(text = "Break" , fg=PINK)
        count_down(3)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(the_time):
    mins = math.floor(the_time/60)
    secs = the_time % 60

    if secs < 10 :
        secs = f"0{secs}"

    canvas.itemconfig(timer , text =f"{mins}:{secs}")
    if reps > 8 :
        resetting()
    if the_time > 0:
        global counter
        counter = window.after(1000 ,count_down , the_time -1)
    else:
        start_count()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100 ,pady = 50 , bg=YELLOW)

#the "timer" title
title = Label(text="Timer", bg=YELLOW ,fg=GREEN , font=(FONT_NAME,50 , "bold"))
title.grid(column=1 , row =1 )

#The tomato pic
canvas = Canvas(width=200 , height=223 , bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100 ,110 , image= tomato_image)
timer = canvas.create_text(100 ,140 ,text="00:00" , fill="white",font=(FONT_NAME , 35 , "bold"))
canvas.grid(column = 1 , row =2)

#the checks
marks = ""
def check():
    check_marks.config(text=marks)

check_marks = Label(bg=YELLOW , fg=GREEN ,font=("Arial" , 16, 'bold'))
check_marks.grid(column= 1 ,row = 4, pady=10, padx= 5)


start_button = Button(text="Start", highlightthickness=0 , command= start_count )
start_button.grid(column = 0 , row = 3)


reset_button = Button(text="Reset" , highlightthickness=0 , command= resetting)
reset_button.grid(column=2 , row = 3)




window.mainloop()