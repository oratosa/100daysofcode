import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.go_up, key="Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect when turtle player collides with a car
    # and stop the game if it happens.
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Detect when the turtle player has reached the top edge of the screen.
    if player.ycor() == FINISH_LINE_Y:
        scoreboard.level_up()
        scoreboard.update_score()
        car_manager.speed_up()
        player.get_start()


screen.exitonclick()
