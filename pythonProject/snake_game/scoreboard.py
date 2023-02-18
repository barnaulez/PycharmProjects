from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(x=0, y=280)
        self.write(f"Scores: {self.score}", move=False, align='center', font=('Courier New', 10, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align='center', font=('Arial', 16, 'bold'))