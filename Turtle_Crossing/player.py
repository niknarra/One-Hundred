STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player:
    def __init__(self):
        self.player = Turtle("turtle")
        self.player.color("blue")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def up(self):
        self.player.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.player.goto(STARTING_POSITION)
