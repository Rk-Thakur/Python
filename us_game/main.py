import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)




# Coordinates for the states on click
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)   
# turtle.mainloop() 

data = pandas.read_csv('50_states.csv')
all_states = (data.state).to_list()
gussed_states = []

while len(gussed_states) < 50:
    answer_state = screen.textinput(title = f'{len(gussed_states)}/50 States Correct',prompt ="What's another state?").title() 
    print(answer_state)

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in gussed_states]
        # missing_state = []
        # for state in all_states:
        #     if state not in gussed_states:
        #         missing_state.append(state)
            new_data = pandas.DataFrame(missing_state)  
            new_data.to_csv('states_to_learn.csv')
        break

    if answer_state  in all_states:
        print(answer_state)
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())













