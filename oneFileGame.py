"""
TODO:
1. convert this into a OOP code
2. make a generic version
"""

player1 = "O"
player2 = "X"
board = [None] * 9
diagonals = [[0, 4, 8], [2, 4, 6]]
rows = [[0,1,2], [3,4,5], [6,7,8]]
columns = [[0,3,6], [1,4,7], [2,5,8]]

def printBoard(b):
    for cell in range(len(b)):
        if (cell+1)%3 == 0:
            print(b[cell], end="\n")
        else:
            print(b[cell], end="\t")
    print("", end='\n')

def checkDiagonal(b, symbol):
    for diagonal in diagonals:
        count = 0
        for cell in diagonal:
            if b[cell] == symbol:
                count+=1
        if count == 3:
            return True
    return False

def checkHorizontal(b, symbol):
    for row in rows:
        count = 0
        for cell in row:
            if b[cell] == symbol:
                count+=1
        if count == 3:
            return True
    return False


def checkVertical(b, symbol):
    for col in columns:
        count = 0
        for cell in col:
            if b[cell] == symbol:
                count+=1
        if count == 3:
            return True
    return False

def checkForWin(b, symbol):
    if checkHorizontal(b, symbol) or checkVertical(b, symbol) or checkDiagonal(b, symbol):
        print(currentPlayer + " wins")
        return True

def changePlayer(arg):
    if arg == "X":
        return "O"
    else:
        return "X"

end = False
p1 = "X"
p2 = "O"
currentPlayer = p1
while not end:
    loc = int(input("location: "))
    board[loc] = currentPlayer
    printBoard(board)
    if (None not in board or checkForWin(board, currentPlayer)):
        end = True
    currentPlayer = changePlayer(currentPlayer)

print("Game ends", end='\n')
printBoard(board)
