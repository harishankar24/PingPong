from turtle import Turtle

class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color('red')
    self.shape('circle')
    self.penup()
    self.goto(0,0)
    self.x_move = 4
    self.y_move = 4
    
  def move(self):
    """
    Makes the ball move diagonally.
    """
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    """
    Redirects the ball when it collides with horizontal axis. (Up wall and Down wall)
    """
    self.y_move *= -1
    
  def bounce_x(self):
    """
    Used to set the direction of the ball when it misses either of the paddle.
    """
    self.x_move *= -1
    
  def reset_position(self):
    """
    Brings the ball to origin/center of the screen.
    """
    self.goto(0,0)
    self.bounce_x()