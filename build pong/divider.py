STARTING_POSITION = (0, 300)
HEADING_ANGLE = 270

from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0) #set to the fastest speed
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING_ANGLE)
        self.draw_divider()


    def draw_divider(self):
        for divide in range(0, 30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.penup()