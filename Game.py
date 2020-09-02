# This module controls how the game works

from Player import Player
from Board import Board
class Game:
    # Declare player
    # TODO: Check how to declare player1 and player2 of type Player and board of type board
    __player1 = ""
    __player2 = ""
    __board = []
    __current_player = ""

    # Initialise game
    def __init__(self):
        # Assign symbols to player and initialse player and board
        self.__player1 = Player("X")
        self.__player2 = Player("O")
        self.__board = Board()
        self.__current_player = self.__player1
    def currentPlayer(self):
        return self.__current_player.printPlayer()

    def start(self):
        print(currentPlayer+": ")

    def getSymbol():
        input
