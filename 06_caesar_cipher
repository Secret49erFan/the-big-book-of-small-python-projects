'''
    Caesar Ciper, by Alex Flores @Secret49erFan on X
    (al@inventwithpython.com)
    The Caesar cipher is a shift cipher that uses addition and subtraction
    to encrypt and decrypt letters.
    More info at: https://en.wikipedia.org/wiki/Caesar_cipher
    View this code at https://nostarch.com/big-book-small-python-projects
    Tags: short, beginner, cryptogrtaphy, math
'''

try:
    import pyperclip # pyperclip copies text to the clipboard
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# you can add numbers and punctuation marks to encryp those
# symbols as well.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Alex Flores @Secret49erFan on X')
print('The Caesar cipher encrypts letters by shifting then over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')

# Let the user enter if they are encyrpting or decrypting.
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter the key to use:
while True: # Keep asking until the user enters a valid key.
    max_key = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {max_key})')
    response = input('> ').upper()
    if not response.isdecimal():
        continue # To come back and do another loop for better response.

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt.
print(f'Enter the message to {mode}.')
message = input('> ')

# Caesar cipher only works on uppercase letters.
message = message.upper()

# Stores the encypted/decrypted form of the message.
translated = ''

# Encrypt/Decypt each symbol in the message.
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol) # Returns a valid index.
        if mode == 'encrypt':
            num += key
        elif mode =='decrypt':
            num -= key
        
        # Handle the wrap-around if num is larger dthan the length of
        # SYMBOLS or less than 0.
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        # Add encrypted/decrypted numbers's symbol to translated.
        translated += SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting.
        translated += symbol

# Display the encrypted/decrypted string to the screen.
print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')
except:
    pass # Do nothing if pyperclip wasn't intalled.