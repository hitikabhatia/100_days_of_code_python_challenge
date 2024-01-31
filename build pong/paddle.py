from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(position)

    def move_paddle_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def move_paddle_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)