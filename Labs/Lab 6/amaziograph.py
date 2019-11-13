import turtle

number_of_divisions = 8 # The number of subdivisions around the centre
turtle_width = 5         # The width of the turtles

# Don't show the animation
turtle.tracer(False)

# Draw the background lines
turtle.color("gray")
for i in range(number_of_divisions):
    turtle.forward(500)
    turtle.backward(500)
    turtle.left(360 / number_of_divisions)
turtle.color("black")
turtle.hideturtle()

# Create the required turtles

allTurtles = [] # The turtles are put in this list

# The default turtle is the first one in the list

##### Add your code here #####

# Add the rest of the turtles in the list
defTurtle = turtle.Turtle()
defTurtle.shape('circle')
defTurtle.shapesize(1.3)
defTurtle.width(turtle_width)
allTurtles.append(defTurtle)
##### Add your code here #####
for _ in range(1, number_of_divisions):
    otherTurtle = turtle.Turtle()
    otherTurtle.hideturtle()
    otherTurtle.width(turtle_width)
    allTurtles.append(otherTurtle)

print(len(allTurtles))

# Set up the ondrag event
xt = [1, 1, -1, -1, 1, 1, -1, -1]
yt = [1, -1, 1, -1, 1, -1, 1, -1]

def draw(x,y):
    allTurtles[0].goto(x,y)
    for i in range(1, len(allTurtles)):
        if i < 4:
            new_x = x*xt[i]
            new_y = y*yt[i]
            allTurtles[i].goto(new_x, new_y)
        else:
            new_x = y*yt[i]
            new_y = x*xt[i]
            allTurtles[i].goto(new_x, new_y)

allTurtles[0].ondrag(draw)

colours = ["black", "tomato", "spring green", "slate blue", "turquoise", "orchid", "gold"]

# Set up the onclick event
def click(x, y):
    for i in range(len(colours)):
        if x <= (-130 + 50 * i):
            for Turtle in allTurtles:
                Turtle.color(colours[i])
            break

# Make the colour selection turtles
colourTurtles = []

for colour in colours:
    colourTurtle = turtle.Turtle()
    colourTurtle.shape("square")
    colourTurtle.up()
    colourTurtle.shapesize(2)
    colourTurtle.color(colour)
    colourTurtle.goto(-150,-250)
    colourTurtle.onclick(click)
    colourTurtles.append(colourTurtle)
    
increment = 0

for i in range(len(colourTurtles)):
    colourTurtles[i].setx(colourTurtles[i].xcor()+increment)
    increment += 50
    
while True:
    turtle.update()

turtle.done()
