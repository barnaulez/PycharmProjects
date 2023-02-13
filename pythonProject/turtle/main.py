from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("classic")
t.width(5)
t.ht()

colours = ["medium blue", "peru", "turquoise", "light sea green",
           "cadet blue", "dark cyan", "teal", "dark slate gray"]

def draw_shape(borders):
    t.color(random.choice(colours))
    for _ in range(borders):
        t.right(360/borders)
        t.forward(100)

for borders_number in range(3, 11):
    draw_shape(borders_number)

screen = Screen()
screen.exitonclick()
