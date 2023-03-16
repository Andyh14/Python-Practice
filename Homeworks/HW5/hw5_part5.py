"""
File:         hw5_part5.py
Author:       Andy Huang
Date:         10/14/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program takes a random list of numbers and puts them in descending order.
"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'STOP'
MAX_INT = 100
"""
    Start coding here!
"""


def swap(swapping_list, i, j):
    """
    :param swapping_list: the list that we're reverse sorting
    :param i: the first position to swap
    :param j: the second position to swap
    """
    # switches the two values using indexing
    if swapping_list[j] > swapping_list[i]:
        swapping_list[i], swapping_list[j] = swapping_list[j], swapping_list[i]
        return swapping_list

    if swapping_list[j] == swapping_list[i]:
        return swapping_list


def find_max_index_after(i, some_list):
    """
    :param i: start at position i to look for the max
    :param some_list: the list to search
    :return: the INDEX of the maximum, not the maximum itself!
    """
    greater_index = 0
    max_number = some_list[i]

    # finds the max number and it's index from index value i to the end.
    for x in range(i, len(some_list)):
        if some_list[x] >= max_number:
            max_number = some_list[x]
            greater_index = x
    return greater_index


def reverse_selection_sort(a_list):
    """
    :param a_list: the list to reverse sort
    :return: the reverse sorted list
    """
    answer_list = []

    # for every i finds the max from i to the end and switches the max and the i value
    for i in range(len(a_list)):
        max_index = find_max_index_after(i, a_list)
        answer_list = swap(a_list, i, max_index)
    return answer_list


"""
    Your code should end here.  The driver below should not be modified during submission.
"""


if __name__ == '__main__':
    length_or_stop = input('What length of list do you want to sort? (or STOP to end) ')
    while length_or_stop != STOP_PARAM:
        try:
            the_list = [randint(0, MAX_INT) for _ in range(int(length_or_stop))]
            print('The list is: ', the_list)
            print('The reverse sort is: ', reverse_selection_sort(the_list))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input('What length of list do you want to sort? (or STOP to end) ')
