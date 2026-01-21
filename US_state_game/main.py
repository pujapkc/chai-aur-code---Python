import turtle
import pandas as pd

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./US_state_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data
data = pd.read_csv("./US_state_game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)

# Save missing states
missing_states = [state for state in all_states if state not in guessed_states]
pd.DataFrame(missing_states, columns=["state"]).to_csv("./US_state_game/states_to_learn.csv")

screen.mainloop()
