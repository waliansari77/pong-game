from turtle import Turtle

class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()