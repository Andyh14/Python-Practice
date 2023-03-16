"""
File:    lucky_base.py
Author:  Andy Huang
Date:    12/14/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program will convert a number to base 7.

"""


def lucky_base(number):
    """
        This function will convert a number to base 7 according to a formula.

    :param number: The integer to convert
    :return: A string that is the new number.
    """
    answer_string = ""
    find_exponent = 0
    exponent = 0

    # the loop will find the exponent value that is one over the number inputted.
    while find_exponent < number:
        exponent += 1
        find_exponent = 7 ** exponent

    changing_number = number

    # this value is 7 to the starting exponent that is closest and less than the inputted value.
    starting_exponent = exponent - 1

    # the loop executes the formula for finding each digit that forms the new number in base 7.
    for x in range(1, exponent):

        # first divide the changing number by a power of 7 that is closest and less than than the changing number.
        answer_string += (str(int(changing_number / 7 ** starting_exponent)))

        # change the changing number to be the remainder of the division.
        changing_number = changing_number % (7 ** starting_exponent)

        # make the power for the division in the next loop one less.
        starting_exponent -= 1

    # the final digit in the final number will always be the inputted number mod 7.
    final_number = str(number % 7)
    answer_string += final_number

    return answer_string


if __name__ == '__main__':
    number = int(input("give me a number: "))
    print(lucky_base(number))
