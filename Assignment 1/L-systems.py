# Name: Sahil Daswani, ID: 20630681

import turtle

# You should put the initial string, rules, length, angle and iteration here
lsystem_string = "+++F"
lsystem_rules = [["F", "F[+F][-F]"], ["1", "0"]]
lsystemLength = 60
lsystemAngle = 30
lsystemIterations = 3
lsystemColours = ["brown", "lime green"]

# The stack includes the position and heading for the turtle at any point
stack = []

# Initializing Parameters
color_digits = []
for i in range(10):
    color_digits.append(str(i))

forwardLetters = "ABCDEF"

# Apply L-system rules to the initial string
for _ in range(lsystemIterations):
    result = ""
    for letter in lsystem_string:
        matched = False
        for rule in lsystem_rules:
            if rule[0] == letter:
                result = result + rule[1]
                matched = True
        if not matched:
            result = result + letter
    lsystem_string = result
    
# Initialize the turtle
turtle.setup(800, 600)
turtle.speed(0)
turtle.width(2)

# Move to an appropriate starting point
turtle.up()
turtle.goto(-200, 0)
turtle.down()

# Draw the final L-system string
for letter in lsystem_string:
    for forwardLetter in forwardLetters:
        if letter == forwardLetter:
            turtle.forward(lsystemLength)
    if letter == "+":
        turtle.left(lsystemAngle)
    elif letter == "-":
        turtle.right(lsystemAngle)
    elif letter == "^":
        turtle.right(180)
    elif letter == "[":
        item = [turtle.position(), turtle.heading()]
        stack.append(item)
    elif letter == "]":
        item = stack.pop()
        turtle.goto(item[0])
        turtle.setheading(item[1])
    elif letter in color_digits:
        turtle.color(lsystemColours[int(letter)])

# Hide the turtle after the drawing is finished
turtle.hideturtle()

turtle.done()
