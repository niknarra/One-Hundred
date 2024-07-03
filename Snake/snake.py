import turtle
import time

initialPos = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self, n):
    self.snakeSegments = []
    self.create_snake(n)
    self.head = self.snakeSegments[0]

  def create_snake(self, n):
    for _ in range(n):
      s = turtle.Turtle(shape='square')
      s.penup()
      s.speed(1)
      s.color('white')
      s.goto(initialPos[_])
      self.snakeSegments.append(s)
  
  def move(self):
    for seg in range(len(self.snakeSegments) - 1, 0, -1):
      newX = self.snakeSegments[seg - 1].xcor()
      newY = self.snakeSegments[seg - 1].ycor()
      self.snakeSegments[seg].goto(newX, newY)
    self.head.forward(20)
    
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  
  def reset_snake(self):
    for seg in self.snakeSegments:
      seg.goto(1000, 1000)
    self.snakeSegments.clear()
    self.create_snake(3)
    self.head = self.snakeSegments[0]