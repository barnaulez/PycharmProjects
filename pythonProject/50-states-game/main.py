import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
screen.title("50 States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        states_dict = {
            "state": missing_states
        }
        df = pandas.DataFrame(states_dict)
        df.to_csv("learn.csv")
        break
    if answer_state in all_states:
        correct_answers.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.ht()
        state_name.goto(x_cor, y_cor)
        state_name.write(answer_state, align='center', font=('Arial', 8, 'normal'))


screen.exitonclick()

