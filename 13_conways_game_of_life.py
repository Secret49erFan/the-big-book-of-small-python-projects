"""Conway's Game of Life, by Alex Flores @alexflores83 on X
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation"""

import copy, random, sys, time

# Set up the constants.
WIDTH = 79 # The width of the cell grid.
HEIGHT = 20 # The height of the cell grid.

# (!) Change ALIVE to '#' or another character.
ALIVE = "O" # The character representing a living cell.
# (!) Change DEAD to '.' of another character.
DEAD = " " # The character representing a dead cell.

# (!) Change ALIVE to "|" and DEAD to "-".

# The cells are next_cells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
next_cells = {}
# Put random dead and alive cells into next_cells.
for x in range(WIDTH): # Loop over every posible column.
    for y in range(HEIGHT): # Loop over every possible row.
        # 50/50 chance for starting cells being dead or alive.
        if random.randint(0, 1) == 0:
            next_cells = ALIVE # Add a living cell. 
        else:
            next_cells = DEAD # Add a dead cell.

while True: # Main program loop.
    # Each iteration of this loop is a step of the simulation.
    
    print("\n" * 50) # Seperate each step of the simulation.
    cell = copy.deepcopy(next_cells)