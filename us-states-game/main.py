import turtle,pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/us-states-game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", 
                                    prompt="What's another state's name? ")
    if answer_state == 'exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/us-states-game/states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state ==  answer_state]
        t.goto(int(state_data.x), int(state_data.y)) # type: ignore
        t.write(state_data.state.item())

