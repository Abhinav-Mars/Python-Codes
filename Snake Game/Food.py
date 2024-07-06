from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
        self.color('yellow')
        self.speed(0)
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    
    def relocate_food(self):
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
    
    
        