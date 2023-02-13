import turtle as t
import random

tim = t.Turtle()
tim.shape("classic")
tim.width(6)
tim.ht()
tim.speed("fastest")
t.colormode(255)
moves = 1000
########### Challenge 4 - Random Walk ########
##colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
##           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]
turns = ["right", "left"]
routes = ["fw", "bk"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def moving():
    tim.color(random_color())
    t = random.choice(turns)
    if t == "right":
        tim.right(random.choice((angles)))
    else:
        tim.left(random.choice(angles))
    r = random.choice(routes)
    if r == "fw":
        tim.forward(10)
    else:
        tim.bk(10)

for _ in range(moves):
    moving()

screen = t.Screen()
screen.exitonclick()