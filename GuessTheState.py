# Day 25 - July 4 '24
# Guess The State Game

from turtle import Turtle, Screen
import pandas as pd

def mark_state(state):
  if state in stateNames:
    state_data = stateData[stateData.state == state]
    x = int(state_data.x)
    y = int(state_data.y)
    new_turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.write(state)

def update_score():
  global score
  score += 1

def get_highest_score():
  with open('highscore.txt',mode='r') as scoredoc:
    highScore = scoredoc.readline()
    return highScore

def update_high_score(score):
  with open('highscore.txt',mode='w') as scoredoc:
    scoredoc.write(score)

def missed_states():
  for state in stateNames:
    if state not in guessedStates:
      missedStates.append(state)
  print(f"The Remaining States: {', '.join(missedStates)}")
  print(f"You missed {len(missedStates)} out of 50 states.")
  output = pd.DataFrame(missedStates,columns=['State'])
  output.to_csv('output.csv')

highScore = get_highest_score()
guessedStates = []
missedStates = []

score = 0
myScreen = Screen()
myScreen.setup(width=725, height=491)
myScreen.bgpic(picname="blank_states_img.gif")

stateData = pd.read_csv('50_states.csv')

stateNames = stateData['state'].to_list()

totalStates = len(stateData["state"])

while score < totalStates:
  userGuess = myScreen.textinput(title=f"Score:{score} HighScore: {highScore}", prompt="What's your guess?").title()
  if userGuess == 'Exit':
    missed_states()
    break
  if userGuess in stateNames:
    guessedStates.append(userGuess)
    mark_state(userGuess)
    update_score()
    #score +=1
  if score > int(highScore):
    highScore = score
    update_high_score(str(score))

myScreen.exitonclick()
