# pong game
import time
import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Jason")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player 1: {scoreA}  |  Player 2: {scoreB}", align="center", font=("Courier", 24, "normal"))

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 0)


# Function
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keybinds
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")
win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Down")
# main game loop

while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player 1: {scoreA}  |  Player 2: {scoreB}", align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player 1: {scoreA}  |  Player 2: {scoreB}", align="center", font=("Courier", 24, "normal"))
    # paddle and ball collision
    if (340 < ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 > ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (-340 > ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 > ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if scoreA > 3:
        ball.clear()
        paddleB.clear()
        paddleA.clear()
        pen.clear()
        pen1.write("Player 1 WINS!", align="center", font=("Courier", 45, "bold"))
        winsound.PlaySound("victory.wav", winsound.SND_ASYNC)
        time.sleep(10)
        exit()

    if scoreB > 3:
        ball.clear()
        paddleB.clear()
        paddleA.clear()
        pen.clear()
        pen1.write('Player 2 WINS!', align="center", font=("Courier", 45, "bold"))
        winsound.PlaySound("victory.wav", winsound.SND_ASYNC)
        time.sleep(10)
        exit()
