import sys

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
class Piece:
    def __init__(self, type):
        self.type = type

    def get_blocked_positions(self, row_char, col_char, board):
        blocked = set()
        row = int(row_char)
        col = get_col_int(col_char)
        if self.type == "King":
            blocked = blocked.union(self.get_king_movements(row, col, board))
        if self.type == "Queen":
            blocked = blocked.union(self.get_queen_movements(row, col, board))
        if self.type == "Bishop":
            blocked = blocked.union(self.get_bishop_movements(row, col, board))
        if self.type == "Rook":
            blocked = blocked.union(self.get_rook_movements(row, col, board))
        if self.type == "Knight":
            blocked = blocked.union(self.get_knight_movements(row, col, board))
        return blocked

    def get_king_movements(self, row_int, col_int, board):
        return self.get_king_movements_list(row_int, col_int, board)

    def get_king_movements_list(self, row_int, col_int, board):
        rows = board.height
        cols = board.width
        moves = list()
        i = row_int - 1
        while i < row_int + 2:
            j = col_int - 1
            while j < col_int + 2:
                if i >= 0 and i < rows and j >= 0 and j < cols:
                    position = get_position_tuple(get_col_char(j), i)
                    if board.able_to_move_to(position) and (not (i == row_int and j == col_int)):
                        moves.append(position)
                j += 1
            i += 1
        return moves

    def get_queen_movements(self, row_int, col_int, board):
        moves = self.get_bishop_movements(row_int, col_int, board)
        moves = moves.union(self.get_rook_movements(row_int, col_int, board))
        return moves

    def get_bishop_movements(self, row_int, col_int, board):
        rows = board.height
        cols = board.width
        moves = set()
        i = row_int
        j = col_int
        count = 0
        plus_stop = False
        minus_stop = False
        self_pos = get_position_tuple(get_col_char(col_int), row_int)
        while i >= 0:
            if j + count < cols and (plus_stop == False):
                pos = get_position_tuple(get_col_char(j + count), i)
                if not board.able_to_move_to(pos):
                    if not(i == row_int and j == col_int):
                        plus_stop = True
                else:
                    if self_pos != pos:
                        moves.add(pos)
            if j - count >= 0 and (minus_stop == False):
                pos = get_position_tuple(get_col_char(j - count), i)
                if not board.able_to_move_to(pos):
                    if not(i == row_int and j == col_int):
                        minus_stop = True
                else:
                    if self_pos != pos:
                        moves.add(pos)
            i -= 1
            count += 1
        i = row_int
        count = 0
        plus_stop = False
        minus_stop = False
        while i < rows:
            if j + count < cols and (plus_stop == False):
                pos = get_position_tuple(get_col_char(j + count), i)
                if not board.able_to_move_to(pos):
                    if not(i == row_int and j == col_int):
                        plus_stop = True
                else:
                    if self_pos != pos:
                        moves.add(pos)
            if j - count >= 0 and (minus_stop == False):
                pos = get_position_tuple(get_col_char(j - count), i)
                if not board.able_to_move_to(pos):
                    if not(i == row_int and j == col_int):
                        minus_stop = True
                else:
                    if self_pos != pos:
                        moves.add(pos)
            i += 1
            count += 1
        return moves

    def get_rook_movements(self, row_int, col_int, board):
        rows = board.height
        cols = board.width
        moves = set()
        for i in range(row_int + 1, rows):
            pos = get_position_tuple(get_col_char(col_int), i)
            if not board.able_to_move_to(pos):
                break
            moves.add(pos)
        i = row_int - 1
        while i >= 0:
            pos = get_position_tuple(get_col_char(col_int), i)
            if not board.able_to_move_to(pos):
                break
            moves.add(pos)
            i -= 1
        for j in range(col_int + 1, cols):
            pos = get_position_tuple(get_col_char(j), row_int)
            if not board.able_to_move_to(pos):
                break
            moves.add(pos)
        j = col_int - 1
        while j >= 0:
            pos = get_position_tuple(get_col_char(j), row_int)
            if not board.able_to_move_to(pos):
                break
            moves.add(pos)
            j -= 1
        return moves

    def get_knight_movements(self, row_int, col_int, board):
        rows = board.height
        cols = board.width
        moves = set()
        if (col_int - 1 >= 0):
            if (row_int + 2 < rows):
                pos = get_position_tuple(get_col_char(col_int - 1), row_int + 2)
                moves.add(pos)
            if (row_int - 2 >= 0):
                pos = get_position_tuple(get_col_char(col_int - 1), row_int - 2)
                moves.add(pos)
        if (col_int - 2 >= 0):
            if (row_int + 1 < rows):
                pos = get_position_tuple(get_col_char(col_int - 2), row_int + 1)
                moves.add(pos)
            if (row_int - 1 >= 0):
                pos = get_position_tuple(get_col_char(col_int - 2), row_int - 1)
                moves.add(pos)
        if (col_int + 1 < cols):
            if (row_int + 2 < rows):
                pos = get_position_tuple(get_col_char(col_int + 1), row_int + 2)
                moves.add(pos)
            if (row_int - 2 >= 0):
                pos = get_position_tuple(get_col_char(col_int + 1), row_int - 2)
                moves.add(pos)
        if (col_int + 2 < cols):
            if (row_int + 1 < rows):
                pos = get_position_tuple(get_col_char(col_int + 2), row_int + 1)
                moves.add(pos)
            if (row_int - 1 >= 0):
                pos = get_position_tuple(get_col_char(col_int + 2), row_int - 1)
                moves.add(pos)
        return moves

    def to_string(self):
        length = len(self.type)
        string_form = self.type
        while (length < 8):
            string_form += " "
            length += 1
        return string_form

