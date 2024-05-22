from turtle import Turtle,Screen
import random

colors = ["dark green","crimson","green yellow","goldenrod","deep pink","dark orchid"]

mars = Turtle()
my_screen = Screen()

sides = [3,4,5,6,7,8,9,10]

def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        mars.forward(100)
        mars.right(angle)

for i in range(10):
    mars.color(random.choice(colors))
    draw_shape(sides[i])

my_screen.exitonclick()