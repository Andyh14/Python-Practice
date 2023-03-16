"""
File:         the_third_degree.py
Author:       Andy Huang
Date:         11/02/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program prints out the outputs of the function the third degree for numbers 1 through 10.
"""


def the_third_degree(number):
    if number == 0:
        return 2
    if number == 1:
        return 1
    if number == 2:
        return 5

    # this is the equation for the problem with its recursive attributes
    elif number > 2:
        return (3 * the_third_degree(number - 1)) + (2 * the_third_degree(number - 2)) + (the_third_degree(number - 3))


if __name__ == '__main__':
    for i in range(10):
        print(the_third_degree(i))












