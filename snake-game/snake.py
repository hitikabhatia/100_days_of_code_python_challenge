from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
angle_dictionary = {"RIGHT_ANGLE": 0,
                    "UP_ANGLE": 90,
                    "LEFT_ANGLE": 180,
                    "DOWN_ANGLE": 270,
                    }


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != angle_dictionary["DOWN_ANGLE"]:
            self.head.setheading(angle_dictionary["UP_ANGLE"])

    def down(self):
        if self.head.heading() != angle_dictionary["UP_ANGLE"]:
            self.head.setheading(angle_dictionary["DOWN_ANGLE"])

    def left(self):
        if self.head.heading() != angle_dictionary["RIGHT_ANGLE"]:
            self.head.setheading(angle_dictionary["LEFT_ANGLE"])

    def right(self):
        if self.head.heading() != angle_dictionary["LEFT_ANGLE"]:
            self.head.setheading(angle_dictionary["RIGHT_ANGLE"])
