"""Sevseg, by Alex Flores @alexflores83 on X
A seven-segment number display module, used by the Countdown and Digital
Clock progrmas.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, module"""

"""A labeled seven-segment display, with each segment labeled A to G:
  __A__
 |     |    Each digit in a seven-segment display:
 F     B     __       __   __        __   __  __   __   __
 |__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
 |     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
 E     C
 |__D__|"""


def get_sev_seg_str(number, min_width=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smallter than min_width."""

    # Convert number to string in case it's an int or fl