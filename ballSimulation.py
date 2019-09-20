import turtle
import random

# Screen properties
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Bouncing Ball Simulation")
wn.tracer(0)

ballNum = int(turtle.textinput("Simulator Settings", "Please enter the number of balls:"))

balls = []
colors = ["red", "green", "blue", "white", "purple", "yellow"]

for i in range(ballNum):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.color(colors[random.randint(0,len(colors)-1)])
    ball.penup()
    ball.shape("circle")
    ball.speed(0)
    x = random.randint(-290,290)
    y = random.randint(0, 270)
    ball.goto(x, y)
    ball.dy = 0
    dx = random.randint(-2,2)
    if dx == 0:
        ball.dx = 2
    else:
        ball.dx = dx

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() < -270 or ball.ycor() > 270:
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.goto(random.randint(-290,290), random.randint(0, 270))
            ball.dy = 0

        if ball.xcor() > 300 or ball.xcor() < -300:
            ball.dx *= -1

screen.mainloop()
