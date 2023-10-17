from turtle import Screen
from paddle import Paddle
from alien import Alien
# from ball import Ball
from laser import Laser
from enemy_laser import EnemyLaser
from box import Box
from scoreboard import Scoreboard
from colors import COLORS, COLORS_BOXES
import time
from random import choice, randint

# Parametry okna
screen = Screen()
screen.bgcolor(COLORS[0])
screen.setup(width=1200, height=800)
screen.title("Space Invaders")
screen.tracer(0)

# Generacja obiektów
paddle = Paddle((0, -360))
laser = Laser()
scoreboard = Scoreboard()

# Generacja obiektów enemy_laser
lasers = 20
enemy_lasers = []
for i in range(lasers):
    enemy_lasers.append(EnemyLaser())


# Generacja obiektów box
rows = 4
columns = 50
boxes = []
for i in range(rows):
    for j in range(columns):
        if j % 4:
            boxes.append(Box((-500 + j / columns * 1000, -200 - i * 20)))

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

    for enemy_laser in enemy_lasers:
        enemy_laser.move_enemy_laser()

    for alien in aliens:
        alien.move_alien()

    for alien in aliens:
        if (alien.xcor() <= - 500 or alien.xcor() >= 500) and alien.alien_shot == False:
            for any_alien in aliens:
                any_alien.change_direction()
                any_alien.move_towards_player()
            break

    # Detect collision with box
    for box in boxes:
        if laser.distance(box) <= 17 and box.ycor() - laser.ycor() <= 15:
            box.destroy_box()
            laser.delete_laser()
        for enemy_laser in enemy_lasers:
            if enemy_laser.distance(box) <= 17 and box.ycor() - enemy_laser.ycor() <= 15:
                box.destroy_box()
                enemy_laser.delete_laser_alien()
        for alien in aliens:
            if alien.distance(box) <= 20 and box.ycor() == alien.ycor():
                box.destroy_box()

    # Detect collision with top wall
    if laser.ycor() > 395:
        laser.delete_laser()

    # Detect collision with alien
    aliens_grouped = {}
    for alien in aliens:
        if laser.distance(alien) <= 17 and alien.ycor() - laser.ycor() <= 15:
            alien.kill_alien()
            laser.delete_laser()
            scoreboard.point()

        if alien.xcor() not in aliens_grouped:
            aliens_grouped[alien.xcor()] = []
        aliens_grouped[alien.xcor()].append(alien)

        if alien.ycor() <= -360:
            scoreboard.game_over()
            game_is_on = False

    bottom_alien = None
    chosen_laser = choice(enemy_lasers)
    if not chosen_laser.flying and randint(0, 5) == 1:
        aliens_grouped_key = choice(list(aliens_grouped.keys()))
        chosen_aliens_xcord = aliens_grouped[aliens_grouped_key]
        bottom_position = 300
        for alien in chosen_aliens_xcord:
            if alien.ycor() < bottom_position:
                bottom_position = alien.ycor()
                bottom_alien = alien
        try:
            chosen_laser.shoot_alien(bottom_alien.xcor(), bottom_alien.ycor())
        except AttributeError:
            pass

    # Detect collision of alien missile with bottom wall
    for enemy_laser in enemy_lasers:
        if enemy_laser.ycor() < - 395:
            enemy_laser.delete_laser_alien()

        if enemy_laser.distance(paddle) <= 17 and enemy_laser.ycor() - paddle.ycor() <= 15:
            scoreboard.game_over()
            game_is_on = False

        if enemy_laser.distance(laser) <= 11 and enemy_laser.ycor() - laser.ycor() <= 10:
            laser.delete_laser()
            enemy_laser.delete_laser_alien()

    if scoreboard.score == 45:
        scoreboard.game_over()






    # ball.move()


screen.exitonclick()
