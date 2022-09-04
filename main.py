import time
from turtle import Screen, Turtle

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Play with arrows
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
# Play with WASD
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    snake.move()

    # Detect collusion with food
    if snake.segments[0].distance(food) <= 6:
        food.change_food_position()
        snake.extend()
        scoreboard.add_new_score()

    # Detect collusion with wall
    if snake.head.xcor() > 235 or snake.head.ycor() > 240 or snake.head.xcor() < -245 or snake.head.ycor() < -235:
        game_is_on = False
        scoreboard.game_over()

    # Detect collusion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 4:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
