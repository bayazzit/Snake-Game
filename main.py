import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=410, height=410)
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
    if snake.head.xcor() > 190 or snake.head.ycor() > 200 or snake.head.xcor() < -200 or snake.head.ycor() < -190:
        scoreboard.reset()
        snake.reset()
        game_is_on = False

    # Detect collusion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 4:
            scoreboard.reset()
            snake.reset()
            game_is_on = False

screen.exitonclick()
