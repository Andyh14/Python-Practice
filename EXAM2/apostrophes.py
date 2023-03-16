"""
File:         apostrophes.py
Author:       Andy Huang
Date:         11/18/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program adds apostrophes to strings according to prof eric's rules.

"""
OPENING_STRING = "Give me a string to add apostrophes to, or quit to stop: "
END_COMMAND = "quit"
UPPER_LETTER = "S"
LOWER_LETTER = "s"
APOSTROPHE_SYMBOL_LOWER = "'s"
APOSTROPHE_SYMBOL_UPPER = "'S"


def add_apostrophe(string):
    """
    This function will add apostrophe's to a string and return the new string.
    :param string: Original string without apostrophes
    :return: New string with added apostrophes
    """
    # base case
    if not string:
        return ""

    # checks if the current first letter is "s"
    elif string[0].lower() == LOWER_LETTER:

        # check for end of string "s" if so add apostrophe s
        if len(string) == 1:
            if string[0] == UPPER_LETTER:
                return APOSTROPHE_SYMBOL_UPPER + add_apostrophe(string[1:])
            else:
                return APOSTROPHE_SYMBOL_LOWER + add_apostrophe(string[1:])

        # check for end of word "s" if so add apostrophe s
        elif string[1].isalnum() is False:
            if string[0] == UPPER_LETTER:
                return APOSTROPHE_SYMBOL_UPPER + add_apostrophe(string[1:])
            else:
                return APOSTROPHE_SYMBOL_LOWER + add_apostrophe(string[1:])

        # check for beginning "s"
        else:
            return string[0] + add_apostrophe(string[1:])
    else:
        # adds other letters that are not s
        return string[0] + add_apostrophe(string[1:])


if __name__ == '__main__':

    string_input = str(input(OPENING_STRING))

    # will keep asking until input is "quit"
    while string_input != END_COMMAND:
        print(add_apostrophe(string_input))
        string_input = str(input(OPENING_STRING))




