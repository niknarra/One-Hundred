# Day 23 - July 3 '24
# Turtle Crossing

import time
from turtle import Screen
from player import Player
from carmanager import CarManager, MOVE_INCREMENT
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Turtle Crossing")
screen.tracer(0)

score = Score()
player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.up, "space")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.cars:
        if car.distance(player.player) < 20:
            game_is_on = False
            score.game_over()

    if player.player.ycor() > 280:
        player.reset_position()
        score.level += 1
        score.update_score()
        cars.car_speed += MOVE_INCREMENT

screen.exitonclick()
