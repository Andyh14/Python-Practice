"""
File:         hw4_part4.py
Author:       Andy Huang
Date:         9/30/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program prints out a cycle of symbols in the shape of a square
that is in between a 1x1 board and a 50x50 board.
"""
if __name__ == "__main__":
    #                spade      heart    diamond   clover
    symbols_list = ['\u2660', '\u2665', '\u2666', '\u2663']

    size_board = int(input('What size of board do you want? (between 1 and 50) '))

    true_range = size_board
    empty_list = []

    # user input check
    if 0 < size_board < 50:
        for x in range(true_range):

            # creates the first column
            first_index = x % 4
            empty_list = [symbols_list[first_index]]

            # checks if the first symbol is a spade. If so creates corresponding row
            if symbols_list[first_index] == '\u2660':
                for y in range(1, true_range):
                    index = y % 4
                    empty_list.append(symbols_list[index])

            # checks if the first symbol is a heart. If so creates corresponding row
            if symbols_list[first_index] == '\u2665':
                for y in range(2, true_range + 1):
                    index = y % 4
                    empty_list.append(symbols_list[index])

            # checks if the first symbol is a diamond. If so creates corresponding row
            if symbols_list[first_index] == '\u2666':
                for y in range(3, true_range + 2):
                    index = y % 4
                    empty_list.append(symbols_list[index])

            # checks if the first symbol is a clover. If so creates corresponding row
            if symbols_list[first_index] == '\u2663':
                for y in range(4, true_range + 3):
                    index = y % 4
                    empty_list.append(symbols_list[index])

            print(''.join(empty_list))

    else:
        print('That\'s not in the range...')

























