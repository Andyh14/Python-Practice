"""
File:         hw2_part2.py
Author:       Andy Huang
Date:         9/14/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program is a puzzle where the user will get the loot if they get the right knob and
switch combination.

"""

first_knob_position = int(input('What is the position of the first knob? (Enter 1-12) '))

second_knob_position = int(input('What is the position of the second knob? (Enter 1-12) '))

switch_position = input('What is the position of the switch? (Enter up or down) ')


if first_knob_position <= 0 or second_knob_position <= 0:
    print('Knobs can only be in positive nonzero positions')
else:
    if first_knob_position % 2 == 0 and second_knob_position % 2 != 0:
        if switch_position.lower() == "up":
            print('The door opens, you get all the loot! ')
        else:
            print('The door clanks but does not open, try again. ')

    if first_knob_position % 2 == 0 and second_knob_position % 2 == 0:
        print('The door clanks but does not open, try again. ')
    if first_knob_position % 2 != 0 and second_knob_position % 2 != 0:
        print('The door clanks but does not open, try again. ')

    if first_knob_position % 2 != 0 and second_knob_position % 2 == 0:
        print('The handle doesn\'t budge...')












