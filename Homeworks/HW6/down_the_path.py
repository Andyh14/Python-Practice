"""
File:         hw6_part3.py
Author:       Andy Huang
Date:         11/03/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program counts the number of times the number goes through the algorithm.
"""


def down_the_path(n):
    """
    :param n: an integer
    :return: the number of times that down the path runs
    """
    # base case
    if n <= 0:
        return 0

    # adds one to the count and divides the next step.
    elif n % 15 == 0:
        return 1 + down_the_path(n / 15)

    elif n % 5 == 0:
        return 1 + down_the_path(n / 5)

    elif n % 3 == 0:
        return 1 + down_the_path(n / 3)

    else:
        # adds one to the count still but subtracts one according to the rules.
        if n > 0:
            return 1 + down_the_path(n - 1)


if __name__ == '__main__':
    for i in range(20):
        print(i, down_the_path(i))

