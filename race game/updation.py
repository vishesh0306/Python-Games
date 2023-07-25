import random
from turtle import Turtle,Screen

def again():
    screen = Screen()

    screen.reset()
    a = screen.textinput(title="PLAY AGAIN?",prompt='DO YOU WANT TO PLAY AGAIN? {"yes" or "no"} : ')
    return a

def boundary():
    screen = Screen()
    screen.bgcolor("black")
    t=Turtle()
    t.shape("turtle")
    t.pencolor("red")
    t.penup()
    t.goto(x=250,y=200)
    t.pendown()
    t.right(90)
    t.forward(400)
    t.hideturtle()

boundary()

def game():
    screen=Screen()
    screen.bgcolor("black")
    screen.title("Let's Start the Race")
    screen.setup(width=600,height=450)

    user_bet=screen.textinput(title="MAKE A BET", prompt='Which turtle will win the race?\n ["red","green","yellow","orange","purple","blue","pink"] \nEnter a colour : ')

    colour=["red","green","yellow","orange","purple","blue","pink"]

    position=[-150,-100,-50,0,50,100,150]
    all_turtle=[]
    is_race_on=False

    for i in range(7):
        new_turtle=Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colour[i])
        new_turtle.penup()
        new_turtle.goto(x=-245, y=position[i])

        all_turtle.append(new_turtle)

    if user_bet in colour:
        is_race_on=True

    while is_race_on:

        for i in all_turtle:
            if(i.xcor()>230):
                is_race_on=False
                winner=i.pencolor()

                if(winner==user_bet):
                    print("YOU WIN THE RACE,",winner,"turtle won" )
                else:
                    print("YOU LOOSE THE RACE,",winner,"turtle won" )

            movement=random.randint(0,10)
            i.forward(movement)

    t=again()
    if(t=='yes'):
        game()

game()