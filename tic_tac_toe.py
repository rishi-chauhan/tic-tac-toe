"""
TODO:
1. convert this into a OOP code
2. make a generic version
"""
PLAYER1 = "O"
PLAYER2 = "X"
BOARD = [None] * 9
DIAGONALS = [[0, 4, 8], [2, 4, 6]]
ROWS = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
COLUMNS = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
END = False
CURRENT_PLAYER = PLAYER1

def print_board(board):
    for index, cell in enumerate(board):
        if (index+1)%3 == 0:
            print(cell, end="\n")
        else:
            print(cell, end="\t")
    print("", end='\n')

def check_diagonal(board, symbol):
    for diagonal in DIAGONALS:
        count = 0
        for cell in diagonal:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_horizontal(board, symbol):
    for row in ROWS:
        count = 0
        for cell in row:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_vertical(board, symbol):
    for col in COLUMNS:
        count = 0
        for cell in col:
            if board[cell] == symbol:
                count += 1
        if count == 3:
            return True
    return False

def check_for_win(board, symbol):
    if check_horizontal(board, symbol) or check_vertical(board, symbol) or check_diagonal(board, symbol):
        print(CURRENT_PLAYER + " wins")
        return True
    return False

def change_player(arg):
    if arg == "X":
        return "O"
    return "X"

while not END:
    LOC = int(input("location: "))
    if BOARD[LOC] is not None:
        print("The cell already has a value. Try again")
        continue
    BOARD[LOC] = CURRENT_PLAYER
    print_board(BOARD)
    if None not in BOARD or check_for_win(BOARD, CURRENT_PLAYER):
        END = True
    CURRENT_PLAYER = change_player(CURRENT_PLAYER)

print("Game ends", end='\n')
print_board(BOARD)
