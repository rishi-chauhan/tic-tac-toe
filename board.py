"""
Module to control board
"""

# CELL_ARRAY_SETS = [DIAGONALS, ROWS, COLS]
CELL_ARRAY_SETS = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

def print_board(board):
    """Prints the board"""
    for index, cell in enumerate(board):
        if (index+1)%3 == 0:
            print(cell, end="\n")
        else:
            print(cell, end="\t")
    print("", end='\n')

def check_for_win(board, symbol):
    """checks if someone won"""
    for cell_arr in CELL_ARRAY_SETS:
        if get_cell_array(board, cell_arr) == [symbol]*3:
            print(symbol + " wins")
            return True
    return False

def get_cell_array(board, index_arr):
    """returns an array of cell value where cell indexed are mentioned in index_arr"""
    return [board[cell] for cell in index_arr]
