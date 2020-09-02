# The main module

from Board import Board
from Game import Game
from Player import Player

player1 = Player("O")
player2 = Player("X")

board = Board()
game = Game()

board.printBoard()
