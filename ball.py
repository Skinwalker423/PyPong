from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)

    def move(self):
        self.forward(.1)

    def bounce_walls(self):
        heading = self.heading()
        projection = 360 - heading
        self.setheading(projection)

    def bounce_paddle(self):
        print("collision detected on paddle")
        heading = self.heading()
        if heading < 180:
            self.setheading(180 - heading)
        else:
            projection = 360 - heading + 180
            self.setheading(projection)
