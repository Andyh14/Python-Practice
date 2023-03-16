"""
File:    board_square.py
Author:  Andy Huang
Date:    11/11/2020
Section: 46
E-mail:  Andyh1@umbc.edu
Description:
  This program creates classes UrPiece and BoardSquare that is used for the royal game of ur program.
"""


class UrPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol
        self.starting_white = None
        self.starting_black = None
        self.ending_white = None
        self.ending_black = None

    def can_move(self, num_moves):
        """
                This function checks if the piece can move a number of spaces on the board.

                :param num_moves: The number of steps a piece would take.
                :return
                """
        # Check if starting move is possible for landing on the starting square.
        if num_moves == 1 and self.position is None:
            if self.color == "White" and self.starting_white.piece is None:
                return True

            if self.color == "Black" and self.starting_black.piece is None:
                return True

            elif self.color == "White" and self.starting_white.piece is not None:
                return False

            elif self.color == "Black" and self.starting_black.piece is not None:
                return False

        location = self.position

        # changes for starting move that doesn't land on the starting square.
        if location is None and self.color == "Black":
            num_moves -= 1
            location = self.starting_black
        if location is None and self.color == "White":
            num_moves -= 1
            location = self.starting_white

        if num_moves > 0:
            # checks if the piece is on the ending square and if it has a roll of 1 which would make it complete.
            if location == self.ending_white or location == self.ending_black:
                if num_moves == 1:
                    # self.complete = True
                    return True

            steps = num_moves

            # moves the location of checking to the square you want to check
            while steps != 0:

                # checks possibility of landing one past the exit square and if so piece can move
                if self.color == "White":
                    if location is not None:
                        location = location.next_white
                        if location == self.ending_white and location.piece is None:
                            if steps == 1:
                                return True
                        elif location == self.ending_white:
                            if steps == 2:
                                return True
                            else:
                                return False
                    else:
                        return False

                if self.color == "Black":
                    if location is not None:
                        location = location.next_black
                        if location == self.ending_black and location.piece is None:
                            if steps == 1:
                                return True
                        elif location == self.ending_black:
                            if steps == 2:
                                return True
                            else:
                                return False
                    else:
                        return False
                steps -= 1

            # makes sure that if there's a piece on a rosette you cannot go on there.
            if location is not None:
                if location.rosette is True:
                    if location.piece is not None and location.piece.symbol != self.symbol:
                        return False
                    else:
                        return True

                # checks if there's a piece on the landing square and if it's the same color.
                elif location.piece is not None:
                    if location.piece.color == self.color:
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True


class BoardSquare:
    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit, 'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}
