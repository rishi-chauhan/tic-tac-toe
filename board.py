"""
Module to control board
"""

DIAGONALS = [[0, 4, 8], [2, 4, 6]]
ROWS = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
COLUMNS = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

def print_board(board):
    """Prints the board"""
    for index, cell in enumerate(board):
        if (index+1)%3 == 0:
            print(cell, end="\n")
        else:
            print(cell, end="\t")
    print("", end='\n')


def check_diagonal(board, symbol):
    """checks diagonals for win"""
    for diagonal in DIAGONALS:
        count = 0
        for cell in diagonal:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_rows(board, symbol):
    """checks horizontals for win"""
    for row in ROWS:
        count = 0
        for cell in row:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_columns(board, symbol):
    """checks vertical for win"""
    for col in COLUMNS:
        count = 0
        for cell in col:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_for_win(board, symbol, current_player):
    """checks if someone won"""
    if check_rows(board, symbol) or check_columns(board, symbol) or check_diagonal(board, symbol):
        print(current_player + " wins")
        return True
    return False
