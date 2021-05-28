# Pong game
import turtle
import winsound
from os import path
from pydub import AudioSegment

# Sound file convert from MP3 to WAV
src = "no-god-no.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=900, height=700)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A 
paddle_a = turtle.Turtle() 
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, -200)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = -.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

# Functions
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
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 340:
                ball.sety(340)
                ball.dy *= -1

        if ball.ycor() < -340:
                ball.sety(-340)
                ball.dy *= -1

        if ball.xcor() > 440:
                ball.goto(0,0)
                ball.dx *= -1
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
                winsound.PlaySound("test.wav", winsound.SND_ASYNC)

        if ball.xcor() < -440:
                ball.goto(0,0)
                ball.dx *= -1
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
                winsound.PlaySound("test.wav", winsound.SND_ASYNC)

        # Paddle and ball collision
        if ball.xcor() > 370 and (ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(370)
            ball.dx *= - 1

        if ball.xcor() < -370 and (ball.xcor() > -400) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-370)
            ball.dx *= - 1
