import random
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLOR=["#FFE4E1","#FFB6C1","#FFD700","#FFFFE0","#FFEFD5","#BDB76B","#E6E6FA","#98FB98","#8FBC8B","#E0FFFF","#ADD8E6","#FFF0F5","#F5F5DC"]
MOVE= 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        new_segments = Turtle("square")
        new_segments.color(random.choice(COLOR))
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)



    def right(self):
      if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
    def left(self):
      if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)
    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)
    def down(self):
      if self.head.heading() != UP:
        self.head.setheading(DOWN)
