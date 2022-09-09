import turtle

# Создаём окно

win = turtle.Screen()
win.title("Просто пинг понг :D")
win.bgcolor("black")
win.setup(width=1200, height=600)
win.tracer(0)

# Создаём ракетки

racket_left = turtle.Turtle()
racket_left.speed(0)
racket_left.shape('square')
racket_left.color('purple')
racket_left.shapesize(stretch_len=1, stretch_wid=5)
racket_left.penup()  # При движении не удлинять объект
racket_left.goto(-570, 0)

racket_right = turtle.Turtle()
racket_right.speed(0)
racket_right.shape('square')
racket_right.color('yellow')
racket_right.shapesize(stretch_len=1, stretch_wid=5)
racket_right.penup()  # При движении не удлинять объект
racket_right.goto(560, 0)

# Создаём мяч

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()  # При движении не удлинять объект
ball.goto(0, 0)
ball.dx = ball.dy = 1

# Подсчёт очков
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"{score_a} {score_b}", align="center", font=("Verdana", 22, "normal"))



# Создаём раздилительную полосу

stripe = turtle.Turtle()
stripe.speed(0)
stripe.shape('square')
stripe.color('white')
stripe.shapesize(stretch_len=0.01, stretch_wid=600)
stripe.goto(0, 0)


# Функции

def racket_left_up():
    y = racket_left.ycor()
    y += 20
    racket_left.sety(y)


def racket_left_down():
    y = racket_left.ycor()
    y -= 20
    racket_left.sety(y)


def racket_right_up():
    y = racket_right.ycor()
    y += 20
    racket_right.sety(y)


def racket_right_down():
    y = racket_right.ycor()
    y -= 20
    racket_right.sety(y)


# Работа с клавиатурой

win.listen()
win.onkeypress(racket_left_up, "w")
win.onkeypress(racket_left_down, "s")

win.onkeypress(racket_right_up, "Up")
win.onkeypress(racket_right_down, "Down")

while True:
    win.update()

    # Движени мячика
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 600:
        ball.goto(0, 0)
        ball.dx *= -1

        score_a += 1
        pen.clear()

        pen.write(f"{score_a} {score_b}", align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() < -600:
        ball.goto(0, 0)
        ball.dx *= -1

        score_b += 1
        pen.clear()

        pen.write(f"{score_a} {score_b}", align="center", font=("Verdana", 22, "normal"))

    if (ball.xcor() > 545) and (ball.ycor() < racket_right.ycor() + 50) and (ball.ycor() > racket_right.ycor() - 50):
        ball.dx *= -1

    if (ball.xcor() < -545) and (ball.ycor() < racket_left.ycor() + 50) and (ball.ycor() > racket_left.ycor() - 50):
        ball.dx *= -1

    if (ball.xcor() > racket_right.xcor() + 5) and (ball.xcor() < racket_right.xcor() - 5) and (ball.ycor() < racket_right.ycor() + 50) and (ball.ycor() >= racket_right.ycor() - 50):
        ball.dy = -ball.dy

    if (ball.xcor() < racket_left.xcor() + 5) and (ball.xcor() < racket_left.xcor() - 5) and (ball.ycor() < racket_left.ycor() + 50) and (ball.ycor() >= racket_left.ycor() - 50):
        ball.dy = -ball.dy


    # Звцикливание ракеток

    if racket_left.ycor() > 350:
        racket_left.sety(-350)

    if racket_left.ycor() < -350:
        racket_left.sety(350)

    if racket_right.ycor() > 350:
        racket_right.sety(-350)

    if racket_right.ycor() < -350:
        racket_right.sety(350)























