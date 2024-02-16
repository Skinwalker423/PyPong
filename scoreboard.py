from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = {
            "left": 0,
            "right": 0
        }
        self.create_board()

    def increase_score(self, player):
        """pass in the argument 'left' to increase left player score by 1 or pass in 'right' to increase right player
        score"""
        self.scores[player] += 1
        self.clear()
        self.write_scores()

    def write_scores(self):
        self.write(arg=f"{self.scores['left']}      -      {self.scores['right']}", align="center", font=("Arial", 40, "normal"))

    def create_board(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 230)
        self.write_scores()
