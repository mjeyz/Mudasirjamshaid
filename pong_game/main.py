from turtle import Screen
from pong_game.paddle import Paddle
from ball import Ball
import time
from pong_game.scoreboard import ScoreBoard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("My Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddles and ball initialization
r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()
scoreboard = ScoreBoard()

# Key bindings for paddle movement
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Right paddle up
screen.onkey(r_paddle.go_down, "Down")  # Right paddle down
screen.onkey(l_paddle.go_up, "w")  # Left paddle up
screen.onkey(l_paddle.go_down, "s")  # Left paddle down

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if the ball goes out of bounds (right side)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if the ball goes out of bounds (left side)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
