from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        with open("data.txt") as file:
            self.high_score = int(file.read())
#        self.high_score = 0
        self.score = 0
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Scores: {self.score}. High Score: {self.high_score}", move=False, align='center', font=('Courier New', 10, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER!", move=False, align='center', font=('Arial', 16, 'bold'))