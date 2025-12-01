''' Birthday Paradox Simulation, By Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox."
More info at https://en.wikipedia.org/wiki/Birthday_problem.
View this code at https://nostarch.com/big-book-small-python-projects.
Tags: short, math, simulation'''

import datetime, random


def get_birthdays(number_of_birthdays):
    '''Returns a list of a number of random date objects for birthdays.'''
    birthdays = []
    # The year is unimportant for our simulation, as long as all
    # birthdays have the same year.
    start_of_year = datetime.date(2001, 1, 1)
    for i in range(number_of_birthdays):
        # Get a random day into the year.
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays
            
def get_match(birthdays):
    '''Returns a set of date objects of birthdays that occurs more than once
       in the birthday list''' 
    seen = set()
    dupes =  set()
    for birthday in birthdays:
        if birthday in seen:
            dupes.add(birthday)
        else:
            seen.add(birthday)
    return dupes # empty set if no dupes

def set_full_month(birthday):
    '''Converts the abbreviated str to a full str'''
    date_text = f'{birthday:%B %#d}'
    return date_text

# Display the intro:
print('''
      Birthday Paradox, by Alex Flores @secret49erfan on X
      (Al sweigart al@inventwithpython.com)

      The birthday paradox shows us that in a group of N people, the odds
      that two of them have matching birthdays is surprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random
      simulations) to explore this concept.

      (It's not actually a paradox, it's just a surprising result.)
      ''')

while True: # Keep asking until the user enters a valid amount.
    print ('How many birthdays shall I generate? (Max 150)')
    response = input('>')
    if response.isdecimal() and (0 < int(response) <= 150):
        number_bdays = int(response)
        break # The user enters a valid amount.
print()

# Generate and display the birthdays.
print(f'Here are {number_bdays} birthdays:')
birthdays = get_birthdays(number_bdays)

date_text = ', '.join(set_full_month(birthday) for birthday in sorted(birthdays))
print(date_text)

# for i, birthday in enumerate(birthdays):
#     if i != 0:
#         # Display a comma for each birthday af ther the first birthday,
#         print(', ', end='')
#     # month_name = MONTHS[birthday.month - 1]
#     date_text = set_full_month(birthday) # birthday.strftime('%B %#d')
#     print(date_text, end='')
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display th results.
print('In this example, ', end='')
if match:
    # month_name = MONTHS[match.month - 1]
    date_text = ', '.join(set_full_month(birthday) for birthday in sorted(match)) # birthday.strftime('%B %#d')
    print(f'multiple people have a birthday on {date_text}')
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations.
print(f'Generating {number_bdays} random birthdays,')
input('Press enter to begin...')

print("Let's run 100,000 simulations.")
sim_match = 0 # How many simulations had matching birthdays in them.
bd_match = 0
for i in range(100_000):
    # Report on the progress every 10_000 simulations.
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(number_bdays)
    
    if datetime.date(2001, 5, 11) in birthdays:
        bd_match += 1
            # print(f'Ding! {birthday} in simulation #{i}')
    
    # if get_match(birthdays) != None:
    #     sim_match += 1
    dupes = get_match(birthdays) # Returns a set of duplicate dates
    if dupes:
        sim_match += 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(sim_match / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {number_bdays} people, there was a')
print(f'matching birthday in that group {sim_match} times. This means')
print(f'that {number_bdays} people have a {probability}% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")
print(f'Your birthday had a match {bd_match} times in 100,000 simulations of {number_bdays} people!')