from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x=position[0], y=position[1])
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
