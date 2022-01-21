from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_num = 0

        self.score = Label(text=f"Score: {self.score_num}", font=("Arial", 15, "normal"), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280
                                                     )
        self.canvas.grid(row=1, column=0,  columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.correct_answer)
        self.correct_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question, fill=THEME_COLOR)

    def correct_answer(self):
        if self.quiz.check_answer("True") and self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, fill="green")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.next_question)
            else:
                self.canvas.itemconfig(self.question_text, text=f"Your Score: {self.quiz.score}/{len(self.quiz.question_list)}")
                self.correct_button.config(state="disabled")
                self.wrong_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.question_text, fill="red")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.next_question)
            else:
                self.canvas.itemconfig(self.question_text, text=f"Your Score: {self.quiz.score}/{len(self.quiz.question_list)}")
                self.correct_button.config(state="disabled")
                self.wrong_button.config(state="disabled")

    def wrong_answer(self):
        if self.quiz.check_answer("False") and self.quiz.still_has_questions():
            self.score_num += 1
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, fill="green")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.next_question)
            else:
                self.canvas.itemconfig(self.question_text, text=f"Your Score: {self.quiz.score}/{len(self.quiz.question_list)}")
                self.wrong_button.config(state="disabled")
                self.correct_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.question_text, fill="red")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.next_question)
            else:
                self.canvas.itemconfig(self.question_text, text=f"Your Score: {self.quiz.score}/{len(self.quiz.question_list)}")
                self.wrong_button.config(state="disabled")
                self.correct_button.config(state="disabled")








