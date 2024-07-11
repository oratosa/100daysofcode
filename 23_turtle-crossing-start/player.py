from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.get_start()

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=STARTING_POSITION[0], y=new_y)

    def get_start(self):
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
