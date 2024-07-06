from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Score import Score

FIELD_LIMIT = 300

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("DarkMagenta")
my_screen.title("Snake Game 🐍")
my_screen.listen()
my_screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
player_score = Score()
snake.create_snake()


#controls
my_screen.onkey(key="Up",fun=snake.go_up)
my_screen.onkey(key="Down",fun=snake.go_down)
my_screen.onkey(key="Left",fun=snake.go_left)
my_screen.onkey(key="Right",fun=snake.go_right)

#snake moves
while game_on:
    my_screen.update()
    time.sleep(0.2)  
    
    snake.move_snake()
    player_score.display_score()
    
    #Detect the collison with food
    if (snake.turtles[0].distance(food.xcor(),food.ycor())<=15):
        food.relocate_food()
        snake.grow_snake()
        player_score.calc_score()
    #Detect collision with walls
    if (snake.turtles[0].xcor() >= FIELD_LIMIT or snake.turtles[0].xcor() <= -FIELD_LIMIT or snake.turtles[0].ycor() >= FIELD_LIMIT or snake.turtles[0].ycor() <= -FIELD_LIMIT):
        game_on = False
    #Detect self collision
    for i in snake.turtles[1:]:
        if (snake.turtles[0].position() == i.position()):
            game_on = False
            
my_screen.exitonclick()