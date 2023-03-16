"""
File:    jelly_bean_sort.py
Author:  Andy Huang
Date:    12/14/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
        This function will sort jelly beans by their color in ascending order.
"""
NUMBER = 1


def jelly_bean_sort(list_of_colors):
    """
        This function will return a sorted list in ascending order

    :param list_of_colors: A list of strings that could be colors or not.
    :return: A sorted list that is in ascending order.
    """
    colors = []
    final_list = []

    # creates color names that are not repeats.
    for color in list_of_colors:
        if color not in colors:
            colors.append(color)

    # creates the amount of each color and appends the color and number in the correct format.
    for color in colors:
        color_number = 0
        for bean_color in list_of_colors:
            if color == bean_color:
                color_number += 1
        final_list.append([color, color_number])

    # selection sorting using the helper functions
    for index in range(len(final_list)):
        min_index = find_min_number(final_list, index)
        swap(final_list, min_index, index)

    return final_list


def find_min_number(a_list, start):
    """
        This function will return the smallest number index.

    :param a_list: The list to search through to find the smallest number index.
    :param start: The index in the list where the function will start checking.
    :return: The smallest number index
    """
    min_index = start
    for i in range(start, len(a_list)):

        # the NUMBER index is to access the number in the tuple for comparison.
        if a_list[min_index][NUMBER] > a_list[i][NUMBER]:
            min_index = i

    return min_index


def swap(a_list, x, y):
    """
        This function will swap two things in a list.

    :param a_list: The list of tuples in this case
    :param x: The index of one position in the list.
    :param y: The index of the other position in the list.
    :return: None - since a_list is mutable
    """
    temp = a_list[x]
    a_list[x] = a_list[y]
    a_list[y] = temp


if __name__ == '__main__':
    jelly_bean_list = ['red', 'green', 'red', 'yellow', 'green', 'red', 'blue', 'red', 'green', 'yellow']
    print(jelly_bean_sort(jelly_bean_list))
