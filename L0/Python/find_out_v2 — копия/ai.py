import labirint
import os
import random
import copy
import sys
from time import sleep

def ai_move(x, y):
    global labirint, move_history
    #check exit
    if labirint[x][y-1] == 2 or labirint[x][y+1] == 2 or labirint[x-1][y] ==2 or labirint[x+1][y]==2:
        print("I found EXIT!")
        sys.exit()

    #check where can we go!
    lst_move = []
    if labirint[x][y-1] == 0 and labirint[x][y-1] != "*":
        lst_move.append("go_left")
    if labirint[x][y+1] == 0 and labirint[x][y+1] != "*":
        lst_move.append("go_right")
    if labirint[x-1][y] == 0 and labirint[x-1][y] != "*":
        lst_move.append("go_up")
    if labirint[x+1][y] == 0 and labirint[x+1][y] != "*":
        lst_move.append("go_down")

    #check can we do a move and
    #if no,we'll finish the game or repeate again
    try: 
        make_decision = random.choice(lst_move)
    except:
        print("I'm lost or i was here")
        print(move_history)
        move_history = []
        sleep(5)
        #sys.exit()
        labirint = copy.deepcopy(labirint.labirint_source)
        AI(5,3)

    #make a move
    if make_decision == "go_left" :
        AI(x,y-1)
    if make_decision == "go_right" :
        AI(x,y+1)
    if make_decision == "go_up" :
        AI(x-1,y)
    if make_decision == "go_down" :
        AI(x+1,y)


def AI(pos_x, pos_y):
    global labirint, move_history
    os.system("cls")
    #labirint[pos_x][pos_y] = "*"
    labirint.show_labirint()
    move_history.append([pos_x, pos_y])
    ai_move(pos_x, pos_y)