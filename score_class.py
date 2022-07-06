import turtle
from turtle import Turtle
import random

turtle.colormode(255)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_colors = (r, g, b)
    return generated_colors


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=275)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over, you faced with a wall or bitten by your self \n You're final score is: {self.score} ",
                   align="center", font=("arial", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.color(generate_color())
        self.update_score()
