from tkinter import *

FONT = ("Calibri", 16, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

#Label
my_label1 = Label(text="Miles", font=FONT)
my_label1.grid(row=0, column=2)

my_label2 = Label(text="is equal to ", font=FONT)
my_label2.grid(row=1, column=0)

my_label3 = Label(text="Km", font=FONT)
my_label3.grid(row=1, column=2)

km = Label(text="0", font=FONT)
km.grid(row=1, column=1)
km.config(padx=5, pady=5)

#Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)


def calculate():
    mile = entry.get()
    b = round(float(mile)*1.609344, 2)
    km.config(text=b, font=FONT)


#Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
