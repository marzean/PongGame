from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xcor_distance = 5
        self.ycor_distance = 5
        self.ball_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.xcor_distance
        new_y = self.ycor() + self.ycor_distance
        self.penup()
        self.goto(new_x, new_y)

    def ball_up(self):
        self.ycor_distance *= -1

    def ball_side(self):
        self.xcor_distance *= -1
        self.ball_speed *= 0.9

    def reset_right(self):
        self.goto(0, 0)
        self.ball_side()

    def reset_left(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.ball_side()






