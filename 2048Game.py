import random
import numpy as np
import time

# 0 := right; 1 := up; 2 := left; 3 := down
moves = [0,1,2,3]
gameData = [[],[]]
data = []
highestNum = 2

def newBoard():
    board = [[2,4,8,16],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    return np.array(board)

def printBoard(board):
    for i in range(4):
        print(board[i])
    print()

def newNum(board):
    #Get a free spot
    while True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if board[x][y] == 0:
            break
    #Add 2 (90%) or 4 (10%) at that spot
    if 0.9 < random.random():
        board[x][y] = 4
    else:
        board[x][y] = 2
    return board

def moveEverythingToTheRight(board):
    for i in range(3):
        for row in range(4):
            for column in range(3 - i):
                #move everything to the right
                if board[row][column] != 0:
                    #if the next spot is empty: replace it
                    if board[row][column + 1] == 0:
                        board[row][column + 1] = board[row][column]
                        board[row][column] = 0
    return board

def combineNumToTheRight(board):
    global highestNum
    #form right to left
    for row in range(3,-1,-1):
        for column in range(3,0,-1):
            #combine
            if board[row][column] == board[row][column - 1]:
                board[row][column] = board[row][column] * 2
                board[row][column -1] = 0
                if highestNum < board[row][column]:
                    highestNum = board[row][column]
    return board

def moveRight(board):
    board = moveEverythingToTheRight(board)
    board = combineNumToTheRight(board)
    board = moveEverythingToTheRight(board)
    return board

def move(board, to):
    if to == 0:
        board = moveRight(board)
    elif to == 1:
        board = np.rot90(board, 3)
        board = moveRight(board)
        board = np.rot90(board)
    elif to == 2:
        board = np.fliplr(board)
        board = moveRight(board)
        board = np.fliplr(board)
    elif to == 3:
        board = np.rot90(board)
        board = moveRight(board)
        board = np.rot90(board, 3)
    else:
        print("ERROR: to must beequl to 0/1/2/3 (0 := right; 1 := up; 2 := left; 3 := down)")
        print()
    return board

def startGame():
    board = newBoard()
    for i in range(2):
        newNum(board)
    return board

def isMovePossible(board, move):
    movePoss = True
    b = newBoard()
    b = move(board, move)
    if board == b:
        movePoss = False
    return movePoss

def noPossibleMove(board):
    noPossMove = False
    if np.min(board) != 0:
        possMoveCount = 0
        for i in range(4):
            if isMovePossible(board, i):
                possMoveCount += 1
        if possMoveCount == 0:
            noPossMove = True
    return noPossMove

def randomPlay(board):
    m = random.randint(0,3)
    board = move(board, m)
    board = newNum(board)
    return board , m

##startTimer =time.clock()
##stats = []
##for j in range(10000):
##    highestNum = 2
##    i = 0
##    b = startGame()
##    gameData = [[],[]]
##    for i in range(20):
##        b, m = randomPlay(b)
##        gameData[0].append(b)
##        gameData[1].append(m)
##        i += 1
##        if highestNum == 32:
##            data.append(gameData)
##            stats.append(i)
##            break
##    if j % 1000 == 0:
##        print(j)
##
##stopTimer = time.clock()
##print("Time: ", stopTimer - startTimer)
##print("Games who reached 32: ", len(stats))
##if len(stats) != 0:
##    print("Average move count: ", round(sum(stats) / len(stats), 2))




