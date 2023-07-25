from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        file = open("score_history.txt", "r")
        self.high_score = int(file.read())

        file.close()

        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", move=False, align="center", font=("arial", 20, "normal"))

    def update_score_board(self):
        self.write(f"Score : {self.score}   High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score += 1
            with open("score_history.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.update_score_board()




