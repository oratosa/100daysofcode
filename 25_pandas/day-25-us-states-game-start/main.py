import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US states game")
image = "/Users/asotaro/codes/100daysofcode/25_pandas/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_df = pd.read_csv(
    "/Users/asotaro/codes/100daysofcode/25_pandas/day-25-us-states-game-start/50_states.csv"
)
all_states = states_df["state"].to_list()

answered_states = []
while len(answered_states) < 50:
    guessed_state = screen.textinput(
        title=f"{len(answered_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if guessed_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in answered_states:
                missing_states.append(state)

        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv(
            "/Users/asotaro/codes/100daysofcode/25_pandas/day-25-us-states-game-start/missed_states.csv"
        )

        break

    if guessed_state in all_states:
        state_data = states_df[states_df["state"] == guessed_state]
        x = state_data["x"].item()
        y = state_data["y"].item()
        state = state_data["state"].item()

        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto((x, y))
        state_name.write(state)

        answered_states.append(state)
