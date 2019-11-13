import random
import time
import turtle
import pygame

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

firework_radius = 100   # The maximum radius a firework can have
firework_count = 40     # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]


##### Initialize the turtle module

turtle.setup(screen_width, screen_height)
turtle.bgpic("hong_kong.gif")
turtle.width(2)
turtle.speed(6)
turtle.hideturtle()
pygame.mixer.init()

##### For loop to shoot individual firework

for i in range(firework_count):
    turtle.speed(3)
    pygame.mixer.music.load("firework_launch.mp3")
    
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1)
        turtle.clear()

    # Initialize a starting position
    starty = -(screen_height/2)
    startx = random.randint(-(screen_width/2), (screen_width/2))
    turtle.up()
    turtle.goto(startx, starty)
    turtle.down()
    
    # Initialize a destination
    destx = random.randint(-(screen_width/2), (screen_width/2))
    desty = random.randint(0, screen_height/2)
    
    # Shoot a firework from the start to the destination
    turtle.color("orange")
    pygame.mixer.music.play()
    turtle.goto(destx, desty)
    turtle.tracer(False)
    turtle.undo()
    turtle.up()
    turtle.goto(destx, desty)

    # Pick a firework color from the firework colour list
    color = firework_colours[random.randint(0, (len(firework_colours)-1))]
    turtle.color(color)

    # Pick a size for the firework
    fireworkRadius = random.randint(firework_radius/2, firework_radius)
    # Pick the number of explosion directions
    numberOfDots = 12

    ##### For loop to draw each ring of explosion
    radius = 12
    while radius < fireworkRadius:
        turtle.forward(12)
        turtle.left(90)
        for i in range(numberOfDots):
            turtle.circle(radius, 360/numberOfDots)
            turtle.dot(radius/12)
            
        turtle.right(90)
        turtle.sety(turtle.ycor()-4)
        radius += 12
    pygame.mixer.music.load("firework_explosion_001.mp3")
    pygame.mixer.music.play()
    turtle.update()
    turtle.tracer(True)
    time.sleep(1)
    
turtle.done()
