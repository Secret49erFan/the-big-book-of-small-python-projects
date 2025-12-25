'''
Bouncing DVD Logo, by Alex Flores, @Secret49erFan on X.
(Al Sweigart | al@inventwithpython.com)
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, bext
'''

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext mod, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants.
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one.
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries.
COLOR = 'color'
X = 'x'
Y= 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1
    
    corner_bounces = 0 # Count how many times a logo hits a corner
    while True: # Main program loop.
        for logo in logos: # Handle each logo in the logos list.
            # Erase the logo's current location.
            bext.goto(logo[X], logo[Y])