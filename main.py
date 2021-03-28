from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard,HEIGHT,WIDTH
import time

# SET THE SCREEN
screen = Screen()
screen.bgcolor('black')
screen.setup(height = HEIGHT, width = WIDTH)
screen.title('Pong')
screen.tracer(0)

# SET THE PADDLE, BALL, SCOREBOARD
r_paddle = Paddle((WIDTH//2 - 30,0))
l_paddle = Paddle((-(WIDTH//2 - 20),0))
ball = Ball()
scoreboard = Scoreboard()

# WAITING FOR THE KEYPRESS EVENT
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_on = True
ball_speed = 0.016 #Decrease to make the ball move faster.
while game_on:
  
  time.sleep(ball_speed)
  screen.update()
  ball.move()

  #Detecting Collision with the wall
  if (ball.ycor() > (HEIGHT//2 - 12)) or (ball.ycor() < -(HEIGHT//2 - 20)):
    ball.bounce_y()

  #Detecting Collision with the paddle
  if (ball.distance(r_paddle) < 50 and ball.xcor() > (WIDTH//2-50)) or (ball.distance(l_paddle) < 50 and ball.xcor() < -(WIDTH//2-40)):
    ball.bounce_x()
  
  #Detect if right paddle misses
  if ball.xcor() > (WIDTH//2-10):
    ball.reset_position()
    scoreboard.l_point()

  #Detect if left paddle misses
  if ball.xcor() < -(WIDTH//2-10):
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()