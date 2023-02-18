from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(x=-280, y=270)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.level += 1