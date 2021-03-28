from turtle import Turtle

class Paddle(Turtle):
  
  def __init__(self, position):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(stretch_wid = 5, stretch_len = 1)
    self.penup()
    self.goto(position)
    
  def go_up(self):
    """
    Move the paddle up.
    """
    self.goto(self.xcor(), self.ycor() + 15)
  
  def go_down(self):
    """
    Move the paddle down.
    """
    self.goto(self.xcor(), self.ycor() - 15)