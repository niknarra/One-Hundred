import turtle

def get_highscore():
  with open('high_score.txt', 'r') as f:
    highScore = int(f.read())
  return highScore

highScore = get_highscore()

class Score():
  def __init__(self):
    #self.get_highscore()
    self.highscore = highScore
    self.score = 0
    self.score_display = turtle.Turtle()
    self.score_display.penup()
    self.score_display.hideturtle()
    self.score_display.color('white')
    self.score_display.goto(0, 260)
    self.update_display()

  def update_display(self):
    self.score_display.clear()
    self.score_display.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 20, "normal"))
    
  def update_score(self):
    self.score += 1
    self.update_display()

  def game_over(self):
    self.score_display.goto(0, 0)
    self.score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))
    
  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open('high_score.txt',mode='w') as highScoreStore:
        highScoreStore.write(str(self.highscore))
    self.score = 0
    self.update_display()