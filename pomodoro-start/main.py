from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF8DC7"
RED = "#e7305b"
VIOLET = "#80489C"
BLUE = "#73bcd5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 1
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=VIOLET)
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 1:
        label.config(text="WORK", fg=RED)
        count_down(WORK_MIN*60)
    else:
        if reps % 8 == 0:
            label.config(text="BREAK", fg=VIOLET)
            count_down(LONG_BREAK_MIN*60)
        else:
            label.config(text="BREAK", fg=VIOLET)
            count_down(SHORT_BREAK_MIN*60)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 0:
            check.config(text="✓")
        else:
            check.config(text="")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), bg=BLUE, fg=VIOLET)
label.grid(row=0, column=1)

canvas = Canvas(window, width=800, height=498, bg=BLUE, highlightthickness=0)
photo = PhotoImage(file='snack.gif')
canvas.create_image(400, 249, image=photo)
timer_text = canvas.create_text(400, 249, text="00:00", font=(FONT_NAME, 60, "bold"), fill="black")
canvas.grid(row=1, column=1)

button_start = Button(text="Start", highlightbackground="black", bg=BLUE, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightbackground="black", bg=BLUE, command=reset_timer)
button_reset.grid(row=2, column=2)

check = Label(font=(FONT_NAME, 40, "normal"), bg=BLUE, fg=VIOLET)
check.grid(row=3, column=1)

window.mainloop()
