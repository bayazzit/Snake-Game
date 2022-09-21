from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)

STARTING_POSITIONS = [(0, 0), (-5, 0), (-10, 0), (-15, 0)]
MOVE_DISTANCE = 5
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shapesize(0.4)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        # The first segment is moving and the tail follows it #
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        # Turn right #
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def up(self):
        # Turn upwards #
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        # Turn left #
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        # Turn downwards #
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
