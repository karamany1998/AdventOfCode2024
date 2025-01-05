from collections import defaultdict
import math


def main():
    matrix = []
    positions = defaultdict(list)
    elements = set()
    obstaclePos = set()

    with open("input.txt") as file:
        for line in file:
            lst =[]
            for x in line:
                if x !='\n':
                    lst.append(x)
            matrix.append(lst)
    for i in range(0 , len(matrix)):
        for j in range(0 , len(matrix[0])):
            if matrix[i][j] != '.' and matrix[i][j] !='#':
                positions[matrix[i][j]].append([i,j])
                elements.add(matrix[i][j])
    row = len(matrix)
    col = len(matrix[0])
    tot = 0
    for ele in elements:
        posList = positions[ele]



        for i in range(0 , len(posList)):
            for j in range(i+1 , len(posList)):
                first = posList[i]
                second = posList[j]
                obstaclePos.add((first[0] , first[1]))
                obstaclePos.add((second[0], second[1]))

                print('first position is ' , first)
                print('second position is ' , second)

                diffX = first[0]-second[0]
                diffY = first[1]-second[1]
                diffX_2 = -1*diffX
                diffY_2 = -1*diffY

                print('direction 1 is ' +str(diffX)+ ' '+str(diffY))
                print('direction 2 is ' + str(diffX_2) + ' ' + str(diffY_2))

                newX = first[0] + diffX
                newY = first[1] + diffY

                print('first candidate is '+str(newX)+' '+str(newY))

                while newX< row and newX>=0 and newY < col and newY >=0:
                    obstaclePos.add((newX , newY))
                    newX += diffX
                    newY += diffY

                newX = second[0] + diffX_2
                newY = second[1] + diffY_2
                print('another candidate is ' +str(newX)+' '+str(newY))

                while newX < row and newX >= 0 and newY < col and newY >= 0:
                    obstaclePos.add((newX, newY))
                    newX += diffX_2
                    newY += diffY_2

    print(len(obstaclePos) + tot)
    print(obstaclePos)











if __name__=='__main__':
    main()