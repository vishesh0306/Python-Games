from snake import Snake
from turtle import Screen
from food import Food
from score_board import Score
import time


screen = Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()


#       score count
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#     detecting the food
    for i in snake.segments:
        if i.distance(food) < 15:

                food.refresh()
                snake.extend()
                score.increase_score()



#       detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 240 or snake.head.xcor() < -290 or snake.head.ycor() < -240:
        score.game_over()
        game_is_on = False


#         detect collision with tail
#           if head collide with any segment then game over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
