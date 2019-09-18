import random

#generates random number in variable num
num = random.randint(1,100)

#Declares the state of the answer (False = wrong, True = correct)
answerState = False

# +1 everytime a player makes a guess
numberOfAttempts = 0

while answerState == False:
    #Input is created everytime the player gets the answer wrong
    userNumber = int(input("Please enter a number between 0 and 100: "))

    #Game logic
    if userNumber == num:
        answerState = True
        numberOfAttempts += 1
        print("Well done! The number was " + str(num) + ". You guessed it in " + str(numberOfAttempts) + " tries.")
    elif userNumber > num:
        print("Too high")
        numberOfAttempts += 1
    elif userNumber < num:
        print("Too low")
        numberOfAttempts += 1