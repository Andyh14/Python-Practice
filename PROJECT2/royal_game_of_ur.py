"""
File:    royal_game_of_ur.py
Author:  Andy Huang
Date:    11/11/2020
Section: 46
E-mail:  Andyh1@umbc.edu
Description:
  This program allows you to play the royal game of ur.
"""

from sys import argv
from random import choice
from board_square import BoardSquare, UrPiece

STARTING_PIECES = 7
WHITE_COLOR = "White"
BLACK_COLOR = "Black"
BLACK_SYMBOL = "B"
WHITE_SYMBOL = "W"
OFF_BOARD_STATEMENT = "currently off the board"
LINE_OF_QUOTES = '""""""""""""""""""""""""""""""""""""""""""""""""""'
ENDING_STEPS = [1, 2]
NO_OPTION_STRING = "You do not have any options so it is the next person's turn. "

class RoyalGameOfUr:
    STARTING_PIECES = 7
    WHITE_COLOR = "White"
    BLACK_COLOR = "Black"
    OFF_BOARD_STATEMENT = "currently off the board"

    def __init__(self, board_file_name):
        self.board = None
        self.load_board(board_file_name)
        self.white_pieces = []
        self.black_pieces = []
        self.starting_white = None
        self.starting_black = None
        self.ending_white = None
        self.ending_black = None
        self.completed_white_pieces = []
        self.completed_black_pieces = []
        self.win_condition = False
        self.name_player_one = None
        self.name_player_two = None

    def load_board(self, board_file_name):
        """
        This function takes a file name and loads the map, creating BoardSquare objects in a grid.

        :param board_file_name: the board file name
        :return: sets the self.board object within the class
        """

        import json
        try:
            with open(board_file_name) as board_file:
                board_json = json.loads(board_file.read())
                self.num_pieces = self.STARTING_PIECES
                self.board = []
                for x, row in enumerate(board_json):
                    self.board.append([])
                    for y, square in enumerate(row):
                        self.board[x].append(BoardSquare(x, y, entrance=square['entrance'], _exit=square['exit'],
                                                         rosette=square['rosette'], forbidden=square['forbidden']))

                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if board_json[i][j]['next_white']:
                            x, y = board_json[i][j]['next_white']
                            self.board[i][j].next_white = self.board[x][y]
                        if board_json[i][j]['next_black']:
                            x, y = board_json[i][j]['next_black']
                            self.board[i][j].next_black = self.board[x][y]
        except OSError:
            print('The file was unable to be opened. ')

    def draw_block(self, output, i, j, square):
        """
        Helper function for the display_board method
        :param output: the 2d output list of strings
        :param i: grid position row = i
        :param j: grid position col = j
        :param square: square information, should be a BoardSquare object
        """
        MAX_X = 8
        MAX_Y = 5
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 or y == 0 or x == MAX_X - 1 or y == MAX_Y - 1:
                    output[MAX_Y * i + y][MAX_X * j + x] = '+'
                if square.rosette and (y, x) in [(1, 1), (1, MAX_X - 2), (MAX_Y - 2, 1), (MAX_Y - 2, MAX_X - 2)]:
                    output[MAX_Y * i + y][MAX_X * j + x] = '*'
                if square.piece:
                    # print(square.piece.symbol)
                    output[MAX_Y * i + 2][MAX_X * j + 3: MAX_X * j + 5] = square.piece.symbol

    def display_board(self):
        """
        Draws the board contained in the self.board object

        """
        if self.board:
            output = [[' ' for _ in range(8 * len(self.board[i // 5]))] for i in range(5 * len(self.board))]
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if not self.board[i][j].forbidden:
                        self.draw_block(output, i, j, self.board[i][j])

            print('\n'.join(''.join(output[i]) for i in range(5 * len(self.board))))

    def roll_d4_dice(self, n=4):
        """
        Keep this function as is.  It ensures that we'll have the same runs with different random seeds for rolls.
        :param n: the number of tetrahedral d4 to roll, each with one dot on
        :return: the result of the four rolls.
        """
        dots = 0
        for _ in range(n):
            dots += choice([0, 1])
        return dots

    def play_game(self):
        """
            This function is the code for the whole game.
        """
        # creates pieces of both white and black color
        self.create_pieces(WHITE_COLOR)
        self.create_pieces(BLACK_COLOR)

        # finds the starting and ending squares
        self.find_starting_squares()
        self.find_ending_squares()

        # user input for names
        self.name_player_one = input("What is your name? ")
        print('{} you will play as white'.format(self.name_player_one))
        self.name_player_two = input("What is you name? ")
        print('{} you will play as black. '.format(self.name_player_two))

        # loops through turns
        while not self.win_condition:
            self.display_board()
            white_roll = self.roll_d4_dice()
            if white_roll != 0:
                self.white_turn(white_roll)
            else:
                print("{} rolled a zero. ".format(self.name_player_one))

            if self.win_condition is False:
                self.display_board()
                black_roll = self.roll_d4_dice()
                if black_roll != 0:
                    self.black_turn(black_roll)
                else:
                    print("{} rolled a zero. ".format(self.name_player_two))

        if len(self.completed_white_pieces) == STARTING_PIECES:
            print("{} has won the game!!".format(self.name_player_one))

        if len(self.completed_black_pieces) == STARTING_PIECES:
            print("{} has won the game! ".format(self.name_player_two))

    def find_starting_squares(self):
        """
                This function finds the starting squares in self.board and sets the starting square variables
                to a board square.
        """
        # loops through to find specific board squares
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                # checks for starting white
                if self.board[i][j].entrance == WHITE_COLOR:
                    self.starting_white = self.board[i][j]
                    for each in self.white_pieces:
                        each.starting_white = self.board[i][j]

                # checks for starting black
                if self.board[i][j].entrance == BLACK_COLOR:
                    self.starting_black = self.board[i][j]
                    for each in self.black_pieces:
                        each.starting_black = self.board[i][j]

    def find_ending_squares(self):
        """
                This function finds the ending squares for both black and white pieces.
        """
        # loops through to find specific board squares
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                # checks for ending white
                if self.board[i][j].exit == WHITE_COLOR:
                    self.ending_white = self.board[i][j]
                    for each in self.white_pieces:
                        each.ending_white = self.board[i][j]

                # checks for ending black
                if self.board[i][j].exit == BLACK_COLOR:
                    self.ending_black = self.board[i][j]
                    for each in self.black_pieces:
                        each.ending_black = self.board[i][j]

    def create_pieces(self, color):
        """
                This function creates the pieces for the game and puts them in a list.

                :param color: the color of the piece you want to make. In this case either black or white.
                :return
        """
        if color == BLACK_COLOR:
            piece_number = 1
            while piece_number != (STARTING_PIECES + 1):
                black_piece = UrPiece(BLACK_COLOR, BLACK_SYMBOL + str(piece_number))
                self.black_pieces.append(black_piece)
                piece_number += 1

        if color == WHITE_COLOR:
            piece_number = 1
            while piece_number != (STARTING_PIECES + 1):
                white_piece = UrPiece(WHITE_COLOR, WHITE_SYMBOL + str(piece_number))
                self.white_pieces.append(white_piece)
                piece_number += 1

    def display_options(self, pieces_list, number_moves):
        """
                This function takes the number of moves for the can_move function then displays all the possible
                options the player can make. It also puts those options as a key to their piece in a dictionary.

                :param pieces_list: list of all non-completed pieces.
                :param number_moves: The number of the roll for the player at that turn.
                :return: The dictionary of options.
        """
        empty_dictionary = {}
        for piece in range(len(pieces_list)):

            # checks if pieces are off the board and displays if possible to move
            if pieces_list[piece].position is None:
                if pieces_list[piece].can_move(number_moves):
                    print(piece + 1, pieces_list[piece].symbol, OFF_BOARD_STATEMENT)
                    empty_dictionary[int(piece + 1)] = pieces_list[piece]

            # checks if pieces are on the board and displays if possible to move
            elif pieces_list[piece].position is not None:
                if pieces_list[piece].can_move(number_moves):
                    print(piece + 1, pieces_list[piece].symbol, pieces_list[piece].position.position)
                    empty_dictionary[int(piece + 1)] = pieces_list[piece]
        return empty_dictionary

    def choose_option(self, dictionary_of_options):
        """
                This function asks the user what to do and returns a piece to move

                :param dictionary_of_options: A dictionary of options with the pieces.
                :return The piece the user wants to move.
        """
        loop_trigger = 0

        # This while loop will keep on asking for user input until the input is one of the possible options.
        while loop_trigger == 0:
            user_choice = input("What would you like to do? ")
            if int("".join(user_choice.split())) in dictionary_of_options:
                for each in dictionary_of_options:
                    if each == int("".join(user_choice.split())):
                        return dictionary_of_options[each]
            else:
                print("That is not a viable option. ")

    def move_piece(self, piece_to_move, number_steps):
        """
                This function moves a piece the amount of steps it is given.

                :param piece_to_move: The specific piece to move
                :param number_steps: The number of steps the piece wants to go
                :return The piece at its new location.
        """
        # moving section for white pieces:
        move_number = number_steps
        if piece_to_move.color == WHITE_COLOR:
            location = piece_to_move.position

            # "if the piece is off the board" situation checks
            if piece_to_move.position is None:
                move_number -= 1
                location = piece_to_move.starting_white
            else:
                if piece_to_move.position != self.ending_white:
                    # erases the piece on its original square so the square will be blank after the piece moves.
                    piece_to_move.position.piece = None

            if move_number == 0:
                piece_to_move.position = location
                piece_to_move.starting_white.piece = piece_to_move

            else:
                # moving loop to find final destination board square.
                while move_number != 0:
                    location = location.next_white
                    if location is None and move_number == 1:
                        piece_to_move.complete = True
                    if location == piece_to_move.ending_white and move_number == 2:
                        piece_to_move.complete = True
                    move_number -= 1

            # checks if the piece is completed or not
            if not self.completed_check(piece_to_move, self.white_pieces, self.completed_white_pieces):
                piece_to_move.position = location
                if piece_to_move.position is not None:

                    if piece_to_move.position.piece is not None:
                        if piece_to_move.position.piece.color != piece_to_move.color:
                            piece_to_move.position.piece.position = None
                            piece_to_move.position.piece = piece_to_move

                    else:
                        piece_to_move.position.piece = piece_to_move
                else:
                    piece_to_move.position.piece = piece_to_move
            else:
                piece_to_move.position.piece = None
                # piece_to_move.position = None
                print("{}\n{} has made it to the goal!\n{}".format(LINE_OF_QUOTES, piece_to_move.symbol, LINE_OF_QUOTES))
                return None

        # Moving section for black pieces (same code but color variables switched):
        if piece_to_move.color == BLACK_COLOR:
            location = piece_to_move.position
            if piece_to_move.position is None:
                move_number -= 1
                location = piece_to_move.starting_black
            else:
                if piece_to_move.position != self.ending_black:
                    piece_to_move.position.piece = None

            if move_number == 0:
                piece_to_move.position = location
                piece_to_move.starting_black.piece = piece_to_move

            else:
                while move_number != 0:
                    location = location.next_black
                    if location is None and move_number == 1:
                        piece_to_move.complete = True
                    if location == piece_to_move.ending_black and move_number == 2:
                        piece_to_move.complete = True
                    move_number -= 1

            # checks if the piece is completed if it lands there.
            if not self.completed_check(piece_to_move, self.black_pieces, self.completed_black_pieces):
                piece_to_move.position = location
                if piece_to_move.position is not None:

                    if piece_to_move.position.piece is not None:
                        if piece_to_move.position.piece.color != piece_to_move.color:
                            piece_to_move.position.piece.position = None
                            piece_to_move.position.piece = piece_to_move

                    else:
                        piece_to_move.position.piece = piece_to_move
            else:
                piece_to_move.position.piece = None
                print("{}\n{} has made it to the goal!\n{}".format(LINE_OF_QUOTES, piece_to_move.symbol, LINE_OF_QUOTES))
                return None

        return piece_to_move

    def black_turn(self, roll_number):
        """
            This function does everything for a black player's turn.

            :param roll_number: the number of moves
            :return
        """
        print("You rolled", roll_number)
        black_options_dictionary = self.display_options(self.black_pieces, roll_number)

        # checks if you have options or not
        if len(black_options_dictionary) != 0:
            black_choice_piece = self.choose_option(black_options_dictionary)
            moved_piece = self.move_piece(black_choice_piece, roll_number)
            self.rosette_turn(moved_piece)
            self.winning_check(self.completed_black_pieces)
        else:
            print(NO_OPTION_STRING)

    def white_turn(self, roll_number):
        """
            This function does everything for a white player's turn.

            :param roll_number: the number of moves
            :return
        """
        print("You rolled", roll_number)
        white_options_dictionary = self.display_options(self.white_pieces, roll_number)

        # checks if you have options or not
        if len(white_options_dictionary) != 0:
            white_choice_piece = self.choose_option(white_options_dictionary)
            moved_piece = self.move_piece(white_choice_piece, roll_number)
            self.rosette_turn(moved_piece)
            self.winning_check(self.completed_white_pieces)
        else:
            print(NO_OPTION_STRING)

    def completed_check(self, piece, list_of_pieces, list_of_completed):
        """
            This function checks if a piece is comleted if it is takes it out of a list and puts it in a different one.

            :param piece: the piece that you are checking
            :param list_of_pieces: the list you are taking the piece out of
            :param list_of_completed: the list you are putting the piece into.
            :return True or False
        """
        if not piece.complete:
            return False

        if piece.complete:
            list_of_pieces.remove(piece)
            list_of_completed.append(piece)
            return True

    def rosette_turn(self, piece):
        """
            This function does everything for a white player's turn. Again because it is a rosette square.

            :param piece: the number of moves
            :return
        """
        if piece is not None:
            if piece.position is not None:

                # same format as white turn
                if piece.color == WHITE_COLOR:
                    if piece.position.rosette:
                        print("You landed on a Rosette. Go again.")
                        number_roll = self.roll_d4_dice()
                        self.display_board()
                        if number_roll != 0:
                            self.white_turn(number_roll)
                        else:
                            print("{} rolled a zero".format(self.name_player_one))

                # same format as black turn
                if piece.color == BLACK_COLOR:
                    if piece.position.rosette:
                        print("You landed on a Rosette. Go again.")
                        number_roll = self.roll_d4_dice()
                        self.display_board()
                        if number_roll != 0:
                            self.black_turn(number_roll)
                        else:
                            print("{} rolled a zero".format(self.name_player_two))

    def winning_check(self, list_completed_pieces):
        """
            This function checks if someone has won yet.

            :param list_completed_pieces: the number of moves
            :return
        """
        if len(list_completed_pieces) == STARTING_PIECES:
            self.win_condition = True


if __name__ == '__main__':
    file_name = input('What is the file name of the board json? ') if len(argv) < 2 else argv[1]
    rgu = RoyalGameOfUr(file_name)
    rgu.play_game()
