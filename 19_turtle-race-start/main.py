from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet.",
    prompt="Which turtle (red/green/blue/black/yellow/purple) will win the race? Enter a color:",
)

colors = ["red", "green", "blue", "black", "yellow", "purple"]
turtles = []

for i in range(len(colors)):
    instance = Turtle(shape="turtle")
    instance.color(colors[i])
    instance.penup()
    instance.goto(x=-230, y=-100 + i * 40)
    turtles.append(instance)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:

        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
