import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


def get_click_coordinates(x, y):
    print(x, y)


turtle.onscreenclick(get_click_coordinates)

turtle.mainloop()
