from turtle import Turtle

PADDLE_LENGTH = 1
PADDLE_HEIGHT = 5

DISTANCE_TRAVEL = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.resizemode()
        self.shape("square")
        self.turtlesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        print("moving up")
        pos = self.position()
        pos_x = pos[0]
        pos_y = pos[1] + DISTANCE_TRAVEL
        self.goto(x=pos_x, y=pos_y)

    def down(self):
        print("moving down")
        pos = self.position()
        pos_x = pos[0]
        pos_y = pos[1] - DISTANCE_TRAVEL
        self.goto(x=pos_x, y=pos_y)
