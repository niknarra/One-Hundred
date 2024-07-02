from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('red')
    self.penup()
    self.speed('fastest')
    self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    randomX = random.randint(-280, 280)
    randomY = random.randint(-280, 280)
    self.goto(randomX, randomY)

  def refresh(self):
    randomX = random.randint(-280, 280)
    randomY = random.randint(-280, 280)
    self.goto(randomX, randomY)