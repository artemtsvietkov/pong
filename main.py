import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_started = False

def start_game():
    global game_started
    if not game_started:
        game_started = True
        ball.move_speed = 0.1
        screen.update()

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(start_game, "space") 

def on_close():
    global game_started
    game_started = False
    screen.bye()  

screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

while True:
    try:
        screen.update()  

        if not game_started:
            ball.goto(0, 0)
            continue

        ball.move()

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        if ball.xcor() > 380:
            scoreboard.left_score += 1
            scoreboard.update_score()
            ball.reset_position()
            game_started = False 

        if ball.xcor() < -380:
            scoreboard.right_score += 1
            scoreboard.update_score()
            ball.reset_position()
            game_started = False 

    except turtle.Terminator:
        break
