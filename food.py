from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # stretch by factor of 0.5
        self.color("magenta")
        self.speed("fastest")
        self.set_random_pos()

    def set_random_pos(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        random_pos = (random_x, random_y)
        self.goto(random_pos)
