import turtle
import random

# Screen properties
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Bouncing Ball Simulation")
wn.tracer(0)

# Instructions Text
text = turtle.Turtle()
text.penup()
text.color('white')
text.goto(0,270)
text.hideturtle()
text.write("Press Spacebar to Speed Up Balls", align=("center"), font=("Arial", 15, "bold"))

# Allows users to input the number of balls
ballNum = int(turtle.textinput("Simulator Settings", "Please enter the number of balls:"))

# Arrays and constants
balls = []
colors = ["red", "green", "blue", "white", "purple", "yellow"]

gravity = 0.15

# Increase speed when spacebar is pressed
def SpeedUp():
    for ball in balls:
        ball.dy += random.randint(2,4)
        ball.dx += random.randint(-10,10)/10

wn.onkey(SpeedUp, 'space')
wn.listen()

# Create i number of balls
for i in range(ballNum):
    balls.append(turtle.Turtle())

# Ball properties
for ball in balls:
    ball.color(random.choice(colors))
    ball.penup()
    ball.shape("circle")
    ball.speed(0)
    x = random.randint(-290,290)
    y = random.randint(0, 270)
    ball.goto(x, y)
    ball.dy = 0
    dx = random.randint(-3,3)
    if dx == 0:
        ball.dx = random.randint(-3,3)
    else:
        ball.dx = dx

# Infinite loop
while True:
    wn.update()

    for ball in balls:
        # Gravity affecting vertical speed
        ball.dy -= gravity

        # X and Y position changing based of horizontal and vertical speed
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # Change direction when hitting a corner and decrease speed by 10%
        if ball.ycor() < -275:
            ball.dy *= -0.9
            ball.dx *= 0.998
            ball.sety(-275)

        if ball.ycor() > 270:
            ball.dy *= -0.9
            ball.sety(270)

        if ball.xcor() > 300:
            ball.dx *= -0.9
            ball.setx(300)

        if ball.xcor() < -300:
            ball.dx *= -0.9
            ball.setx(-300)

screen.mainloop()