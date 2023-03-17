import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carManager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
loop = 0
level = 0
while game_is_on:
    if loop % 6 == 0:
        carManager.add_car()
    time.sleep(0.1)
    screen.update()
    carManager.move(level)
    for car in carManager.cars:
        if player.distance(car) < 20 and (player.xcor() <= (car.xcor() + 20) or player.xcor() >= (car.xcor() - 20)):
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.refresh()
        scoreboard.refresh()
        level +=1
    loop += 1
screen.exitonclick()