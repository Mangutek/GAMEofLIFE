import os
import time
import numpy as np
text = open("data.txt").readlines()    #your starting positions
# input is bulid from '.' as dead cells and 'X' as alive ones
#for example  
#    ....................
#    ....................
#    ....................
#    ....................
#    .......X.XX.........
#    .......XXX..........
#    ........X...........
#    ....................
#    ....................
#    ....................
#    ....................
 #   ....................
data = []

for line in text: data.append([])
for y in range(len(tekst)):
    for x in range(len(tekst[0])-1):
        data[y].append(tekst[y][x])

def copymatrix(new, old):
    for z in range(len(old)):
        new.append([])
    for y in range(len(old)):
        for x in range(len(old[y])):
             new[y].append(old[y][x])
def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""

def game_of_life(dane):
    tab = []
    tab.clear()
    copymatrix(tab, dane)
    for y in range(len(dane)):
        for x in range(len(dane[y])):
            ile = 0
            try:
                if dane[y-1][x-1] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y-1][x] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y-1][x+1] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y][x-1] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y][x+1] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y+1][x-1] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y+1][x] == 'X': ile=ile+1
            except:
                pass
            try:
                if dane[y+1][x+1] == 'X': ile=ile+1
            except:
                pass
            if dane[y][x] == 'X' and (ile == 2 or ile == 3):
                tab[y][x] = 'X'
            elif dane[y][x] == '.' and ile == 3:
                tab[y][x] = 'X'
            else:
                tab[y][x] = '.'
    return tab

for i in range(100):  #number of generations
    print(i)
    printmatrix(data)
    data = game_of_life(data)
    time.sleep(0.5)
    os.system('cls')




    
            
        
