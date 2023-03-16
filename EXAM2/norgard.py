"""
File:         norgard.py
Author:       Andy Huang
Date:         11/18/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program finds the value of a given integer in Norgand's sequence.

"""
STARTING_NUMBER_ONE = 1
STARTING_NUMBER_TWO = 2
STARTING_NUMBER_THREE = 3
OPENING_STRING = "What value do you want to calculate? Or \"quit\" to stop: "
ENDING_STRING = "quit"


def norgard_sequence(number):
    """
    This function will output the value after a number is put through Norgard's sequence.
    :param number: A integer which is used to calculate the value of Norgand's sequence at that integer.
    :return: A number value that corresponds with the given number in Norgand's sequence.
    """
    # error check just in case
    if number < 0:
        return 0

    # base case
    if number == 0:
        return 0

    # other specific cases for the algorithm
    elif number == STARTING_NUMBER_ONE:
        return 1
    elif number == STARTING_NUMBER_TWO:
        return -1
    elif number == STARTING_NUMBER_THREE:
        return 2

    elif number > 0:
        # odd or even recursive algorithm equations
        if number % 2 == 0:
            return norgard_sequence(number // 2) * -1
        elif number % 2 != 0:
            return 1 + norgard_sequence((number - 1) // 2)


if __name__ == '__main__':
    integer_input = input(OPENING_STRING)

    # will keep on asking until "quit" is inputted
    while integer_input != ENDING_STRING:
        print(norgard_sequence(int(integer_input)))
        integer_input = input(OPENING_STRING)
