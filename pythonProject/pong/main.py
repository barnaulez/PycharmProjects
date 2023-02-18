from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time, random

heading_angle = random.randint(0,45)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
ball_compare = (ball.xcor(), ball.ycor())
screen.update()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

inc = 0
game_is_on = True

while game_is_on:

    time.sleep(0.05)
    screen.update()
    ball.move(heading_angle)

    if ball.ycor() > 280 or ball.ycor() < -280:
        heading_angle = 180 - ball.bounce((ball_compare))
        ball_compare = (ball.xcor(), ball.ycor())
        print(f"bounce {heading_angle}")
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        heading_angle = 360 - ball.bounce((ball_compare))
        ball_compare = (ball.xcor(), ball.ycor())
        print(f"bounce {heading_angle}")
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        heading_angle = 360 - ball.bounce((ball_compare))
        ball_compare = (ball.xcor(), ball.ycor())
        print(f"bounce {heading_angle}")
    elif ball.xcor() > 380:
        inc = 90
        heading_angle = random.randint(0, 89) + inc
        ball.goto(0,0)
        scoreboard.refresh_left()
    elif ball.xcor() < -380:
        inc = 0
        heading_angle = random.randint(0, 89) + inc
        ball.goto(0, 0)
        scoreboard.refresh_right()



screen.exitonclick()

