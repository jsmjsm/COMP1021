import turtle
import random


# This dictionary contains the blocks' information
# Each block type (I, J, L, S, Z, O and T) contains its color and
# tile arrangements of different orientations
blocks = {
    "I": {
        "color": "cyan",
        "tiles":
            [ [ [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ] ],
              
              [ [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 1, 1 ] ] ]
    },
    "J": {
        "color": "blue",
        "tiles":
            [ [ [ 0, 1, 0 ],
                [ 0, 1, 0 ],
                [ 1, 1, 0 ] ],
              
              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 0, 0, 1 ] ],
              
              [ [ 1, 1, 0 ],
                [ 1, 0, 0 ],
                [ 1, 0, 0 ] ],
              
              [ [ 0, 0, 0 ],
                [ 1, 0, 0 ],
                [ 1, 1, 1 ] ] ]
    },
    "L": {
        "color": "orange",
        "tiles":
            [ [ [ 1, 0, 0 ],
                [ 1, 0, 0 ],
                [ 1, 1, 0 ] ],
              
              [ [ 0, 0, 0 ],
                [ 0, 0, 1 ],
                [ 1, 1, 1 ] ],
              
              [ [ 0, 1, 1 ],
                [ 0, 0, 1 ],
                [ 0, 0, 1 ] ],
              
              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 1, 0, 0 ] ] ]
    },
    "S": {
        "color": "lime",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 0, 1, 1 ],
                [ 1, 1, 0 ] ],
              
              [ [ 1, 0, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 0 ] ] ]
    },
    "Z": {
        "color": "red",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 1 ] ],
              
              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ] ]
    },
    "O": {
        "color": "yellow",
        "tiles": [ [ [ 1, 1 ],
                     [ 1, 1 ] ] ]
    },
    "T": {
        "color": "magenta",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 0, 1, 0 ],
                [ 1, 1, 1 ] ],
              
              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 0 ] ],
              
              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 0, 1, 0 ] ],
              
              [ [ 1, 0, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ] ]
    }
}


# Initialize the map variables
tile_size = 25
map_rows = 20
map_cols = 10
map_x = -125
map_y = 250

# Create the map turtle
map_turtle = turtle.Turtle()
map_turtle.hideturtle()
map_turtle.up()

# Create the game map using a list of lists
game_map = []
for row in range(map_rows):
    game_row = []
    for col in range(map_cols):
        game_row.append("")
    game_map.append(game_row)


# Initialize the block variables
active_block = None
active_block_row = 0
active_block_col = 0
active_block_index = 0

# Create the block turtle
block_turtle = turtle.Turtle()
block_turtle.hideturtle()
block_turtle.up()


# Initialize the game update interval
game_update_interval = 250

# Initialize the game score
score = 0

# Determine if the game is over or not
game_over = False


# This helper function draws a box with the given parameters using the turtle t
# The box is drawn from the top left hand corner
def draw_box(t, width, height, pencolor, fillcolor):
    t.color(pencolor, fillcolor)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.up()

    
# This function draws the game map
def draw_map():
    map_turtle.clear()
    
    for row in range(map_rows):
        for col in range(map_cols):
            map_turtle.goto(map_x + tile_size * col, map_y - tile_size * row)

            #
            # Task: draw the tiles based on the content of the map
            #
            pass

            # Draw the tile for the current position
            draw_box(map_turtle, tile_size, tile_size, "black", "white")


# This function makes a new block to start from the top
def make_new_block():
    global active_block
    global active_block_row, active_block_col
    global active_block_index

    #
    # Task: make a new random block
    #
    pass


# This function draws the active block
def draw_block():
    block_turtle.clear()

    # Find the x and y position of the block
    x = map_x + active_block_col * tile_size
    y = map_y - active_block_row * tile_size

    #
    # Task: draw the active block at the location (x, y)
    #
    pass


# This function tests whether the block is valid given its information
def is_valid_block(block_type, block_row, block_col, block_index):

    #
    # Task: determine if the block is valid with the given information
    #
    pass

    # The block is valid
    return True

    
# This function sets the active block onto the game map
def set_block_on_map():

    #
    # Task: put the block on the game map
    #
    pass


# This function removes the completed rows on the map
def remove_completed_rows():
    global game_map

    #
    # Task: update the map by finding and removing the completed rows
    #
    pass

    #
    # Task: increase the score and difficulty when a row is completed
    #
    pass


# This function is the game loop which updates in fixed intervals
def game_loop():
    global active_block, active_block_row
    
    # If there is no active block, make one
    if active_block == None:
        
        #
        # Task: make a new block here
        #
        pass

    # Move the active block one row down
    else:

        #
        # Task: move the active block down
        #
        pass

    turtle.update()

    # Set the next update
    turtle.ontimer(game_loop, game_update_interval)


# Set up the turtle window
turtle.setup(800, 600)
turtle.bgpic("hkust.gif")
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Draw the background border around the map
turtle.goto(map_x - 10, map_y + 10)
draw_box(turtle, tile_size * map_cols + 20, tile_size * map_rows + 20, \
         "", "skyblue")

# Draw the empty map in the window
draw_map()
turtle.update()

# Set up the game loop
turtle.ontimer(game_loop, game_update_interval)


# This function handles the rotation of the block
def rotate():
    global active_block_index

    #
    # Task: handle the rotation of the block
    #
    pass


# This function handles the left movement of the block
def move_left():
    global active_block_col

    #
    # Task: handle the left movement of the block
    #
    pass


# This function handles the right movement of the block
def move_right():
    global active_block_col

    #
    # Task: handle the right movement of the block
    #
    pass


# This function drop the block down the map
def drop():
    global active_block_row

    #
    # Task: drop the block as far as it can
    #
    pass


# Set up the key handlers

#
# Task: set up the key handlers
#
pass

turtle.done()
