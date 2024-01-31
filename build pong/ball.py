from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slowest") #the speed value is '1'
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
    def move_ball(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_y(self):
        #reversing the direction of the ball along the y-axis
        self.y_move *= -1

    def bounce_x(self):
        #reversing the direction of the ball along the x-axis
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed *= 0.9