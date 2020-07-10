# This module is controls the board of the game

class Board:
  __board = []

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
