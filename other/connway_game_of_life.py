'''Programm beginning'''
from random import randint

x = 3
y = 3

board = []
for line in range(x):
    lineContent = []
    for col in range(y):
        lineContent.append((randint(0,1)))
    board.append(lineContent)
    
boardCopy = board
for i in range(y):
    for j in range(x):
        if y > 0:
            if x > 0:
                subTotal1 = board[x - 1][y - 1] + board[x][y - 1] + board[x - 1][y]
            if x < len(board[i]):
                subTotal2 = board[x][y - 1] + board[x + 1][y - 1] + board[x + 1][y]
        if y < len(board):
            if x > 0:
                subTotal3 = board[x - 1][y] + board[x - 1][y + 1] + board[x][y + 1]
            if x < len(board[i]):
                subTotal4 = board[x + 1][y] + board[x + 1][y + 1] + board[x][y + 1]
        if y == 1 and x == 1:
            subTotal5 = - board[x][y - 1] - board[x - 1][y] - board[x + 1][y] - board[y + 1][x]
        if y == 0 and x == 1:
            subTotal6 = - board[x][y - 1]
        if y == len(board) and x == 1:
            subTotal7 = - board[x][y + 1]
        total = subTotal1 + subTotal2 + subTotal3 + subTotal4 + subTotal5 + subTotal6 + subTotal7

        if total > 3 or total < 2:
            boardCopy[i][j] = 0
        elif total == 3:
            boardCopy[i][j] = 1
        else:
            boardCopy[i][j] = boardCopy[i][j]
    boardCopy = board
    for line in board:
        print(line)
