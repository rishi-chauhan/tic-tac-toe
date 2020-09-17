"""Module to control player"""

def generate_player(symbol):
    """generates player"""
    return symbol

def change_player(current_player):
    """changes current player"""
    if current_player == "X":
        return "O"
    return "X"
