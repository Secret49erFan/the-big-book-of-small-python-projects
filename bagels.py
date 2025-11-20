'''
Alex Flores @secret49erfan on X
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle
'''
import random
import string

# (!) Try setting this to 1 or 10.
NUM_DIGITS = 3

# (!) Try setting this to 1 or 100.
MAX_GUESSES = 20


def main():
    print(f'''
          Bagels, a deductive logic game.
          By Alex Flores @secret49erfan on X insprired by Al Sweigart.
          
          I am thinking of a {NUM_DIGITS}-digit code with no repeated digits or letters.
          Try to guess what it is. Here are some clues:
          When I say:   That means:
          Pico          One digit is correct but in the wrong position.
          Fermi         One digit is correct and in the right position.
          Bagels        No digit is correct.

          For example, if the secret number was 248 and your guess was 843,
          the clues would be Fermi Pico.
          ''')
    
    # Main game loop.
    while True:
        # This stores the secret number the player needs to guess.
        secret_num = get_secret_number()
        print('I have thought up a code.')
        print(f'You have {MAX_GUESSES} to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess.

            while len(guess) != NUM_DIGITS or not guess.isalnum():
                print(f'Guess #{num_guesses}')
                guess = input('>').upper()
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                # They're correct, so break out of this loop.
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'the answer was {secret_num}')
        
        # Ask player if the want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_number():
    '''Returns a string made up of NUM_DIGITS unique random digits'''
    # Create a list of digits of 0 to 9.
    characters = list(string.digits) + list(string.ascii_uppercase)
    random.shuffle(characters)

    # Get the first NUM_DIGITS digits in the list for the secret number.
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += characters[i]
    return secret_num


def get_clues(guess, secret_num):
    '''Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair.'''
    if guess == secret_num:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        # There are no correct digits at all.
        return 'Bagels'
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ''.join(clues)


# If the program is executed (instead of imported), run the game:
if __name__ == '__main__':
    main()