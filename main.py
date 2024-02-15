from turtle import Screen, Turtle
from paddle import Paddle
import time

NET_LENGTH = 10
NET_WIDTH = 5
NET_GAP = 20

screen = Screen()
net = Turtle()
right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)

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


create_net()

screen.listen()
screen.onkey(key='Down', fun=right_paddle.down)
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)
screen.onkey(key='w', fun=left_paddle.up)

is_game_on = True

while is_game_on:
    screen.update()
screen.exitonclick()
