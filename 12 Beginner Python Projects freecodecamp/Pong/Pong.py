# Simple Pong Game
# by @TokyoEdTech via freecodecamp.org
# functional-style coding, not object-oriented

import turtle
import os

# Turtle module for simple games
wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600) # origin is in the center of the screen
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # default size 20 x 20 px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretch size by factor of 5 (make taller)
paddle_a.penup() # doens't draw a line
paddle_a.goto(-350, 0) # start on left side of screen

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # default size 20 x 20 px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretch size by factor of 5 (make taller)
paddle_b.penup() # doens't draw a line
paddle_b.goto(350, 0) # start on right side of screen

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # default size 20 x 20 px
ball.color("white")
ball.penup() # doens't draw a line
ball.goto(0, 0)

# Ball movement
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function

def paddle_a_up():
    y = paddle_a.ycor() # current y coordinate, from turtle module
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # current y coordinate, from turtle module
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # current y coordinate, from turtle module
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # current y coordinate, from turtle module
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # listen for keyboard input

wn.onkeypress(paddle_a_up, "w") # when user presses "w", call function paddle_a_up
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay bounce.wav&") # prevent play delays when sound plays with &
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    # Paddle Hit
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 45):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 45):
        ball.setx(-340)
        ball.dx *= -1
