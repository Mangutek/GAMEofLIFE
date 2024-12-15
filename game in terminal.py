import os, time
text = open("C:\\Users\\Admin\\Desktop\\GAMEOFLIFE\\map2.txt").readlines()
data = []
mapa = []
pos = [3, 5]
org = []
npc = {(1,1): 'dialog1',
       (11, 1): 'dialog2',
       (20, 1): 'dialog3',
       (23, 1): 'dialog4',
       (23, 12): 'dialog5',
       (23, 19): 'dialog6',
       (2, 21): 'dialog7'}

#########################
#&......#...........#...#
#.......#...........#&..#
#.......#...........#...#
######++#...........#...#
#.....;;;;;;;;;;;;;;+...#
#.....;;;;;;;;;;;;;;+...#
######;;............#...#
#....+;;............#...#
#....+;;............#...#
#....#;;............#####
#&...#;;................#
#....#.;................#
#....#;;................#
#....#;;................#
#....#;;................#
######;;................#
#.....;;;;;;;;;;;;;;;;;;#
#.....;;;;;;;;;;;;;;;;;;#
########;;########++#...#
#&.....#;;#.........#...#
#......#;;#.........#...#
#......+;;#.........#...#
#&.....+;;#.&......&#...#
#########################


def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""
def copymatrix(new, old):
    for z in range(len(old)):
        new.append([])
    for y in range(len(old)):
        for x in range(len(old[y])):
             new[y].append(old[y][x])

for line in text:
    data.append(line.strip())
for line in data:
    mapa.append([])
for y in range(len(data)):
    for x in range(len(data[y])):
        mapa[y].append(data[y][x])

copymatrix(org, mapa)
mapa[pos[0]][pos[1]] = '@'
printmatrix(mapa)

def ruch(input, pos, mapa, org):
    if input == 'w':
        if mapa[pos[0]-1][pos[1]] == '#': pass
        elif mapa[pos[0]-1][pos[1]] == '&':
            dialog(npc[(pos[0]-1, pos[1])])
        else:
            mapa[pos[0]][pos[1]] = org[pos[0]][pos[1]]
            pos[0] += -1
            mapa[pos[0]][pos[1]] = '@'
    elif input == 's':
        if mapa[pos[0]+1][pos[1]] == '#': pass
        elif mapa[pos[0]+1][pos[1]] == '&':
            dialog(npc[(pos[0]+1, pos[1])])
        else:
            mapa[pos[0]][pos[1]] = org[pos[0]][pos[1]]
            pos[0] += 1
            mapa[pos[0]][pos[1]] = '@'

    elif input == 'a':
        if mapa[pos[0]][pos[1]-1] == '#': pass
        elif mapa[pos[0]][pos[1]-1] == '&':
            dialog(npc[(pos[0], pos[1]-1)])
        else:
            mapa[pos[0]][pos[1]] = org[pos[0]][pos[1]]
            pos[1] += -1
            mapa[pos[0]][pos[1]] = '@'

    elif input == 'd':
        if mapa[pos[0]][pos[1]+1] == '#': pass
        elif mapa[pos[0]][pos[1]+1] == '&':
            dialog(npc[(pos[0], pos[1]+1)])
        else:
            mapa[pos[0]][pos[1]] = org[pos[0]][pos[1]]
            pos[1] += 1
            mapa[pos[0]][pos[1]] = '@'
    else:
        pass
    return pos, mapa

def dialog(index):
    if index == 'dialog1':
        for i in range(20):
            print("Witaj wędrowcze!")
            time.sleep(0.1)
            os.system('cls')
        for i in range(20):
            print("Czego poszukujesz w tym pięknym mieście?")
            time.sleep(0.1)
            os.system('cls')
        for i in range(20):
            print("Mamy tutaj wszystko, oprócz kobiet.")
            time.sleep(0.1)
            os.system('cls')
        

while True:
    time.sleep(0.1)
    os.system('cls')
    printmatrix(mapa)
    pos, mapa = ruch(input(), pos, mapa, org)
