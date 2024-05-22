import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)

mars = Turtle()
mars.speed('fastest')
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    mars.color(r,g,b)
    #else you can return the tuple (r,g,b)

for i in range(int(360/10)):
    random_color()
    mars.circle(100)
    mars.setheading(mars.heading()+10)

my_screen = Screen()
my_screen.exitonclick()
    
    