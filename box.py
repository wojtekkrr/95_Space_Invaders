from alien import Turtle
from colors import COLORS_BOXES
from random import randint


class Box(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(COLORS_BOXES[randint(0, 3)])
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)

    # Usunięcie obiektu box z widoku
    def destroy_box(self):
        self.goto(10000, 10000)
