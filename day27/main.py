from tkinter import *

window = Tk()
window.title("Converter")
window.config(padx= 20 , pady = 20)


def convert():
    miles = float(input.get())
    label_3.config(text=round(miles*1.60934 , 1))

input = Entry(width=7)
input.focus()
input.grid(column=1 , row= 0)

label_1 = Label(text="Miles")
label_1.grid(column= 2, row = 0)

label_2 = Label(text="is equals to ")
label_2.grid(column=0, row= 1)

label_3 = Label(text="0")
label_3.grid(column= 1 , row= 1)

label_4 = Label(text="km")
label_4.grid(column= 2 , row= 1)

button = Button(text="Convert" , command=convert)
button.grid(column =1 , row = 2)




window.mainloop()
