from turtle import Screen
from snake_class import Snake
from food import Food
from score_class import Score
import time
window = Screen()
window.tracer(0)  # window.tracer(0) prevent from animations that we do not want to see
window.setup(width=600, height=600)
window.title("Snake Game")
window.bgcolor("black")
score = Score()
food = Food()
snake = Snake()
window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.right, "Right")
window.onkey(snake.left, "Left")
is_game_on = True
while is_game_on:
    window.update()  # window.update() after animation it will update the window or screen
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.extend_snake()
    # Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        is_game_on = False
        score.game_over()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()























window.mainloop()
