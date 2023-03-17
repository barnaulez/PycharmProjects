from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.start_cars()

    def start_cars(self):
        self.add_car()

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x=random.randint(260, 280), y=random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + level*MOVE_INCREMENT)