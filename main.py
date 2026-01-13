from tkinter import *
from tkinter import messagebox
from pandas.core.accessor import delegate_names
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for letter in range(randint(8, 10))]
    passowrd_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_numbers + password_letter + passowrd_symbols
    shuffle(password_list)

    password = "".join(password_list)
    passw_i.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_i.get()
    email = email_i.get()
    passwo = passw_i.get()

    new_data = {
        website: {
            "email": email,
            "password": passwo
        }
    }

    if len(website) == 0 or len(passwo) == 0:
        messagebox.showinfo(title="Oops...", message="Please make sure you have not left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
                # file doesn't exist OR is empty/invalid
                data = {}
        else:
            # update old data with new data
            data.update(new_data)
            # save updated data back to the file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_i.delete(0, END)
            passw_i.delete(0, END)
# ---------------------------------FIND PASSWORD-----------------------------#
def find_password():
    website = website_i.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username/Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
# window.wm_minsize(width=, height=500)
window.title("Password Manager")
window.grid()
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(height=200, width=200)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1, row=0)

#Labels
website_l=Label(text="Website:")
website_l.grid(column=0, row=2, columnspan=1)

email_l=Label(text="Email/Username:")
email_l.grid(column=0, row=3, columnspan=1)

passw_l=Label(text="Password:")
passw_l.grid(column=0, row=4, columnspan=1)

#Inputs
website_i=Entry(width=41)
website_i.focus()
website_i.grid(column=1, row=2)

email_i=Entry(width=60)
email_i.insert(0, "alexandersamuel@gmail.com")
email_i.grid(column=1, row=3, columnspan=2)

passw_i=Entry(width=41)
passw_i.grid(column=1, row=4)

#Buttons
gen=Button(text="Generate Password", command=generate_password)
gen.grid(column=2, row=4)

ad=Button(text="Add", width=51,command=save)
ad.grid(column=1,row=5,columnspan=2)

search_button=Button(text="Search",width=14,command=find_password)
search_button.grid(column=2,row=2)


window.mainloop()
