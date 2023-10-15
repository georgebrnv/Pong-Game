from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), y=new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), y=new_y_cor)
