
from time import sleep
import os
import sys
import random

labirint = [
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def show_labirint():
    for i in range(len(labirint)):
        for j in range(len(labirint[i])):
            print(labirint[i][j], end=' ')
        print()
    sleep(0.1)

def ai_move(x, y):
    #check exit
    if labirint[x][y-1] == 2 or labirint[x][y+1] == 2 or labirint[x-1][y] ==2 or labirint[x+1][y]==2:
        print("I found EXIT!")
        sys.exit()
    #0 - left, 1 - right
    #2 - up, 3 - down
    lst_move = []
    if labirint[x][y-1] == 0:
        lst_move.append("go_left")
    if labirint[x][y+1] == 0:
        lst_move.append("go_right")
    if labirint[x-1][y] == 0:
        lst_move.append("go_up")
    if labirint[x+1][y] == 0:
        lst_move.append("go_down")
    make_decision = random.choice(lst_move)
    labirint[x][y] = 0
    if make_decision == "go_left" :
        AI(x,y-1)
    if make_decision == "go_right" :
        AI(x,y+1)
    if make_decision == "go_up" :
        AI(x-1,y)
    if make_decision == "go_down" :
        AI(x+1,y)

def AI(pos_x, pos_y):
    os.system("cls")
    labirint[pos_x][pos_y] = "*"
    show_labirint()
    ai_move(pos_x, pos_y)

AI(5,3)



