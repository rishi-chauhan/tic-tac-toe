"""
TODO:
1. convert this into a OOP code
2. make a generic version
"""
import board
import player

BOARD = [None] * 9
PLAYER1 = player.generate_player("O")
PLAYER2 = player.generate_player("X")
END = False
CURRENT_PLAYER = PLAYER1

while not END:
    LOC = int(input("location: "))-1
    if not 0<=LOC<9:
        print("Invalid value. Please enter value between 1-9")
        continue
    if BOARD[LOC] is not None:
        print("The cell already has a value. Try again")
        continue
    BOARD[LOC] = CURRENT_PLAYER
    board.print_board(BOARD)
    if None not in BOARD or board.check_for_win(BOARD, CURRENT_PLAYER):
        END = True
    CURRENT_PLAYER = player.change_player(CURRENT_PLAYER)

print("Game ends", end='\n')
board.print_board(BOARD)
