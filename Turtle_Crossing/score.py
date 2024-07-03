from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Score:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.score_turtle = Turtle()
        self.score_turtle.color('white')
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(-280, 260)
        self.update_score()
        
    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.score_turtle.goto(0, 0)
        self.score_turtle.write("GAME OVER", align="center", font=FONT)
