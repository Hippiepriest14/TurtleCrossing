from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-290,270)
        self.write(f"Level: {self.level_score}",font=FONT)
        self.level_score += 1

    def game_over(self):
        self.goto(-60,0)
        self.write("GAME OVER", font=FONT)
