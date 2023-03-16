
class UrPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol
        self.possible_moves = []
        self.starting_white = ''
        self.ending_white = None
        self.off_board = False

    def can_move(self, num_moves):

        # off_board will only be true if its off the board
        if self.off_board == False:
            if self.starting_white == self.ending_white:
                self.off_board = True
                return True
            else:
                # finds the boardsquare info at the spot you want to check using a list.
                index_number = (num_moves - 1) % len(self.possible_moves)
                bs_info = self.possible_moves[index_number]

            # piece color and rosette checks
            if bs_info.piece != None:
                if bs_info.rosette == False:
                    if bs_info.piece.color == self.color:
                        return False
                    if bs_info.piece.color != self.color:
                        return True
                    elif bs_info == self.ending_white:
                        return False
                else:
                    return False
            else:
                return True
        else:
            return False
        pass

    # assigns the start of the piece
    def white_starts(self, beginning_board_square):
        self.position = beginning_board_square


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



