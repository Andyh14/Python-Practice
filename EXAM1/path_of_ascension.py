"""
File:         path_of_ascension.py
Author:       Andy Huang
Date:         10/4/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program finds the longest ascending subsequence in a random list.
The size of the list can be determined by the user.
"""

import sys
from random import seed, randint

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    length = int(input('What length of sequence do you want to input? '))

    ascension_list = []

    for element in range(length):
        ascension_list.append(randint(0, 100))

    # check the length so it is between 0 and 1000 inclusively
    if 0 <= length <= 1000:
        print(ascension_list)
        increasing_amount = 1
        max_ascending = 1

        # if number is less than the one in front of it then add 1 to the increasing amount
        for i in range(0, len(ascension_list) - 1):

            if ascension_list[i] < ascension_list[i + 1]:
                increasing_amount += 1

            else:
                increasing_amount = 1

            # keeps the largest increasing amount after it loops through and checks all the numbers in the list
            if increasing_amount > max_ascending:
                max_ascending = increasing_amount

        print('The max ascending length is ', max_ascending)

    else:
        print('You can\'t use that length... Try a number between 0 and 1000!')
