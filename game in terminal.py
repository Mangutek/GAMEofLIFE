import os, time
############################################
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
#..........................................#
############################################
text = open("C:\\Users\\Admin\\Desktop\\GAMEOFLIFE\\map.txt").readlines()
data = []
mapa = []
pos = [3, 5]
def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""

for line in text:
    data.append(line.strip())
for line in data:
    mapa.append([])
for y in range(len(data)):
    for x in range(len(data[y])):
        mapa[y].append(data[y][x])
print(data)
mapa[pos[0]][pos[1]] = '^'
printmatrix(mapa)

def ruch(input, pos, mapa):
    if input == 'w':
        if mapa[pos[0]-1][pos[1]] == '#': pass
        else:
            mapa[pos[0]][pos[1]] = '.'
            pos[0] += -1
            mapa[pos[0]][pos[1]] = '^'
    elif input == 's':
        if mapa[pos[0]+1][pos[1]] == '#': pass
        else:
            mapa[pos[0]][pos[1]] = '.'
            pos[0] += 1
            mapa[pos[0]][pos[1]] = '*'

    elif input == 'a':
        if mapa[pos[0]][pos[1]-1] == '#': pass
        else:
            mapa[pos[0]][pos[1]] = '.'
            pos[1] += -1
            mapa[pos[0]][pos[1]] = '<'

    elif input == 'd':
        if mapa[pos[0]][pos[1]+1] == '#': pass
        else:
            mapa[pos[0]][pos[1]] = '.'
            pos[1] += 1
            mapa[pos[0]][pos[1]] = '>'
    else:
        pass
    return pos, mapa

while True:
    printmatrix(mapa)
    pos, mapa = ruch(input(), pos, mapa)
    time.sleep(0.1)
    os.system('cls')
    print(input)
