# This module is controls the board of the game

class Board:
    __board = []
    __diagonals = [[0, 4, 8], [2, 4, 6]]
    __rows = [[0,1,2], [3,4,5], [6,7,8]]
    __columns = [[0,3,6], [1,4,7], [2,5,8]]

    # Initialse board
    def __init__(self):
        self.__board = [None] * 9

    # Print current state of the board
    def printBoard(self):
        for cell in range(9):
            if (cell+1) % 3 == 0:
                print(self.__board[cell])
            else:
                print(self.__board[cell], end=" | ")

    def putSymbol(self, cell, symbol):
        self.__board[cell-1] = symbol
