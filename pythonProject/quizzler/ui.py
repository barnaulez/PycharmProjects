from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.scores_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.scores_label.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="black")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Here is the question",
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.press_true)
        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.press_false)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill="black")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question's list")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def press_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.scores_label.config(text=f"Score: {self.quiz.score}")
