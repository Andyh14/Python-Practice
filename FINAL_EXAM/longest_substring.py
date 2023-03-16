"""
File:    longest_substring.py
Author:  Andy Huang
Date:    12/7/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program returns the length of the longest substring found in the first string given.

"""


def longest_substring(total_string, find_string):
    """
        This function will take two strings and find the longest substring of one string in the other.

    :param total_string: The given string that is going to be searched through.
    :param find_string: The string with letters or substrings I am looking for in total_string.
    :return: The length of the longest substring.
    """
    highest_number = 0
    searching_string = find_string

    # this variable is to stop the while loop
    stop_number = len(searching_string)
    i = 0
    while i != stop_number:
        if searching_string[:1] in total_string:

            # After checking for first letter go through loop for possible longer substring.
            for x in range(len(searching_string) + 1):
                if searching_string[:x] in total_string:

                    # this check makes sure highest number stays the highest number.
                    if highest_number < len(searching_string[:x]):
                        highest_number = len(searching_string[:x])

            # regardless we need to check the next letter so I slice it.
            searching_string = searching_string[1:]
        else:
            searching_string = searching_string[1:]
        i += 1
    return highest_number


if __name__ == '__main__':
    total_string = input('What is the total string you want to search through? ')
    find_string = input("What is the string you want to find in the total string? ")
    longest_value = longest_substring(total_string, find_string)

    print("The longest substring found is {} long".format(longest_value))
