from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snack:
    def __init__(self):
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]

    def create_snack(self):
        for index in range(3):
            position = (10 * (-index), 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_segment.shape("square")
        new_segment.color("#00ABB3")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend(self):
        self.add_segment(self.segments[-1].position())


