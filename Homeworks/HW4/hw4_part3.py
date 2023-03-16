"""
File:         hw4_part3.py
Author:       Andy Huang
Date:         9/30/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program creates a circle when given the intended radius.

"""

radius_input = int(input('What is the radius? (between 0 and 20) '))

# creates the size of the board so it fits the whole circle
board_value = radius_input + 1

if 0 < radius_input < 20:

    # beginning of nested for loop
    for x in range(-board_value, board_value):
        empty_list = []

        for y in range(-board_value, board_value):

            # equation of a circle to find radius
            radius = (x ** 2 + y ** 2) ** 0.5

            # printing stars or spaces depending on the value of radius.
            if radius <= radius_input:
                empty_list.append('*')
            else:
                empty_list.append(' ')

        print(''.join(empty_list))
else:
    print('That\'s not in between 0 and 20 silly.. LOL')
































