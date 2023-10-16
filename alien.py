from turtle import Turtle
from colors import COLORS

class Alien(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color(COLORS[4])
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(-90)
        self.direction = 1

    # Usunięcie obiektu alien z widoku
    def destroy_alien(self):
        self.goto(10000, 10000)

    # Przesuwanie obiektu alien
    def move_alien(self):
        new_x = self.xcor() + 5 * self.direction
        self.goto(new_x, self.ycor())

    # Przesuwanie obiektu alien
    def change_direction(self):
        self.direction *= - 1

# Usuwanie obiektu alien
    def kill_alien(self):
        self.goto(self.xcor(), 10000)

