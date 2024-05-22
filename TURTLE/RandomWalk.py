from turtle import Turtle,Screen
import random


mars = Turtle()

colors = ["dark green","crimson","green yellow","goldenrod","deep pink","dark orchid"]
directions = [0,90,180,270]

mars.speed(0)
mars.pensize(7)
for i in range(200):
    mars.color(random.choice(colors))
    mars.forward(25)
    mars.right(random.choice(directions))

my_screen = Screen()
my_screen.exitonclick()
