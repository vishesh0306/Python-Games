import turtle
import pandas

screen = turtle.Screen()
screen.title("India Map")
screen.bgpic("map10.gif")
screen.setup(730, 730)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("states.csv")
state_list = data["states"].to_list()
guessed_states = []

total = screen.textinput(title="Knowledge test", prompt="How many states are there in India?")

if total == '28':

    while len(guessed_states) < 28:
        l=len(guessed_states)
        answer_state = screen.textinput(title=f"{l}/28 states guessed correct", prompt="Guess!!")
        guess = answer_state.title()

        if guess == 'Exit':
            break

        if guess not in guessed_states and guess in state_list:
            guessed_states.append(guess)

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.states == guess]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(guess)

else:
    print("You are not eligible to play")

print(f"You scored {len(guessed_states)}/28")
if len(guessed_states) == 28:
    print("hurrey!! You guessed all the states name :)")
# screen.exitonclick()



from turtle import Turtle,Screen
screen = Screen()
screen.title("LOGO")
screen.bgcolor("black")

#
# t = Turtle()
# t.color("purple")
# t.begin_fill()
# t.fillcolor("purple")
# t.circle(100)
# t.end_fill()
# t.color("yellow")
# t.goto(50,120)
# screen.exitonclick()
