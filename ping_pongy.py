import turtle
import winsound

# Setup
wn = turtle.Screen()
wn.title('Pongy 4')
wn.bgcolor('#0000FF')
wn.tracer(0)
wn.setup(width=800, height=700)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_len=1, outline=None, stretch_wid=5)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Spawn rendering speed?
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, outline=None, stretch_wid=5)
paddle_b.penup()
paddle_b.color('white')
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.shapesize(stretch_len=1, outline=10, stretch_wid=1)
ball_color = ball.color('white')
ball.penup()
ball.dx = 0.2
ball.dy = 0.2
ball.goto(0, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Player A:{}  Player B:{}'.format(score_a, score_b), align='center', font=('Courier', 24, 'italic'))

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


# Key bindings
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Game Loop
while True:
    wn.update()

    # Ball Movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking
    if ball.xcor() > 390:

        ball.goto(0, 0)
        ball.dx = 0.2
        ball.dx *= -1
        score_a += 1
        ball_color = ball.color('white')
        pen.clear()
        pen.write('Player A:{}  Player B:{}'.format(score_a, score_b), align='center', font=('Courier', 24, 'italic'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:

        ball.goto(0, 0)
        ball.dx = -0.2
        ball.dx *= -1
        score_b += 1
        ball_color = ball.color('white')
        pen.clear()
        pen.write('Player A:{}  Player B:{}'.format(score_a, score_b), align='center', font=('Courier', 24, 'italic'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    if ball.ycor() > 340:

        ball.sety(340)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -340:

        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Paddle Collision
    if (340 < ball.xcor() > 350) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):

        ball.setx(340)
        ball.dx *= -1.1
        ball_color = ball.color('#FF0000')
        winsound.PlaySound('paddle_bounce.wav', winsound.SND_ASYNC)  # winsound only executes wav btw

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):

        ball.setx(-340)
        ball.dx *= -1.1
        ball_color = ball.color('#00FF00')
        winsound.PlaySound('paddle_bounce.wav', winsound.SND_ASYNC)





