"""
File:    jumble.py
Author:  Andy Huang
Date:    12/7/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program uses the jumble function that will jumble a given string.

"""
QUIT = "quit"


def jumble(a_string, a, b):
    """
        This function will returned a jumble string according to the given equation.

    :param a_string: The string to jumble.
    :param a: A integer value that is multiplied by the index of a letter for the equation.
    :param b: A integer value that is added in the equation.
    :return: A jumbled string.
    """
    new_string = ""
    list_new_indexes = []
    for x in range(len(a_string)):

        # equation line to find the index
        new_index = ((a * x) + b) % len(a_string)

        # check fo repeats and if not repeated then add it to the returned string.
        if new_index not in list_new_indexes:
            new_string += a_string[new_index]
            list_new_indexes.append(new_index)
    return new_string


if __name__ == '__main__':
    input_string = input("What is a string to jumble? or \"quit\" to stop: ")

    while input_string != QUIT:
        a = int(input("What is your a value for the equation? "))
        b = int(input("What is your b value for the equation? "))
        jumbled_string = jumble(input_string, a, b)
        print(jumbled_string)
        print()

        input_string = input("What is a string to jumble? ")
