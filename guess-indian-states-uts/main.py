import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Guess the Indian States and Union Territories")
image = "india-map.gif"
screen.addshape(image)
turtle.shape(image)
map_turtle = turtle.Turtle()
map_turtle.hideturtle()
map_turtle.penup()

states_df = pd.read_csv("states_and_uts.csv")
state_list = states_df["state"].tolist()

guessed_states = []
states_left = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States and UTs Correct", prompt="What's the another state name?").title()
    if answer_state == "Exit":
        for each_state in state_list:
            if each_state not in guessed_states:
                states_left.append(each_state)
        pd.DataFrame(states_left).to_csv("missed_states.csv")
        break
    if answer_state in state_list and answer_state not in guessed_states:
        state_record = states_df[states_df.state == answer_state]
        map_turtle.goto(x= state_record.iloc[0][1], y= state_record.iloc[0][2])
        map_turtle.write(arg= answer_state,align= "center",font= ("Arial",8,"normal"))
        guessed_states.append(answer_state)