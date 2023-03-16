"""
File:         knights_move_sum.py
Author:       Andy Huang
Date:         10/5/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  The program will print the board then ask the user to position the knight piece in a position
in a 4x4 matrix made of random numbers. The program will then calculate the total of all the values where
the knight is able to move in the matrix.
"""

import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == '__main__':
    the_matrix = []
    for i in range(4):
        new_row = []
        for j in range(4):
            new_row.append(randint(0, 100))
        the_matrix.append(new_row)
    print(the_matrix)

    # creates/prints the matrix in a 4x4 square shape without the brackets
    for row in range(4):
        for col in range(4):
            print(the_matrix[row][col], end=' ')
        print('')

    row_value = int(input('What is the row that you want to start at? '))

    column_value = int(input('What is the column that you want to start at? '))

    # creating variables with easy to understand names so messing up the list of knight moves is harder.
    knight_move_up_2 = row_value - 2
    knight_move_down_2 = row_value + 2
    knight_move_left_2 = column_value - 2
    knight_move_right_2 = column_value + 2
    knight_move_up_1 = row_value - 1
    knight_move_down_1 = row_value + 1
    knight_move_left_1 = column_value - 1
    knight_move_right_1 = column_value + 1

    the_total = 0
    # list of all possible night move combinations.
    knight_moves = [[knight_move_up_2, knight_move_right_1], [knight_move_up_2, knight_move_left_1],

                    [knight_move_down_2, knight_move_right_1], [knight_move_down_2, knight_move_left_1],

                    [knight_move_up_1, knight_move_left_2], [knight_move_down_1, knight_move_left_2],

                    [knight_move_up_1, knight_move_right_2], [knight_move_down_1, knight_move_right_2]]

    # adds all the values at all the possible knight moves only if those knight moves are inside the range(4).
    if knight_moves[0][0] < 4 and knight_moves[0][1] < 4:
        the_total += the_matrix[knight_moves[0][0]][knight_moves[0][1]]

    if knight_moves[1][0] < 4 and knight_moves[1][1] < 4:
        the_total += the_matrix[knight_moves[1][0]][knight_moves[1][1]]

    if knight_moves[2][0] < 4 and knight_moves[2][1] < 4:
        the_total += the_matrix[knight_moves[2][0]][knight_moves[2][1]]

    if knight_moves[3][0] < 4 and knight_moves[3][1] < 4:
        the_total += the_matrix[knight_moves[3][0]][knight_moves[3][1]]

    if knight_moves[4][0] < 4 and knight_moves[4][1] < 4:
        the_total += the_matrix[knight_moves[4][0]][knight_moves[4][1]]

    if knight_moves[5][0] < 4 and knight_moves[5][1] < 4:
        the_total += the_matrix[knight_moves[5][0]][knight_moves[5][1]]

    if knight_moves[6][0] < 4 and knight_moves[6][1] < 4:
        the_total += the_matrix[knight_moves[6][0]][knight_moves[6][1]]

    if knight_moves[7][0] < 4 and knight_moves[7][1] < 4:
        the_total += the_matrix[knight_moves[7][0]][knight_moves[7][1]]

    print('The sum of the chess moves is', the_total)