class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.piece = None
        self.blocked = 0

    def get_row_as_int(self):
        return self.row

    def get_col_as_int(self):
        return ord(self.col) - 97

    def get_location(self):
        return get_position_tuple(self.col, self.row)

    def set_piece(self, piece):
        if self.piece == None:
            self.piece = piece

    def set_blocked(self):
        self.blocked += 1

    def to_string(self):
        if self.piece != None:
            return "[" + self.piece.to_string() + "]"
        return "[        ]"

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # create an empty board of size width * height that does not contain pieces
        self.grids = []
        for row in range(height):
            row_array = []
            for col in range(width):
                row_array.append(Grid(row, get_col_char(col)))
            self.grids.append(row_array)

    def get_grid(self, location):
        row = int(location[1])
        col = get_col_int(location[0])
        return self.grids[row][col]

    def set_piece(self, piece, row_char, col_char):
        row = int(row_char)
        col = get_col_int(col_char)
        self.grids[row][col].set_piece(piece)

    def set_block(self, location):
        self.get_grid(location).set_blocked()

    def is_occupied_at(self, row_int, col_int):
        return not (self.grids[row_int][col_int].piece is None)

    def has_piece(self, location):
        grid = self.get_grid(location)
        return grid.piece != None and grid.piece.type != "Obstacle"

    def able_to_move_to(self, location):
        grid = self.get_grid(location)
        return grid.piece == None or grid.piece.type != "Obstacle"

    def get_value(self):
        # calculate number of threatened pieces
        count = 0
        for row in self.grids:
            for grid in row:
                if grid.piece != None and grid.piece.type != "Obstacle":
                    count += grid.blocked
        return count

    def get_number_of_pieces(self):
        count = 0
        for row in self.grids:
            for grid in row:
                if grid.piece != None and grid.piece.type != "Obstacle":
                    count += 1
        return count

    def to_string(self):
        string = ""
        for row in self.grids:
            for grid in row:
                string += grid.to_string() + " "
            string += "\n"
        return string

class State:
    pass

def get_col_int(col_char):
    return ord(col_char) - 97

def get_col_char(col_int):
    return chr(col_int + 97)

def get_position_string(col_char, row):
    return col_char + str(row)

def get_position_tuple(col_char, row):
    return (col_char, int(row))

def get_empty_board(width, height, num_of_obstacles, obstacles):
    board = Board(width, height)
    # Add obstacles
    if num_of_obstacles > 0:
        for obstacle in obstacles:
            board.set_piece(Piece("Obstacle"), obstacle[1:], obstacle[0])
    return board

def search():
    pass


### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_CSP():
    # You can code in here but you cannot remove this function or change the return type
    testfile = sys.argv[1] #Do not remove. This is your input testfile.
    input_file = open(testfile, "r")
    lines = input_file.readlines()
    rows = int(lines[0].split(":")[-1])
    cols = int(lines[1].split(":")[-1])
    num_of_obstacles = int(lines[2].split(":")[-1])
    # list of positions of the obstacles
    obstacles = lines[3].split(":")[-1].split()
    piece_types = lines[4][10:43].split(", ")
    piece_counts = lines[4][60:-1].split(" ")
    pieces = dict()
    for i in range(5):
        pieces[piece_types[i]] = int(piece_counts[i])

    goalState = search()
    return goalState #Format to be returned

print(run_CSP())