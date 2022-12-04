from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.setposition(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.clear()
        self.setposition(STARTING_POSITION)