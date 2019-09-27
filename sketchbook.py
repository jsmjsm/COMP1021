# COMP1021 Lab 2 Python sketchbook

import turtle       # Import the turtle module for the program

turtle.width(4)

print("Welcome to the Python sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""

colorfill = ""

if colorfill != "none":
    turtle.fillcolor(colorfill)
    turtle.begin_fill()

while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("q - Quit the program")
    print("s - Speed of the turtle")

    turtle.begin_fill()

    option = input("Please input your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        #
        # Please put your code here
        angle = int(input("Please enter the angle of rotation: "))

        turtle.left(angle)

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        #
        # Please put your code here
        height = int(input("Please enter the height of the rectangle: "))
        width = int(input("Please enter the width of the rectangle: "))

        for i in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)

    ##### Handle the circle option
    if option == "c":
        print()

        #
        # Please put your code here
        radius = int(input("Please enter the radius of the circle: "))

        turtle.circle(radius)

    ##### Handle the pen colour option
    if option == "p":
        print()

        #
        # Please put your code here
        color = input("Please enter a colour name: ")
        turtle.pencolor(color)

    ##### Handle the fill colour option
    if option == "f":
        print()

        #
        # Please put your code here
        colorfill = input("Please enter a colour name (type 'none' to clear the colour): ")


    turtle.end_fill()

    if option == "s":
        print()

        #
        # Please put your code here
        speed = int(input("Choose speed of the turtle (0 is maximum): "))
        turtle.speed(speed)

turtle.done()
