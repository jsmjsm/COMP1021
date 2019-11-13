import random
import turtle

# Generates random number in variable num
num = random.randint(1,100)

# Declares the state of the answer (False = wrong, True = correct)
answerState = False

# +1 everytime a player makes a guess
numberOfAttempts = 0

# Create Turtle
text = turtle.Turtle()
text.hideturtle()
text.write("Please enter an integer number between 1 and 100.", align=("center"),font=("Arial", 20, "bold"))

# Function to clear turtle and change text
def ChangeText(message):
    text.clear()
    text.write(message, align=("center"), font=("Arial", 20, "bold"))

while not answerState:
    # Input is created everytime the player gets the answer wrong
    userNumber = int(turtle.textinput("Guessing Game", "Please enter a number between 1 and 100:"))

    # Game logic
    if userNumber == num:
        answerState = True
        numberOfAttempts += 1
        ChangeText("Well done! The number was %s. You guessed it in %s tries." % (num, numberOfAttempts))
    elif userNumber > num:
        numberOfAttempts += 1
        ChangeText("Too High.")
    elif userNumber < num:
        numberOfAttempts += 1
        ChangeText("Too Low.")

turtle.done()