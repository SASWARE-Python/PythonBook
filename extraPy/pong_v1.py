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


# Keyboard binding
root.listen()
root.onkeypress(paddle_a_up, "w")
root.onkeypress(paddle_a_down, "s")
root.onkeypress(paddle_b_up, "Up")
root.onkeypress(paddle_b_down, "Down")

# Main game loop
bounce_sound = True
while True:
    root.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ((286 < ball.ycor() < 287) or (-286 > ball.ycor() > -287)) and bounce_sound:
        os.system('aplay bounce_side_wall_01.wav&')
        bounce_sound = False

    if (ball.xcor() > 386 or ball.xcor() < -386) and bounce_sound:
        os.system('aplay bounce-02.wav&')
        bounce_sound = False

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound = True

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        bounce_sound = True

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound = True

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        bounce_sound = True

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
