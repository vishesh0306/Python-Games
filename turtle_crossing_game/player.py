from turtle import Turtle
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

t=Turtle()
t.hideturtle()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
            self.goto(STARTING_POSITION)

    def game_over(self):
        t.write("Game Over", align="center", font=("Courier", 30, "normal"))