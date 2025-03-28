from tkinter import *
import pandas
import random
#
FONT = ("Courier" , 35 ,"normal")
BACKGROUND_COLOR = "#B1DDC6"
dictionary = {}
record = {}

#
try :
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError :
    original_data = pandas.read_csv("data/french_words.csv")
    dictionary = original_data.to_dict(orient="records")
else :
    dictionary = data.to_dict(orient="records")


def random_choice():
    global record
    record = random.choice(dictionary)
    print(record)
    pick_word()
    window.after(3000 , change )

def change():
    canvas.create_image(400, 263, image=back_card_img)
    canvas.create_text(400, 150, text=f"English", fill="white", font=("arial" , 40 , "italic"))
    canvas.create_text(400, 263, text=f"{record['English']}", fill="white", font=("ariel" , 46 , "bold"))

def pick_word():
    canvas.create_image(400, 263, image=front_card_img)
    canvas.create_text(400, 150, text=f"French", fill="black", font=("arial" , 40 , "italic"))
    canvas.create_text(400, 263, text=f"{record['French']}", fill="black", font=("ariel" , 46 , "bold"))




#
def to_learn():

    try :
        dictionary.remove(record)
        new_dicit = pandas.DataFrame(dictionary)
        new_dicit.to_csv("data/words_to_learn.csv" , index = False)
        print(len(new_dicit))
    except ValueError:
        pass
    finally :
        random_choice()



#
window = Tk()
window.title("flashy")
window.config(bg=BACKGROUND_COLOR ,padx=50 ,pady=50)

canvas = Canvas(width=800 ,height= 526 ,highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400,263 , image=front_card_img)
canvas.create_text(400,263,text=f"Start ?" ,fill="black" , font=FONT)
canvas.grid(column=0 , row=0 ,columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img ,highlightthickness=0 , command= random_choice)
wrong_button.grid(column= 0 , row = 1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img , highlightthickness=0 , command=to_learn )
right_button.grid(column= 1 , row = 1)







window.mainloop()