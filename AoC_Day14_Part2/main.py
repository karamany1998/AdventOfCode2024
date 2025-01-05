from collections import defaultdict
import time


pos_vals = []
vel_vals = []
matrix = []

def makeMatrix():
    mat = []
    for i in range(0, 103):
        currRow = []
        for j in range(0, 101):
            currRow.append('-')
        mat.append(currRow)
    return mat


def printMatrix(matrix):
    with open("output.txt", "a") as f:

        for row in matrix:
            print(row , file = f)
        print('=========================================================================' , file=f)
        return


def main():



    matrix = makeMatrix()
    with open('input.txt') as file:
        positions = defaultdict(int)
        for line in file:
            currLine = line.strip().split(' ')
            position = currLine[0]
            velocity = currLine[1]

            posXY = position.strip().split(',')
            posX = int(posXY[0][2:])
            posY = int(posXY[1])

            velXY = velocity.strip().split(',')
            velX = int(velXY[0][2:])
            velY = int(velXY[1])

            pos_vals.append([posX, posY])
            vel_vals.append([velX, velY])

    idx =0
    for i in range(0, 10000):
       if(i > 7500):
           print('second ', idx)
           printMatrix(matrix)
           matrix = makeMatrix()

       idx+=1

       for j in range(0 , len(pos_vals)):
           pos1 = pos_vals[j][0]
           pos2 = pos_vals[j][1]

           vel1 = vel_vals[j][0]
           vel2 = vel_vals[j][1]

           pos1 = (pos1 + vel1)%101
           pos2 = (pos2 + vel2)%103

           matrix[pos2][pos1] = '#'







if __name__ == '__main__':
    main()