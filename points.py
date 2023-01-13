from turtle import Turtle


class PointBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.penup()
        self.hideturtle()
        self.left_points = 0
        self.right_points = 0
        self.update_points()

    def update_points(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"Player 1: {self.left_points}", align="center", font=("Courier", 20, "normal"))
        self.goto(150, 200)
        self.write(f"Player 2: {self.right_points}", align="center", font=("Courier", 20, "normal"))

    def left_count(self):
        self.left_points += 1
        self.update_points()

    def right_count(self):
        self.right_points += 1
        self.update_points()

