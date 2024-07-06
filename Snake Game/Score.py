from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,277)
    
    def calc_score(self):
        self.score += 1
    
    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 16, "normal"))

        