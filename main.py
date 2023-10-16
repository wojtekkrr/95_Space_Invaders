from turtle import Screen
# from paddle import Paddle
# from ball import Ball
# from box import Box
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

# Możliwość przesuwania odbijaka poprzez przytrzymanie strzałek
screen.listen()
# screen.onkeypress(paddle.go_left, "Left")
# screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.025)
    # ball.move()


screen.exitonclick()