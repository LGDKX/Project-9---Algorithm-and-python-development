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


def display():
    for line in board:
        print(line)


def verification():
    boardCopy = board
    for i in range(y):
        for j in range(x):
            if y > 0:
                total1 = board[x][y - 1] + board[x - 1][y - 1] + board[x + 1][y - 1]
            if x > 0:
                total2 = board[x - 1][y - 1] + board[x - 1][y + 1] + board[x - 1][y]
            if y < len(board):
                total3 = 1
            if x < len(board[i]):
                total4 = 1
            total1 = board[x][y - 1] + board[x][y + 1] + board[x - 1][y - 1] + board[x - 1][y + 1]
            total2 = board[x - 1][y] + board[x - 1][y] + board[x + 1][y - 1] + board[x + 1][y + 1]
            total = total1 + total2 + total3 + total4
            if total > 3 or total < 2:
                boardCopy[i][j] = 0
            elif total == 3:
                boardCopy[i][j] = 1
            else:
                boardCopy[i][j] = boardCopy[i][j]
    boardCopy = board

verification()
display()
