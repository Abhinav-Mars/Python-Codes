from turtle import Turtle, Screen

mars = Turtle()

mars.shape("turtle")
mars.color("pink","orange")
for i in range(4):
    mars.forward(100)
    mars.right(90)

screen = Screen()
screen.exitonclick()