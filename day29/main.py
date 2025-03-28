from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import json
# import pyperclip

# ----------------------------Searching----------------------------------#
def searching():
    website = website_entry.get()
    try :
        with open("data.json" , "r") as file :
            my_users = json.load(file)
    except :
        messagebox.showerror(title="Empty!" ,message= f"The database is empty")
    else :

        if website in my_users :
            messagebox.showinfo(title=f"{website}",message=f"Email : {my_users[website]["email"]} \n Password : {my_users[website]["password"]}")
        else :
            messagebox.showerror(title="Not found" ,message= f"There is no data for '{website}' ")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generating():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # pyperclip.copy(password)
    return password

def generate():
    password_entry.delete(0 , END)
    password_entry.insert(0 , generating())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    user = {
        website :{
         "email" : email ,
         "password" : password
        }
    }
    if len(website) == 0 or len(email) ==0 or len(password) ==0:
        messagebox.showerror("Ooops !" , "Make sure to fill all the fields")
    elif len(password) < 8 :
        messagebox.showerror("Invalid Password" , "the password must have more than 8 characters")
    else :
        confirm = messagebox.askokcancel("Confirm" , f"Here is your information\nWebsite : {website}\nEmail/Username : {email}\n Password : {password}\n Is it ok to save?")
        if confirm:
            try :
                 with open("data.json", "r") as file:
                     data = json.load(file)
                     data.update(user)
            except FileNotFoundError:
                data = user
            except JSONDecodeError :
                data = user
            finally :
                with open("data.json" , "w") as file :
                     json.dump(data , file , indent=4)
                website_entry.delete(0 , END)
                password_entry.delete(0 , END)

# ---------------------------- UI SETUP ------------------------------- #

my_font = ("Arial" , 12 ,"normal")

window = Tk()
window.title("Password Generator")
window.config(padx = 20 , pady = 20)
window.minsize(500 , 400)


logo = PhotoImage(file="logo.png")
canvas = Canvas(width= 189 , height=200)
canvas.create_image(94.5 , 100, image=logo)
canvas.grid(column=1 , row = 1 , columnspan=1)

website_label = Label(text= "Website :" , highlightthickness=0 )
website_label.grid(column= 0 , row = 2 , padx = 0 , pady = 5)

website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column = 1 , row = 2 ,columnspan=1)
search_button = Button(text="Search", width=8 , command=searching)
search_button.grid(column=2 , row =2 )


email_label = Label(text= "Email/Username :" , highlightthickness=0 ,)
email_label.grid(column= 0 , row = 3 , padx = 20 , pady = 5)

email_entry = Entry(width=36)
email_entry.insert(0 , string= "someone@gmail.com")
email_entry.grid(column = 1 , row = 3 , columnspan = 3)



password_label = Label(text= "Password :" )
password_label.grid(column= 0 , row = 4 , pady = 5)
password_entry = Entry(width=25)
password_entry.grid(column = 1 , row = 4 )

password_button = Button(text="Generate" , command= generate )
password_button.grid(column=2 , row = 4)

add_button = Button(text="Add" , command= add_password , width=33)
add_button.grid(column=1 , row = 5 , pady = 5, columnspan=2)






window.mainloop()