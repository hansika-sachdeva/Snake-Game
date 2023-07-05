from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

play_again = "y"

while play_again == "y":

    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.set_random_pos()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
            game_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_on = False

    valid_ans = False
    play_again = screen.textinput(title="Play again?", prompt="Do you want to play again? Press y for yes and n for no ")
    while not valid_ans:
        if play_again.lower() == "y" or play_again.lower() == "n":
            valid_ans = True
        else:
            play_again = screen.textinput(title="Play again",
                                          prompt="Enter a valid answer. Do you want to play again? Press y for yes and n for no ")

screen.exitonclick()
