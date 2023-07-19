from turtle import Turtle

ALIGN = "center"
SCORE_FONT = ("Courier", 14, "normal")
GAME_FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_data.txt") as highscore_data:
            self.high_score = int(highscore_data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        self.snake_speed = 0.1

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=220)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGN, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore_data.txt", mode="w") as highscore_data:
                highscore_data.write(str(self.high_score))

        self.update_scoreboard()

        if self.score % 5 == 0:
            self.snake_speed *= 0.7

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=GAME_FONT)
        self.score = 0
