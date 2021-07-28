from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("UI Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=270,
                                                     text="hello",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 16, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=40)
        self.true_img = PhotoImage(file="images/true.png")
        self.true_b = Button(image=self.true_img, highlightthickness=0, command=self.selected_true)
        self.true_b.grid(row=2 , column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_b = Button(image=self.false_img, highlightthickness=0, command=self.selected_false)
        self.false_b.grid(row=2, column=1)

        self.get_next()


        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end.")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def selected_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def selected_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)





