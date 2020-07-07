grid = {}
hasWon = False
circle = '\u2B24'
square = '\u2B1B'
turn = circle

def resetBoard(char):
    for y in range(1, 11):
        for x in range(1,11):
            grid[(x, y)] = char

def printBoard():
    for row in range(1,11):
        rowStr = ''
        for col in range(1,11):
            rowStr += grid[row,col] + ' '
        print(rowStr)

resetBoard('x')
grid[1,1] = circle
grid[2,2] = square
printBoard()
