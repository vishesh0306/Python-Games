
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_new_segment(position)

    def add_new_segment(self,position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_new_segment(self.segments[-1].position())



    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


