from turtle import Turtle

Y_COR = 270
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, Y_COR)
        self.score = 0
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align= ALIGNMENT, font= FONT)