from turtle import Screen
from paddle import Paddle
from ball import Ball
from divider import Divider
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 800, height=  600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

pong_ball = Ball()
divider = Divider()
scoreboard = Scoreboard()


screen.onkey(fun= right_paddle.move_paddle_up, key= "Up")
screen.onkey(fun= right_paddle.move_paddle_down, key= "Down")
screen.onkey(fun= left_paddle.move_paddle_up, key= "w")
screen.onkey(fun= left_paddle.move_paddle_down, key= "s")
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move_ball()

    #Detecting collision with up and down wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    #Detecting collision with the paddles
    if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()
        pong_ball.increase_speed()

    #detecting when right paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_ball()
        scoreboard.l_score_point()

    #detecting when the left paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_ball()
        scoreboard.r_score_point()

screen.exitonclick()