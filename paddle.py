from alien import Turtle
from colors import COLORS

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.color(COLORS[0])
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)


    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())



