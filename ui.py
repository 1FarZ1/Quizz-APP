from tkinter import *
THEME_COLOR = "#375362"
class quizz_interface :
    def __init__(self,quizze):
        
        self.window=Tk()
        self.quizz=quizze
        self.window.title("Quizz_app")
        self.score=0
        self.leader=Label(text=f"score:{self.score}",bg=THEME_COLOR,font=("arail",15,"bold"),fg="White")
        self.leader.grid(row=0,column=1)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.quizz1=self.canvas.create_text(150,125,text="THE Quizz",font=("arail",15,"bold"),fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        pic=PhotoImage(file="QUIZZ_APP/images/true.png")
        pic2=PhotoImage(file="QUIZZ_APP/images/false.png")
        self.button=Button(image=pic,highlightthickness=0,command=self.true_pressed)
        self.button.grid(row=2,column=0)
        self.button1=Button(image=pic2,highlightthickness=0,command=self.wrong_pressed)
        self.button1.grid(row=2,column=1)   
        self.get_next()
        self.answr=0
        self.window.mainloop()
    def get_next(self):
        if self.quizz.still_has_questions() :
            self.canvas.config(bg="white")
            self.leader.config(text=f"Score :{self.score}")
            question=self.quizz.next_question()
            self.canvas.itemconfig(self.quizz1,text=question)
        else :
            self.canvas.config(bg="white")
            self.leader.config(text=f"Score :{self.score}")
            self.canvas.itemconfig(self.quizz1,text=f"The Game is over You got {self.score}/10")
            self.button.config(state="disabled")
            self.button1.config(state="disabled")
    def true_pressed(self):
        self.answr=self.quizz.check_answer("True")
        self.check_answer()
    def wrong_pressed(self):
        self.answr=self.quizz.check_answer("False")
        self.check_answer()
    def check_answer(self):
        if self.answr == True :
            self.score = self.score + 1 
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="Red")
        self.window.after(1000,self.get_next)