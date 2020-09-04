# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Comments
# - plain no objects

# Dependencies
# - turtle <- tkinter

import turtle
import os

root = turtle.Screen()
root.title("Pong by Arnaldo Sandoval")
root.bgcolor("black")
root.setup(width=800, height=600)
root.tracer(0)

# Score
score_a = 0
score_b = 0
do_exit = False

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.02
ball.dy = 0.02

# Scope pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def exit_loop():
    global do_exit
    do_exit = True


# Keyboard binding
root.listen()
root.onkeypress(paddle_a_up, "w")
root.onkeypress(paddle_a_down, "s")
root.onkeypress(paddle_b_up, "Up")
root.onkeypress(paddle_b_down, "Down")
root.onkeypress(exit_loop, "x")

# Main game loop
bounce_sound = True
bounce_side = True
bounce_wall = True
bounce_paddle = True

while True:
    root.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bouncing sound
    if ((286 - ball.dy < ball.ycor() <= 286 + ball.dy) or (-279 - ball.dy >= ball.ycor() > -279 + ball.dy)) and bounce_side:
        os.system('aplay bounce_side_wall_01.wav 2>/dev/null &')
        bounce_side = False

    if (370 - ball.dx < ball.xcor() <= 370 + ball.dx) or (-386 + ball.dx < ball.xcor() <= -386 - ball.dx) and bounce_wall:
        os.system('aplay bounce-02.wav 2>/dev/null &')
        bounce_wall = False

    if bounce_paddle and (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        os.system('aplay bounce_paddle_01.wav 2>/dev/null &')
        bounce_paddle = False

    if bounce_paddle and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        os.system('aplay bounce_paddle_01.wav 2>/dev/null &')
        bounce_paddle = False

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        bounce_side = True
        bounce_wall = True

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -394:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        bounce_side = True
        bounce_wall = True

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        bounce_side = True
        bounce_wall = True
        bounce_paddle = True

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        bounce_side = True
        bounce_wall = True
        bounce_paddle = True

    if do_exit:
        break
