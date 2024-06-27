from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collisition with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.y_bounce()

    # Detect collisition with paddles.
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.x_bounce()

    # Detect r_paddle missed balls.
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()
        ball.x_bounce()

    # Detect l_paddle missed balls.
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()
        ball.x_bounce()

    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        game_is_on = False
        winner = "Left paddle" if scoreboard.l_score == 5 else "Right paddle"
        screen.title(f"The Winner is {winner}")

screen.exitonclick()
