from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from points import PointBoard
import time

# setting the screen details

screen = Screen()
screen.bgcolor("yellow")
screen.setup(width=800, height=600)
screen.title("Welcome to Pong game")
screen.tracer(0)

# creating the player1 and player2 paddle

paddle_right = Paddle(360, 0)
paddle_left = Paddle(-360, 0)
ball = Ball()

# The keys to move the paddles with related methods

screen.listen()
screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_right.paddle_down, "Down")
screen.onkey(paddle_left.paddle_down, "s")
player_points = PointBoard()

# game will continue while game is on

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_up()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 330 or ball.distance(paddle_left) < 50 and ball.xcor() > -330:
        ball.ball_side()

    if ball.xcor() > 380:
        ball.reset_right()
        player_points.left_count()
    if ball.xcor() < -380:
        ball.reset_left()
        player_points.right_count()

screen.exitonclick()
