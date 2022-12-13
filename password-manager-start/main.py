import json
from tkinter import *
from tkinter import messagebox
import random as rd
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '*']


def create_password():
    n_letters = rd.randint(5, 8)
    n_symbols = rd.randint(1, 3)
    n_numbers = rd.randint(2, 4)

    password_num = [rd.choice(numbers) for char in range(n_numbers)]
    password_letters = [rd.choice(letters) for char in range(n_letters)]
    password_symbols = [rd.choice(symbols) for char in range(n_symbols)]
    password_list = password_letters + password_symbols + password_num
    rd.shuffle(password_list)
    password = "".join(password_list)
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
position = 0


def save():
    try:
        file_test = open("Data.json", 'r')
        if len(file_test.read()) == 0:
            file = open("Data.json", 'w')
            json.dump({}, file)
            file.close()
        file_test.close()
    except FileNotFoundError:
        file_test = open("Data.json", 'w')
        json.dump({}, file_test)
        file_test.close()
    with open("Data.json", 'r') as file:
        data = json.load(file)
        web = entry_web.get()
        password = entry_pass.get()
        username = entry_user.get()
        new_data = {
            web: {
                "email": username,
                "password": password,
            }
        }
        data.update(new_data)

        if len(web) == 0 or len(password) == 0 or len(username) == 0:
            messagebox.showinfo(title="Oops",
                                message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=web, message=f"There are the details entered:\nEmail: {username}\n"
                                                      f"Password: {password}\nIs this ok to save?")
            if is_ok:
                with open("Data.json", "w") as file_w:
                    json.dump(data, file_w, indent=1)
                entry_web.delete(0, END)
                entry_user.delete(0, END)
                entry_pass.delete(0, END)
            else:
                pass


# ---------------------------- SEARCH ------------------------------- #
def search():
    with open("Data.json", "r") as file:
        data = json.load(file)
        web = entry_web.get()
        try:
            information = data[web]
            messagebox.showinfo(title=web,
                                message=f"Email/Username: {information['email']}\n"
                                        f"Password: {information['password']}")
        except KeyError:
            messagebox.showinfo(title="Oops",
                                message="Don't have information about this web")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189)
photo = PhotoImage(file="logo.gif")
canvas.create_image(100, 95, image=photo)
canvas.grid(row=0, column=1)

# website
label_web = Label(text="Website:")
label_web.grid(row=1, column=0)

entry_web = Entry(width=32)
entry_web.grid(row=1, column=1)
entry_web.insert(0, "https://")

# Username
label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)

entry_user = Entry(width=51)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, "name")

# Password
label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

entry_pass = Entry(width=32)
entry_pass.grid(row=3, column=1)
entry_pass.insert(0, "*****")

# Button Generate Password
button_pass = Button(text="Generate Password",  highlightbackground="black", command=create_password)
button_pass.grid(row=3, column=2)

# Button Add
button_add = Button(text="Add", width=33, highlightbackground="black", command=save)
button_add.grid(row=4, column=1, columnspan=2)

# Button Search
button_search = Button(text="Search", width=13, highlightbackground="black", command=search)
button_search.grid(row=1, column=2)

window.mainloop()





