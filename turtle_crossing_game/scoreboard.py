FONT = ("Courier", 20, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280,y=260)
        self.point=1
        self.write(f"Level : {self.point}",align="left",font=FONT)

    def update_score(self):
        self.clear()
        self.point+=1
        self.write(f"Level : {self.point}", align="left", font=FONT)