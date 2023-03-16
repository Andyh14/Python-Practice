"""
File:    nth_day.py
Author:  Andy Huang
Date:    12/12/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program calls a function that will calculate the total number of gifts a person will receives. 

"""


def nth_day_of_christmas(day):
    """
        This function will recursively count the number of gifts that you receive in total.
    :param day: The integer number of days to calculate how many gifts per days
    :return: The number of gifts in total
    """

    # base case?
    if day <= 0:
        return 0

    # initial values with recursion according to the equation.
    if day == 1:
        return 1 + nth_day_of_christmas(day - 1)

    if day == 2:
        return 3 + nth_day_of_christmas(day - 1)

    if day == 3:
        return 6 + nth_day_of_christmas(day - 1)

    if day > 3:

        # algorithm for the number of gifts.
        gifts = int((day * (day + 1)) / 2)

        # recursion
        return gifts + nth_day_of_christmas(day - 1)


if __name__ == '__main__':
    day = input("Give me a number of days in december: ")
    while day != "quit":

        print(nth_day_of_christmas(int(day)))

        day = input("Give me a number of days in december: ")