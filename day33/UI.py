from tkinter import *
from tkinter import messagebox, Variable

from main import currency_code ,exchange_rates
currency_l = "USD"
currency_r = "SAR"

window = Tk()
window.title("Currency Exchanger")
window.config(padx = 50 , pady  = 50)

input_label = Label()
input_label.config(text=f"{currency_l}")
input_label.grid(column=1, row = 1)

input_currency = Entry(width=10)
input_currency.focus()
input_currency.grid(column=1, row =2)

equals = Label(text=" = ")
equals.grid(column=2 , row =2 , padx=20)

output_label = Label(text =f"{currency_r}")
output_label.grid(column =3, row = 1)

output_count = Entry(width=10)
output_count.grid(column=3, row =2)

def exchange():
    output_count.delete(0, END)
    try :
       main_currency = float(input_currency.get())
    except ValueError :
        messagebox.showerror(title="Invalid Inputs" , message="Please inter a valid number")
        input_currency.delete(0 ,END)
    else:
        output = main_currency * (1 / exchange_rates[currency_l]) * exchange_rates[currency_r]
        output_count.insert(0, round(output , 3))

convert_button = Button(text="Convert" , width =10 , command=exchange)
convert_button.grid(column=1 , row= 3 , columnspan= 3 ,pady = 15)


#Listbox
def listbox_used_l():
    global currency_l
    # Gets current selection from listbox
    selection_l = currencies_l.get(currencies_l.curselection())
    currency_l = currency_code[items.index(selection_l)]['AlphabeticCode']
    input_currency.delete( 0 ,END )
    input_label.config(text=f"{currency_l}")




items = []
for code in currency_code:
    items.append(code['Currency'])

list_items = Variable(value = items)
currencies_l = Listbox(height= 4 ,width=18 , listvariable=list_items)
currencies_l.grid(column=0 , row = 5 , pady= 5 ,padx=5  , columnspan=2)

change_button_l = Button(text="Change currency" , command= listbox_used_l)
change_button_l.grid(column=0 , row = 4 , pady=10  , padx = 5 , columnspan=2)

def listbox_used_r():
    global currency_r
    # Gets current selection from listbox
    selection_r = currencies_r.get(currencies_r.curselection())
    currency_r = currency_code[items.index(selection_r)]['AlphabeticCode']
    output_count.delete(0, END)
    output_label.config(text=f"{currency_r}")

currencies_r = Listbox(height= 4 ,width=18 , listvariable=list_items)
currencies_r.grid(column=2 , row = 5 , pady= 5 ,padx = 5, columnspan=2)

change_button_r = Button(text="Change currency" , command= listbox_used_r)
change_button_r.grid(column= 2 , row = 4 , pady=10  , padx = 5 , columnspan=2)





window.mainloop()