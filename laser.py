from turtle import Turtle
from colors import COLORS, COLORS_BOXES




class Laser(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[2])
        self.shape("square")
        self.shapesize(stretch_wid=.2, stretch_len=.5)
        self.penup()
        self.goto(10000, -340)
        self.setheading(90)
        self.speed = 20
        self.flying = False

    # Przesunięie lasera
    def move(self):
        new_y = self.ycor() + self.speed
        self.goto(self.xcor(), new_y)

    # Przeniesienie lasera w kierunku statku
    def shoot(self, x_cordinate):
        if not self.flying:
            self.goto(x_cordinate, -340)
            self.flying = True

    # Usunięcie pocisku
    def delete_laser(self):
        self.goto(10000, -340)
        self.flying = False


