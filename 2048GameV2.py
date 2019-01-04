import random
import time
import numpy as  np

class _2048_:

    def __init__(self):
        self.moves = {"right": 0, "up": 1, "left": 2, "down": 3}
        self.nextMove = None
        self.highestNum = 2
        self.board = np.array([[0,0,0,0],
                               [0,0,0,0],
                               [0,0,0,0],
                               [0,0,0,0]])

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

    def moveEverythingToTheRight(self):
        for i in range(3):
            for row in range(4):
                for column in range(3 - i):
                    #move everything to the right
                    if self.board[row][column] != 0:
                        #if the next spot is empty: replace it
                        if self.board[row][column + 1] == 0:
                            self.board[row][column + 1] = self.board[row][column]
                            self.board[row][column] = 0

    def combineNumToTheRight(self):
        #form right to left
        for row in range(3,-1,-1):
            for column in range(3,0,-1):
                #combine
                if self.board[row][column] == self.board[row][column - 1]:
                    self.board[row][column] = self.board[row][column] * 2
                    self.board[row][column -1] = 0
                    if self.highestNum < self.board[row][column]:
                        self.highestNum = self.board[row][column]

    def moveRight(self):
        self.moveEverythingToTheRight()
        self.combineNumToTheRight()
        self.moveEverythingToTheRight()

    def move(self, to):
        if to == 0:
            self.moveRight()
        elif to == 1:
            self.board = np.rot90(self.board, 3)
            self.moveRight()
            self.board = np.rot90(self.board)
        elif to == 2:
            self.board = np.fliplr(self.board)
            self.moveRight()
            self.board = np.fliplr(self.board)
        elif to == 3:
            self.board = np.rot90(self.board)
            self.moveRight()
            self.board = np.rot90(self.board, 3)
        else:
            print("ERROR: to must beequl to 0/1/2/3 (0 := right; 1 := up; 2 := left; 3 := down)")
            print()

    def startGame(self):
        self.newNum()
        self.newNum()

    def randomPlay(self):
        self.nextMove = random.randint(0,3)
        self.move(self.nextMove)
        self.newNum()

data = [[],[]]
goal = 32
maxMoveCountToReachGoal = 20
gameSamples = 10000

startTimer = time.clock()
for j in range(gameSamples):
    b = _2048_()
    b.startGame()
    boardData = []
    moveData= []
    #boardData.append(b.board)
    for i in range(maxMoveCountToReachGoal):
        boardToAppend = b.board.tolist()
        boardData.append(np.array(boardToAppend))
        b.randomPlay()
        moveData.append(b.nextMove)
        if b.highestNum == goal:
            for k in range(i + 1):
                data[0].append(boardData[k])
                data[1].append(moveData[k])
            break
    if j % 1000 == 0 and j != 0:
        print(j)

stopTimer = time.clock()

print("Time: ", stopTimer - startTimer)
print("Total boards: ", len(data[0]))

