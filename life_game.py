'''Programm beginn  ing'''
from random import randint
x = 3


board = []
for line in range(x):
    linecontent = []
    for col in range(x):
        linecontent.append((randint(0,1)))
    board.append(linecontent)

for line in board:
    print(line)
