from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(self.ball_speed)
        self.goto(0,0)

    def move(self, direction):
        self.setheading(direction)
        self.forward(10)

    def bounce(self, coordinates):
        if self.ball_speed == 10:
            self.ball_speed = 0
        elif self.ball_speed >= 1 and self.ball_speed < 10:
            self.ball_speed += 1
        print(self.ball_speed)
        return self.towards(coordinates)
