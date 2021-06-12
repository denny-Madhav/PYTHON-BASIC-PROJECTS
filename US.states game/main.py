import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S states game")
img ="blank_states_img.gif"
screen.addshape(img)
turtle.shape((img))


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []
correct = 0
while len(guessed) <50:
    input_state = screen.textinput(title=f"{correct}/50 guessed correct.", prompt="what's another state name ").title()
    print(input_state)
    if input_state in all_states:
        correct +=1
        guessed.append(input_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == input_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


screen.exitonclick()


