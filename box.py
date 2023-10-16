from alien import Turtle
from colors import COLORS
from random import randint


class Box(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(COLORS[randint(1, 4)])
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)

    # Usunięcie obiektu box z widoku
    def destroy_box(self):
        self.goto(10000, 10000)
