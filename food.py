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


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(generate_color())
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        x_core = random.randint(-275, 275)
        y_core = random.randint(-275, 275)
        self.goto(x_core, y_core)

