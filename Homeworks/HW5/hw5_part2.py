"""
File:         hw5_part2.py
Author:       Andy Huang
Date:         10/13/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program takes a list and computes the next level of Pascal's triangle based on the previous level.
"""


def pascal_level(a_list):
    """
    :param a_list: a list represents the previous level in the pascal's triangle construction
    :return: a new list with the previous elements summed
    """
    previous_list = a_list
    if len(previous_list) == 1:
        previous_list.append(1)
        return previous_list

    # creates the answer list with its starting 1 and the ending 1 with the correct numbers in between.
    if len(previous_list) > 1:
        answer_list = [previous_list[0]]

        # formula for creating the pascal triangle using the previous list
        for index in range(len(previous_list) - 1):
            answer_list.append(previous_list[index] + previous_list[index + 1])

        # adds the 1 that is always at the end of the list.
        answer_list.append(previous_list[0])

        return answer_list


if __name__ == '__main__':
    next_line = [1]
    for i in range(10):
        print(next_line)
        next_line = pascal_level(next_line)

    print(pascal_level([1, 2, 3, 4, 5]))
    print(pascal_level([1, 1, 2, 3, 5, 8]))
    print(pascal_level([1, 1, 2, 3, 5, 8, 13, 1]))
