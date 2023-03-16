"""
File:         find_the_way.py
Author:       Andy Huang
Date:         11/21/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program finds a path that leads off the board from a random start point.
"""
import sys
import random

STARTING_COUNT = 0
ALLOWED = '_'
FORBIDDEN = '*'
PROPER_PATH = "O"
NO_PATH = "B"


def create_map(x, y, p):
    """
    :param x: the number of rows of the grid
    :param y: the number of cols of the grid
    :param p: the probability of a forbidden space
    :return: the grid, the starting location
    """
    the_grid = [[FORBIDDEN if random.random() < p else ALLOWED for j in range(y)] for i in range(x)]
    x = random.randint(0, x - 1)
    y = random.randint(0, y - 1)
    the_grid[x][y] = 's'
    return the_grid, [x, y]


def find_the_way_out(the_grid, starting_position):
    """
    :param the_grid: this is a 2d grid, either the positions will be ALLOWED which is a space, or "*" or "s".  s is the starting position passed as a list
        and * is
    :param starting_position:  the starting list/tuple coordinate for the starting position.
    :return: True if there is a way out, False if not

    You need to implement this function
    You are permitted to add helper functions but you shouldn't change the signature (name and parameters) of this function.
    """
    # sets starting position and symbol for that spot on the grid
    x, y = starting_position
    the_grid[x][y] = PROPER_PATH

    # base case where if x or y value is about to be off the board.
    if x == 0 or y == 0 or x == (len(the_grid) - 1) or y == (len(the_grid[0]) - 1):
        return True

    # recursion checks for finding the path.
    # check up
    if x - 1 >= 0 and the_grid[x - 1][y] == ALLOWED:
        if find_the_way_out(the_grid, (x - 1, y)):
            return True
        the_grid[x - 1][y] = ALLOWED

    # check left
    if y - 1 >= 0 and the_grid[x][y - 1] == ALLOWED:
        if find_the_way_out(the_grid, (x, y - 1)):
            return True
        the_grid[x][y - 1] = ALLOWED

    # check right
    if y + 1 < len(the_grid) and the_grid[x][y + 1] == ALLOWED:
        if find_the_way_out(the_grid, (x, y + 1)):
            return True
        the_grid[x][y+1] = ALLOWED

    # check down
    if x + 1 < len(the_grid) and the_grid[x + 1][y] == ALLOWED:
        if find_the_way_out(the_grid, (x + 1, y)):
            return True
        the_grid[x + 1][y] = ALLOWED

    # if not any return False
    return False


def display(the_grid):
    """
        This should display the grid on the screen.
    :param the_grid: the 2d grid.
    """
    print('\n'.join(''.join([str(x).ljust(3) for x in the_grid[i]]) for i in range(len(the_grid))))


def cant_find_the_way_out(the_grid, starting_position):
    """
    This function puts a symbol for all the spaces a piece can move in the grid.
    :param the_grid: A 2D grid that represents the board.
    :param starting_position: The x, y coordinate of the starting position.
    :return:
    """
    # sets starting position and what symbol to place in each spot the function iterates.
    x, y = starting_position
    the_grid[x][y] = NO_PATH

    # all possible movement checks in the area that is allowed.
    if x - 1 >= 0 and the_grid[x - 1][y] == ALLOWED:
        cant_find_the_way_out(the_grid, (x - 1, y))

    if y - 1 >= 0 and the_grid[x][y - 1] == ALLOWED:
        cant_find_the_way_out(the_grid, (x, y - 1))

    if y + 1 < len(the_grid) and the_grid[x][y + 1] == ALLOWED:
        cant_find_the_way_out(the_grid, (x, y + 1))

    if x + 1 < len(the_grid) and the_grid[x + 1][y] == ALLOWED:
        cant_find_the_way_out(the_grid, (x + 1, y))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        seed = int(sys.argv[1])
        x_dimension = int(sys.argv[2])
        y_dimension = int(sys.argv[3])
        probability = float(sys.argv[4])
    else:
        seed = input('What is the seed (enter a string): ')
        x_dimension = int(input('Enter the x dimension: '))
        y_dimension = int(input('Enter the y dimension: '))
        probability = float(input('Enter a float between 0 and 1 to represent the probability of a forbidden space: '))

    random.seed(seed)

    while input('Again? ').strip().lower() == 'yes':
        the_grid, starting = create_map(x_dimension, y_dimension, probability)
        display(the_grid)
        path = find_the_way_out(the_grid, starting)
        print(path)

        # scenario where the function returns false then make all the symbols placed a NO_PATH symbol.
        if not path:
            cant_find_the_way_out(the_grid, starting)
        display(the_grid)
