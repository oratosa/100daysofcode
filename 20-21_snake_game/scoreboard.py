from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.high_score = self.read_high_score_from_file()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_on_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def read_high_score_from_file(self):
        dir = os.path.dirname(__file__)
        with open(f"{dir}/data.txt", "r") as f:
            previous_high_score = int(f.read())
            return previous_high_score

    def write_high_score_on_file(self, score):
        dir = os.path.dirname(__file__)
        with open(f"{dir}/data.txt", "w") as f:
            f.write(str(score))
