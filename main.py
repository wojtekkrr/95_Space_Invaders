from turtle import Screen
from paddle import Paddle
from alien import Alien
# from ball import Ball
from laser import Laser
from box import Box
from colors import COLORS
# from scoreboard import Scoreboard
import time

# Parametry okna
screen = Screen()
screen.bgcolor(COLORS[5])
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

# Generacja obiektów
paddle = Paddle((0, -360))
laser = Laser()

# Generacja obiektów box
rows = 6
columns = 50
boxes = []
for i in range(rows):
    for j in range(columns):
        if j % 4:
            boxes.append(Box((-500 + j / columns * 1000, -100 - i * 20)))

# Generacja obiektów alien
rows = 6
columns = 55
aliens = []
for i in range(rows):
    if i % 2:
        for j in range(30):
            if j % 2:
                aliens.append(Alien((-480 + j / columns * 1000, 300 - i * 20)))

# Możliwość przesuwania odbijaka poprzez przytrzymanie strzałek
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkey(lambda: laser.shoot(paddle.xcor()), "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.025)
    laser.move()
    for alien in aliens:
        alien.move_alien()

    for alien in aliens:
        if alien.xcor() <= - 500 or alien.xcor() >= 500:
            for any_alien in aliens:
                any_alien.change_direction()
            break

    # Detect collision with box
    for box in boxes:
        if laser.distance(box) <= 17 and box.ycor() - laser.ycor() <= 15:
            box.destroy_box()
            laser.delete_laser()

    # Detect collision with top wall
    if laser.ycor() > 395:
        laser.delete_laser()

    # Detect collision with alien
    for alien in aliens:
        if laser.distance(alien) <= 17 and alien.ycor() - laser.ycor() <= 15:
            alien.kill_alien()
            laser.delete_laser()





    # ball.move()


screen.exitonclick()
