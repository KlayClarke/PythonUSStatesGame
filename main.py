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

answer_state = screen.textinput(title='Guess The State', prompt='What\'s another state\'s name?').title()

data = pandas.read_csv('50_states.csv')
for state in data['state']:
    if answer_state == state:
        state_data = data[data.state == f'{state}']
        state_x_coordinate = int(state_data.x)
        state_y_coordinate = int(state_data.y)
        state_coordinates = (state_x_coordinate, state_y_coordinate)
        # pandas.
        state_name.goto(state_coordinates)
        state_name.write(arg=state, move=False, align='center', font=('Arial', 8, 'normal'))


turtle.mainloop()
