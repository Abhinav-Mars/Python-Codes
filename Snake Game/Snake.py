from turtle import Turtle

TURTLE_POSITIONS = [0,-20,-40]
MOVE_DIST = 20
class Snake:
    
    def __init__(self):
        self.turtles = []
    
    def create_snake(self):
        for i in range(3):
   
            mars = Turtle(shape="square")
            mars.color("LawnGreen","LawnGreen")
            mars.penup()
            mars.goto(x=TURTLE_POSITIONS[i],y=0)
            mars.speed(3)
            self.turtles.append(mars)
    
    def grow_snake(self):
        
        extra_seg = Turtle(shape="square")
        extra_seg.color("LawnGreen","Lawngreen")
        extra_seg.penup()
        extra_seg.goto(self.turtles[-1].xcor(),self.turtles[-1].ycor())
        self.turtles.append(extra_seg)

    def move_snake(self):
        for i in range(len(self.turtles) - 1,0,-1):
            self.turtles[i].goto(x=self.turtles[i-1].xcor(),y=self.turtles[i-1].ycor())
        self.turtles[0].forward(MOVE_DIST)
    
    #controls
    def go_up(self):
        if self.turtles[0].heading() == 0:
            self.turtles[0].left(90)
            
        elif self.turtles[0].heading() == 180:
            self.turtles[0].right(90)

    def go_down(self):
        if self.turtles[0].heading() == 0:
            self.turtles[0].right(90)
            
        elif self.turtles[0].heading() == 180:
            self.turtles[0].left(90)
            
    def go_left(self):
        if self.turtles[0].heading() == 90:
            self.turtles[0].left(90)
        
        elif self.turtles[0].heading() == 270:
            self.turtles[0].right(90)
    
    def go_right(self):
        if self.turtles[0].heading() == 90:
            self.turtles[0].right(90)
        
        elif self.turtles[0].heading() == 270:
            self.turtles[0].left(90)