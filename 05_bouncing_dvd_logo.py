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
# Keep WIDTH odd so WIDTH - 3 stays even and matches logo X positions.
if WIDTH % 2 == 0:
    WIDTH -= 1

NUMBER_OF_LOGOS = 5

NUMBER_OF_RAINDROPS = 175

PAUSE_AMOUNT = 0.2

COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
GRADIENT = ['white', 'yellow', 'green', 'black']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for dictionaries.
COLOR = 'color'
X = 'x'
Y= 'y'

DIR = 'direction'
GLYPH = 'glyph'
GLYPHS = ([chr(alpha_code) for alpha_code in range(ord('a'), ord('z') + 1)] +
          [chr(numeric_code) for numeric_code in range(ord('0'), ord('9') + 1)])

def main():
    bext.clear()

    # Generate a drop
    digital_rain = []
    for _ in range(NUMBER_OF_RAINDROPS):
        drop = []
        trail = 1
        anchor = random.randint(1, WIDTH - 1)
        for i in range(random.randint(7, 25)):
            drop.append({COLOR: COLORS[0], # Green.
                         X: anchor,
                         Y: trail,
                         GLYPH: random.choice(GLYPHS),})
            trail += 1
        digital_rain.append(drop)
    
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
        for drops in digital_rain: # Handle each drop in digital_rain list.
            for glyph in drops: # Handle each glyph in the drop list.
                # Erase the glyph's current location.
                bext.goto(glyph[X], glyph[Y])
                print(' ', end='')

                # Make it rain. Move the glyph down.
                glyph[Y] += 1
            
                # Moves the glyph to the top of the terminal.
                if glyph[Y] >= HEIGHT:
                    glyph[Y] = 1

        for logo in logos: # Handle each logo in the logos list.
            # Erase the logo's current location.
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            original_direction = logo[DIR]

            # See if the logo bounces off the corners.
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces += 1
            
            # See if the logo bounces off the left edge.
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            
            # See if the logo bounces off the right edge.
            # (WIDTH - 3 because 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            
            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge.
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            
            if logo[DIR] != original_direction:
                # Change color when the logo bounces.
                logo[COLOR] = random.choice(COLORS)
            
            # Move the logo. (X move by 2 because the terminal
            # characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
            
            # Display number of corner bounces.
        bext.goto(5, 0)
        bext.fg('blue')
        print(f'Corner bounces: {corner_bounces}', end='')

        for drops in digital_rain:
            num_of_glyphs = len(drops)
#            quotient = max(1, (num_of_glyphs - 1) // 4)
            

            for glyph_pos, glyph in enumerate(reversed(drops)):
                bext.goto(glyph[X], glyph[Y])
                if glyph_pos == 0:
                    bext.fg(GRADIENT[0])
                elif glyph_pos < num_of_glyphs * 0.15:
                    bext.fg(GRADIENT[1])
                elif glyph_pos < num_of_glyphs * 0.85:
                    bext.fg(GRADIENT[2])
                else:
                    bext.fg(GRADIENT[3])

                print(glyph[GLYPH], end='')

#        for logo in logos:
#            # Draw the logos a their new location.
#            bext.goto(logo[X], logo[Y])
#            bext.fg(logo[COLOR])
#            print('DvD', end='')
            
        bext.goto(0, 0)

        sys.stdout.flush() # (Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)


# If this program is run, instead of imporated, run the program.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DvD logo, Alex Flores')
        sys.exit() # When Ctrl-C is pressed, end the program.
