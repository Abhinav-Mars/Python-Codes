from turtle import Turtle, Screen

mars = Turtle()
mars.color("blue","orange")

for i in range(10):
    mars.forward(10)
    mars.penup()
    mars.forward(10)
    mars.pendown()
    
screen = Screen()
screen.exitonclick()