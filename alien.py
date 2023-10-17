from turtle import Turtle
from colors import COLORS


class Alien(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color(COLORS[3])
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(-90)
        self.direction = 1
        self.towards_player_dist = 20
        self.alien_shot = False

    # Przesuwanie obiektu alien
    def move_alien(self):
        new_x = self.xcor() + 5 * self.direction
        self.goto(new_x, self.ycor())

    # Zmiana kierunku ruchu obiektów alien
    def change_direction(self):
        self.direction *= - 1

    # Usuwanie obiektu alien
    def kill_alien(self):
        self.goto(self.xcor(), 10000)
        self.alien_shot = True

    # Przybliż się
    def move_towards_player(self):
        new_y = self.ycor() - self.towards_player_dist
        self.goto(self.xcor(), new_y)
