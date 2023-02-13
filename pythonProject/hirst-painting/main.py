#import colorgram
#
#colors = colorgram.extract('image.jpg',100)
#
#dots_list = []
#def single_dot(dot):
#    r = dot.r
#    g = dot.g
#    b = dot.b
#    return (r, g, b)
#
#def all_dots(colors):
#    for colour in colors:
#        dot = single_dot(colour.rgb)
#        dots_list.append(dot)
#
#all_dots(colors)
#print(dots_list)

import turtle as t
import random

colors_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

tim = t.Turtle()
tim.shape("classic")
tim.speed("fastest")
tim.ht()
t.colormode(255)
tim.penup()
tim.setpos(-250, -250)

def random_colour():
    return random.choice(colors_list)

def paint():
    for _ in range(10):
        tim.dot(20, random_colour())
        if (_ < 9):
            tim.forward(50)
        else:
            y = tim.ycor()
            tim.setpos(-250, (y + 50))


for _ in range(10):
    paint()

screen = t.Screen()
screen.exitonclick()