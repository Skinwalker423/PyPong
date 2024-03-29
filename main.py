from turtle import Screen, Turtle
import random
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

NET_LENGTH = 10
NET_WIDTH = 5
NET_GAP = 20

screen = Screen()
net = Turtle()
right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
ball = Ball()
ball.setheading(15)
scoreboard = Scoreboard()

screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
time.sleep(.1)


def create_net():
    net.penup()
    net.color("white")
    net.width(NET_WIDTH)
    net.speed(10)
    net.goto(0, -300)
    net.setheading(90)
    net.penup()
    while net.position()[1] < 300:
        net.pendown()
        net.forward(NET_LENGTH)
        net.penup()
        net.forward(NET_GAP)


screen.listen()
screen.onkey(key='Down', fun=right_paddle.down)
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)
screen.onkey(key='w', fun=left_paddle.up)

is_game_on = True
speed = .05
while is_game_on:
    screen.update()
    ball.move(speed)
    x_pos = ball.xcor()
    y_pos = ball.ycor()
    distance_left = ball.distance(left_paddle)
    distance_right = ball.distance(right_paddle)

    if x_pos > 380 or x_pos < -380:
        time.sleep(2)
        ball.goto(0, 0)
        speed = 0.025
        if x_pos > 300:
            scoreboard.increase_score('left')

            ball.setheading(random.randint(150, 210))

        else:
            scoreboard.increase_score('right')

            angle = random.randint(-30, 30) + 360
            ball.setheading(angle)

    if y_pos > 280 or y_pos < -280:
        ball.bounce_walls()
    if (distance_left < 45 and x_pos < -340) or (distance_right < 45 and x_pos > 340):
        ball.bounce_paddle()
        speed += .005

print("Game Over")
screen.exitonclick()
