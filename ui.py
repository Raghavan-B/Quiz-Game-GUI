THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")

        self.window.config(bg = THEME_COLOR)
        self.window.config(padx=20,pady=20)

        self.score_label = Label(text="Score: 0",fg = "white",bg= THEME_COLOR)
        self.score_label.grid(row = 0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text = "Sample",fill = THEME_COLOR,font=("Arial",20,"italic"),width=260)
        self.canvas.grid(row = 1,column=0,columnspan=2,pady=50)

        right_key_img = PhotoImage(file = "images/true.png")
        
        self.true_key = Button(image=right_key_img,highlightthickness=0)
        self.true_key.grid(row=2,column=0)

        wrong_key_img = PhotoImage(file = "images/false.png")
        self.false_img = Button(image=wrong_key_img,highlightthickness=0)
        self.false_img.grid(row =2,column=1)

        self.get_next_question()        

        
        
        
        
        
        
        self.window.mainloop()

    def get_next_question(self):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text =q_text)
    