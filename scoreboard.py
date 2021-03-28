from turtle import Turtle

WIDTH = 1200
HEIGHT = int(WIDTH * 0.56)  # HEIGHT = 56% of WIDTH = 672

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()
    
  def update_scoreboard(self):
    """
    Keeps the scoreboard updated. Alligns automatically using HEIGHT & WIDTH of the screen.
    """
    self.clear()
    self.goto(-(WIDTH//6), (HEIGHT//2-30))
    self.write(self.l_score, align = 'center', font = ('Courier', 20, 'normal'))
    self.goto((WIDTH//6), (HEIGHT//2-30))
    self.write(self.r_score, align = 'center', font = ('Courier', 20, 'normal'))
  
  def l_point(self):
    """
    Increases the left side score.
    """
    self.l_score += 1
    self.update_scoreboard()
  
  def r_point(self):
    """
    Increases the right side score.
    """
    self.r_score += 1
    self.update_scoreboard()