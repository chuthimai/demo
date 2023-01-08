from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.scoreboard = Label()
        self.scoreboard.config(text="Score: 0", background=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1, pady=20, padx=20)

        self.quiz_box = Canvas()
        self.quiz_box.config(bg="white", width=300, height=250)
        self.quiz_text = self.quiz_box.create_text(
            150,
            125,
            width=250,
            text="This is QUIZ",
            font=FONT,
            fill=THEME_COLOR
        )
        self.quiz_box.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        self.true_button = Button(command=self.true_press)
        self.true_photo = PhotoImage(file="images/true.gif")
        self.true_button.config(
            image=self.true_photo,
            highlightbackground=THEME_COLOR
        )
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        self.false_button = Button(command=self.false_press)
        self.false_photo = PhotoImage(file="images/false.gif")
        self.false_button.config(
            image=self.false_photo,
            highlightbackground=THEME_COLOR
        )
        self.false_button.grid(row=2, column=1, pady=20, padx=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.quiz_box.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.quiz_box.itemconfig(self.quiz_text, text=q_text)
        else:
            self.quiz_box.itemconfig(
                self.quiz_text,
                text=f"The end of question\nYour score is {self.quiz.score}/{self.quiz.question_number}"
            )

    def true_press(self):
        check = self.quiz.check_answer("True")
        self.get_feedback(check)

    def false_press(self):
        check = self.quiz.check_answer("False")
        self.get_feedback(check)

    def get_feedback(self, is_right):
        if is_right:
            self.quiz_box.config(bg="#86C8BC")
        else:
            self.quiz_box.config(bg="#FEA1BF")
        self.window.after(500, self.get_next_question)


