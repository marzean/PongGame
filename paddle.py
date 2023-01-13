from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xc, yc):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("cyan")
        self.penup()
        self.goto(xc, yc)
        self.paddle_up()

    def paddle_up(self):
        new_pos = self.ycor() + 20
        self.goto(self.xcor(), new_pos)

    def paddle_down(self):
        new_pos = self.ycor() - 20
        self.goto(self.xcor(), new_pos)








