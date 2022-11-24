from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


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
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
position = 0


def save():
    global position
    with open("Data.txt", "a") as file:
        web = entry_web.get()
        password = entry_pass.get()
        username = entry_user.get()

        if len(web)==0 or len(password)==0 or len(username)==0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=web, message=f"There are the details entered:\nEmail: {username}\n"
                                                      f"Password: {password}\nIs this ok to save?")

            if is_ok:
                file.write(f"{web} | {username} | {password}\n")
                entry_web.delete(0, END)
                entry_user.delete(0, END)
                entry_pass.delete(0, END)
            else:
                pass



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

entry_web = Entry(width=35)
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.insert(0, "https://")

# Username
label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)

entry_user = Entry(width=35)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, "name")

# Password
label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

entry_pass = Entry(width=16)
entry_pass.grid(row=3, column=1)
entry_pass.insert(0, "*****")

# Button Generate Password
button_pass = Button(text="Generate Password",  highlightbackground="black", command=create_password)
button_pass.grid(row=3, column=2)

# Button Add
button_add = Button(text="Add", width=33, highlightbackground="black", command=save)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()





