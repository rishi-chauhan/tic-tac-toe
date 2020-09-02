# This module controls all the player related info

class Player:
    # Each player will have a symbol related to them which they'll
    # put on the board and they can choose their symbol
    __symbol = ""

    # Initialse player
    def __init__(self, symbol):
        self.__symbol = symbol

    # Print player related information
    def printPlayer(self):
        return "Player symbol: " + self.__symbol
