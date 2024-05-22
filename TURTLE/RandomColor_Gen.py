import turtle as t
from turtle import Turtle,Screen
import random

t.colormode(255)
mars = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    mars.color(r,g,b)
    #else you can return the tuple (r,g,b)

directions = [0,90,180,270]

mars.speed(0)
mars.pensize(7)
for i in range(200):
    random_color()
    mars.forward(25)
    mars.right(random.choice(directions))

my_screen = Screen()
my_screen.exitonclick()