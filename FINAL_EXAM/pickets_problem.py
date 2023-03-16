"""
File:    pickets_problem.py
Author:  Andy Huang
Date:    12/14/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program will take in a board with spaces and pickets and
    return True if there are no pickets more than one space away
    along the diagonals of each picket.
"""
S = " "
P = "P"


def pickets_problem(board):
    """
        This function will return True if none of the pickets on the board are attacking one another.

    :param board: A 2d-list that is filled with spaces and pickets.
    :return: True if the board is good. False if the board is bad.
    """

    for y in range(len(board)):
        for x in range(len(board[y])):

            # finds position coordinates for the pickets.
            if board[y][x] == P:
                position = (x, y)

                # the checks in all four directions
                one_check = check_top_right(board, position)
                two_check = check_bottom_right(board, position)
                three_check = check_top_left(board, position)
                four_check = check_bottom_left(board, position)

                # if one of the checks are false then return False and stop checking.
                if not one_check or not two_check or not three_check or not four_check:
                    return False

    return True


def check_top_right(board, position):
    """
        This is a check function that will check the top right diagonal.

    :param board: The 2d-list
    :param position: The position of the picket
    :return: True if there are no pickets attacking and False if there are.
    """
    steps = 1
    x, y = position

    # checks all top right diagonal squares that are not in a one step reach.
    while x + steps in range(len(board[y])) and y - steps in range(len(board)):
        if steps != 1 and board[y - steps][x + steps] == P:
            return False
        steps += 1

    return True


def check_bottom_right(board, position):
    """
        This is a check function that will check the bottom right diagonal squares.

    :param board: The 2d-list
    :param position: The position of the picket
    :return: True if there are no pickets attacking and False if there are.
    """
    steps = 1
    x, y = position
    while x + steps in range(len(board[y])) and y + steps in range(len(board)):
        if steps != 1 and board[y + steps][x + steps] == P:
            return False
        steps += 1

    return True


def check_top_left(board, position):
    """
        This is a check function that will check the top left diagonal squares.

    :param board: The 2d-list
    :param position: The position of the picket
    :return: True if there are no pickets attacking and False if there are.
    """
    steps = 1
    x, y = position
    while x - steps in range(len(board[y])) and y - steps in range(len(board)):
        if steps != 1 and board[y - steps][x - steps] == P:
            return False
        steps += 1

    return True


def check_bottom_left(board, position):
    """
            This is a check function that will check the bottom left diagonal squares.

        :param board: The 2d-list
        :param position: The position of the picket
        :return: True if there are no pickets attacking and False if there are.
    """
    steps = 1
    x, y = position
    while x - steps in range(len(board[y])) and y + steps in range(len(board)):
        if steps != 1 and board[y + steps][x - steps] == P:
            return False
        steps += 1

    return True


if __name__ == '__main__':
    board = [[S, S, S, S, S], [S, P, P, S, S], [P, S, S, P, S], [S, S, S, P, S], [S, S, S, S, S]]

    print(pickets_problem(board))

