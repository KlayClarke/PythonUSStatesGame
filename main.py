import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
correct_answers = []

score = 0

user_exit = False

while user_exit is False and score < 50:
    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 correct',
                                    prompt='What\'s another state\'s name?').title().strip()
    if answer_state == 'Exit':
        missed_answers = [state for state in all_states if state not in correct_answers]
        missing_states_data = pandas.DataFrame(missed_answers)
        missing_states_data.to_csv('missed_answers.csv')
        user_exit = True

    else:
        for state in data['state']:
            score = len(correct_answers)
            if answer_state == state:
                if state in correct_answers:
                    pass
                else:
                    correct_answers.append(state)
                    state_data = data[data.state == f'{state}']
                    state_x_coordinate = int(state_data.x)
                    state_y_coordinate = int(state_data.y)
                    state_coordinates = (state_x_coordinate, state_y_coordinate)
                    state_name.goto(state_coordinates)
                    state_name.write(arg=state, move=False, align='center', font=('Arial', 8, 'normal'))

screen.clear()
state_name.goto(0, 0)
state_name.write(arg=f'You Guessed {len(correct_answers)} States Correctly', move=False, align='center',
                 font=('Arial', 30, 'normal'))

turtle.mainloop()
