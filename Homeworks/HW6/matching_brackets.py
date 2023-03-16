"""
File:         matching_brackets.py
Author:       Andy Huang
Date:         11/02/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program matches curly braces and returns false if there isn't a matching pair.
"""


def match_brackets(bracket_string, count=0):
    if count < 0:
        return False

    # this filters through once all the slicing is done
    if not bracket_string:
        if count > 0:
            return False
        else:
            return True

    # slices off the open bracket
    elif bracket_string[0] == "{":
        return match_brackets(bracket_string[1:], count + 1)

    # slices off the ending bracket and if it starts out negative stop it there.
    elif bracket_string[0] == "}":
        if count - 1 < 0:
            return False
        else:
            return match_brackets(bracket_string[1:], count - 1)
    else:
        # slices off letters or anything that isn't a curly bracket
        return match_brackets(bracket_string[1:], count)


if __name__ == '__main__':
    question_string = str(input('Enter a string with brackets: '))
    while question_string != 'quit':
        if match_brackets(question_string, 0):
            print(True)
        else:
            print(False)
        question_string = str(input('Enter a string with brackets: '))



