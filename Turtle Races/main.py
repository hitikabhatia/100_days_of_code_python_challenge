from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500,400)
is_race_on = False
user_bet = screen.textinput(title= "Make your bet.", prompt= "Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [90, 60, 30, 0, -30, -60]
turtle_list = []

for turtle_index in range(6):
    each_turtle = Turtle(shape="turtle")
    each_turtle.color(colors[turtle_index])
    each_turtle.penup()
    each_turtle.goto(x=-230, y= y_positions[turtle_index])
    turtle_list.append(each_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for a_turtle in turtle_list:
        if a_turtle.xcor() > 230:
            is_race_on = False
            winning_color = a_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle won the race.")
            else:
                print(f"You lost. The {winning_color} turtle won the race.")
        rand_distance = random.randint(0, 10)
        a_turtle.forward(rand_distance)


screen.exitonclick()
