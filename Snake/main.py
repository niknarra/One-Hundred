# Day 20 & 21 July 2 '24
# Classic Snake Game

from turtle import Screen
import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Nik's Snake Game")
screen.tracer(0)


game_continue = True

score = Score()
mySnake = Snake(3)
food = Food()

screen.listen()
screen.onkey(mySnake.up, "Up")
screen.onkey(mySnake.down, "Down")
screen.onkey(mySnake.left, "Left")
screen.onkey(mySnake.right, "Right")
screen.onkey(mySnake.reset_snake, "space")
screen.onkey(screen.bye, "Escape")
  
while game_continue:
  screen.update()
  time.sleep(0.1)

  mySnake.move()

  if mySnake.head.distance(food) < 15:
    score.update_score()
    food.refresh()
    mySnake.create_snake(1)

  if mySnake.head.xcor() > 290 or mySnake.head.xcor() < -290 or mySnake.head.ycor() > 290 or mySnake.head.ycor() < -290:
    game_continue = False
    score.reset()
    score.game_over()

  for segment in mySnake.snakeSegments[1:]:
    if mySnake.head.distance(segment) < 10:
      game_continue = False
      score.reset()
      score.game_over()
  

screen.exitonclick()