# Name: Sahil Daswani, ID: 20630681
import turtle

# Turn off animation
turtle.tracer(False)

# Menu
print()
print("a - Dragon curve")
print("b - Koch triangle (90 degree)")
print("c - Koch triangle (75 degree)")
print("d - Coloured square")
print("e - Rainbow line")
print("f - Islands and lakes")
print("g - Sierpinski triangle")
print("h - 12-point star")
print("i - 3-point star")
print("j - Plant A ")
print("k - Plant B")
print("l - Plant C")
print("m - Simple square ")
print("n - Simple triangle")
print("o - Fishbone")
print("p - Tree")
print("q - Beehive")
print()

lsystemOption = input("Select one of the 17 L-systems - Input a letter from a to q: ")
iterationOption: str = input("Select the number for iterations (Input '-' for the default): ")
printingOption = input("Input '1' to print L-system string and '2' to print L-system image: ")

# Initial strings, rules, lengths, angles and default iterations
lsystem_string = ["FX",
                  "F",
                  "F",
                  "1F+2F+3F+4F",
                  "X",
                  "F+F+F+F",
                  "A",
                  "X",
                  "[F][+F-][++F--]",
                  "F",
                  "F",
                  "X",
                  "F+F+F+F",
                  "F+F+F",
                  "A++B",
                  "0F[+1A][-1B]",
                  "0F"]

lsystem_rules = [ [["X", "X+YF+"], ["Y", "-FX-Y"]],
                  [["F", "F+F-F-F+F"]],
                  [["F", "F+F-F-F+F"]],
                  [["F", "FF"]],
                  [["X", "X0F"], ["0", "1"], ["1", "2"], ["2", "3"], ["3", "4"],["4", "5"], ["5", "6"], ["6", "0"]],
                  [["F", "F+H-FF+F+FF+FH+FF-H+FF-F-FF-FH-FFF"], ["H", "HHHHHH"]],
                  [["A", "B-A-B"],["B", "A+B+A"]],
                  [["X", "F^FF^F+X"]],
                  [["F", "FF"]],
                  [["F", "FF[-F+F][+F-F]"]],
                  [["F", "F[+F]F[-F][F]"]],
                  [["X", "F-[[X]+X]+F[+FX]-X"], ["F", "FF"]],
                  [["F", "FF"]],
                  [["F", "FF"]],
                  [["A", "F-F++F-A"], ["B", "B-F++F-F"], ["F", "FF"]],
                  [["A", "+0F[+1A][-1B]-"], ["B", "-0F[+1A][-1B]+"]],
                  [["F", "+0F-1F-G[-1F-0F]+"],["G", "GG"]] ]

lsystem_length = [10, 10, 8, 250, 50, 30, 20, 250, 250, 20, 25, 8, 150, 150, 25, 80, 20]
lsystem_angle = [90, 90, 75, 90, 90, 90, 60, 30, 120, 60, 20, 22.5, 90, 120, 90, 10, 60]
lsystem_iterations = [11, 3, 3, 0, 7, 1, 4, 6, 0, 3, 3, 4, 0, 0, 4, 4, 4]
lsystem_colours = [[], [],[],["black", "red", "green", "blue", "yellow" ],
                   ["red", "orange", "yellow", "green", "lime green", "blue", "purple" ],
                   [], [], [], [], [], [], [], [], [], [], ["brown", "green"],
                   ["yellow", "gold"]]

starting_position = [(100, -150), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (-75, 100), (0, 0), (-144, -144), (0, -200), (-150, -50)]
starting_angle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 45, 90, 30]

# The stack includes the position and heading for the turtle at any point
stack = []

# Initializing Parameters
forwardLetters = "ABCDEF"
noDrawForwardLetters = "GHIJKL"

# Get the index of the lsystem option
optionLetters = "abcdefghijklmnopq"
index = optionLetters.index(lsystemOption)

# Apply L-system rules to the initial string
def ChangeLsystemString(iterations):
    for _ in range(iterations):
        result = ""
        for letter in lsystem_string[index]:
            matched = False
            for rule in lsystem_rules[index]:
                if rule[0] == letter:
                    result = result + rule[1]
                    matched = True
            if not matched:
                result = result + letter
        lsystem_string[index] = result

if iterationOption != "-":
    ChangeLsystemString(int(iterationOption))
else:
    ChangeLsystemString(lsystem_iterations[index])
    
# Initialize the turtle
turtle.setup(800, 600)
turtle.speed(0)
turtle.width(2)

# Move to an appropriate starting point
turtle.up()
turtle.goto(starting_position[index])
turtle.setheading(starting_angle[index])
turtle.down()

# Color index array
color_digits = []
for i in range(len(lsystem_colours[index])):
    color_digits.append(str(i))

# Draw the final L-system string
if printingOption == "2":
    for letter in lsystem_string[index]:
        for forwardLetter in forwardLetters:
            if letter == forwardLetter:
                turtle.forward(lsystem_length[index])
        for noForwardLetter in noDrawForwardLetters:
            if letter == noForwardLetter:
                turtle.up()
                turtle.forward(lsystem_length[index])
                turtle.down()
        if letter == "+":
            turtle.left(lsystem_angle[index])
        elif letter == "-":
            turtle.right(lsystem_angle[index])
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
            turtle.color(lsystem_colours[index][int(letter)])
else:
    print(lsystem_string[index])

# Hide the turtle after the drawing is finished
turtle.hideturtle()

# update animation
turtle.tracer(True)
turtle.done()
