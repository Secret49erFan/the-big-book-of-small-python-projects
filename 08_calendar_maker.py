'''Calendar Maker by Alex Flores @Secret49erFan
Create monthly calendars, sacved to a text file a fit for printing.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short'''

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Alex Flores @Secret49erFan')

while True: # Loop to get the year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2026.')
    continue

while True: # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def get_calendar_for(year, month):
    cal_text = '' # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar.
    cal_text += (' ' * 34) + MONTHS[month-1] + str(year) + '\n'

    # Add the days of the week labels to the calndar.
    # (!) Try changinf the abbreviations: SUN, MON, TUE, etc.
    cal_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line that separates the weeks:
    week_separator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators.
    blank_row = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    current_date = datetime.date(year, month, 1)

     # Roll back current_date  until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True: # Loop over each week in the month.
        cal_text += week_separator

        # day_number_row is the row with the day number_labels.
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1) # Go to next day.
        day_number_row += '|\n' # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        cal_text += day_number_row
        for i in range(3): # (!) Try changing the 4 to a 5 or 10.
            cal_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
                break
        
    # Add the horizontal line at the very bottom of the calendar.
    cal_text += week_separator
    return cal_text
    

cal_text = get_calendar_for(year, month)
print(cal_text) # Display the calendar