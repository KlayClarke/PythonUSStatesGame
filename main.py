import csv
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

correct_answers = []
missed_answers = []
score = 0

game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 correct',
                                    prompt='What\'s another state\'s name?').title().strip()
    if answer_state == 'Exit':
        for state in data['state']:
            if state not in correct_answers:
                missed_answers.append([state])
        with open('missed_answers.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(missed_answers)
        print(missed_answers)
        break
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
            elif score == 50:
                screen.clear()
                state_name.write(arg='You Guessed All States', move=False, align='center', font=('Arial', 50, 'normal'))
                state_name.goto(0, 0)
                game_is_on = False

    turtle.mainloop()
