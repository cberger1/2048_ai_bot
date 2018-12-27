import random
import time

gameData = [[],[]]
data = []

class _2048_:

    def __init__(self):
        self.moves = {"right": 0, "up": 1, "left": 2, "down": 3}
        self.highestNum = 2
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]

    def printBoard(self):
        for i in range(4):
            print(self.board[i])
        print()

    def newNum(self):
        #Get a free spot
        while True:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if self.board[x][y] == 0:
                break
        #Add 2 (90%) or 4 (10%) at that spot
        if 0.9 < random.random():
            self.board[x][y] = 4
        else:
            self.board[x][y] = 2

    def moveEveryNumTo(self, mv):
        nextElement = 1
        for i in range(3):
            columns = list(range(3 - i))
            if mv == 2:
                nextElement = -1
                columns = list(range(3, 0 + i, -1))
            for row in range(4):
                for column in columns:
                    #move everything to the right
                    if self.board[row][column] != 0:
                        #if the next spot is empty: replace it
                        if self.board[row][column + nextElement] == 0:
                            self.board[row][column + nextElement] = self.board[row][column]
                            self.board[row][column] = 0

    def moveEveryNumToUoD(self, mv):
            nextElement = 1
            for i in range(3):
                columns = list(range(3 - i))
                if mv == 3:
                    nextElement = -1
                    columns = list(range(3, 0 + i, -1))
                for row in range(4):
                    for column in columns:
                        #move everything to the right
                        if self.board[row][column] != 0:
                            #if the next spot is empty: replace it
                            if self.board[column + nextElement][row] == 0:
                                self.board[column + nextElement][row] = self.board[column][row]
                                self.board[column][row] = 0

    def combineNumTo(self, mv):
        columns = list(range(3))
        rows = list(range(4))
        nextElement = 1
        if mv == 0:
            columns.reverse()
            nextElement = -1

        for row in rows:
            for column in columns:
                #combine
                if self.board[row][column] == self.board[row][column + nextElement]:
                    self.board[row][column] = self.board[row][column] * 2
                    self.board[row][column + nextElement] = 0
                    if self.highestNum < self.board[row][column]:
                        self.highestNum = self.board[row][column]

    def combineNumToUoD(self, mv):
        columns = list(range(3))
        rows = list(range(4))
        nextElement = 1
        if mv == 1:
            columns.reverse()
            nextElement = -1

        for row in rows:
            for column in columns:
                #combine
                if self.board[column][row] == self.board[column + nextElement][row]:
                    self.board[column][row] = self.board[column][row] * 2
                    self.board[column + nextElement][row] = 0
                    if self.highestNum < self.board[column][row]:
                        self.highestNum = self.board[column][row]

    def move(self, to):
        if to == 0:
            self.moveEveryNumTo(to)
            self.combineNumTo(to)
            self.moveEveryNumTo(to)
        elif to == 1:
            self.moveEveryNumToUoD(to)
            self.combineNumToUoD(to)
            self.moveEveryNumToUoD(to)
        elif to == 2:
            self.moveEveryNumTo(to)
            self.combineNumTo(to)
            self.moveEveryNumTo(to)
        elif to == 3:
            self.moveEveryNumToUoD(to)
            self.combineNumToUoD(to)
            self.moveEveryNumToUoD(to)
        else:
            print("ERROR: to must beequl to 0/1/2/3 (0 := right; 1 := up; 2 := left; 3 := down)")
            print()

    def startGame(self):
        self.newNum()
        self.newNum()

##    def isMovePossible(board, m):
##        movePoss = True
##        nb = move(board, m)
##        if board.all() == nb.all():
##            movePoss = False
##        return movePoss
##
##    def noPossibleMove(board):
##        noPossMove = False
##        if np.min(board) != 0:
##            possMoveCount = 0
##            for i in range(4):
##                if isMovePossible(board, i):
##                    possMoveCount += 1
##            if possMoveCount == 0:
##                noPossMove = True
##        return noPossMove

    def randomPlay(self):
        self.move(2)
        self.newNum()

startTimer =time.clock()

for j in range(1):
    highestNum = 2
    b = _2048_()
    b.startGame()
    for i in range(20):
        b.randomPlay()
        b.printBoard()
        if highestNum == 32:
            break
    if j % 1000 == 0:
        print(j)

stopTimer = time.clock()

print("Time: ", stopTimer - startTimer)
#print("Games who reached 32: ", len(stats))
#if len(stats) != 0:
    #print("Average move count: ", round(sum(stats) / len(stats), 2))