from turtle import Turtle
from colors import COLORS


class EnemyLaser(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[3])
        self.shape("square")
        self.shapesize(stretch_wid=.2, stretch_len=.5)
        self.penup()
        self.goto(10000, -340)
        self.setheading(90)
        self.speed = 10
        self.flying = False

    # Przesunięie lasera
    def move_enemy_laser(self):
        new_y = self.ycor() - self.speed
        self.goto(self.xcor(), new_y)

    # Przeniesienie lasera w kierunku obiektu alien
    def shoot_alien(self, x_coordinate, y_coordinate):
        self.goto(x_coordinate, y_coordinate)
        self.flying = True

    # Usunięcie pocisku
    def delete_laser_alien(self):
        self.goto(10000, -340)
        self.flying = False
