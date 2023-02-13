import turtle as t
import random
tim = t.Turtle()
tim.ht()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def paint_circle():
    tim.color(random_color())
    tim.circle(75, 360, 250)
    tim.left(4)

for _ in range(90):
    paint_circle()

screen = t.Screen()
screen.exitonclick()