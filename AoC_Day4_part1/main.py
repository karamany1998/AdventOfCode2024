


def doesFit(i , j , row , col):
    if(i>= row or i<0 or j>= col or j<0):
        return False

    return True

dx = [0 , 0 , 1 , -1 , 1 , -1 , 1, -1]
dy = [-1 , 1 , 0 , 0 , 1 , -1 , -1 , 1]



def solver(matrix , i , j , row , col , currChar , vis):

    vis[(i,j)] = True
    retVal = 0

    for change in range(len(dx)):

        newX = i+dx[change]
        newY = j+dy[change]
        if not doesFit(newX , newY , row , col):
            continue
        if (newX , newY) in vis:
            if vis[(newX ,newY)]:
                continue

        if currChar == 'X' and matrix[newX][newY] == 'M':
            retVal += solver(matrix , newX , newY , row , col , 'M' , vis)
        elif currChar=='M' and matrix[newX][newY]=='A':
            retVal += solver(matrix, newX, newY, row, col, 'A', vis)
        elif currChar == 'A' and matrix[newX][newY]=='S':
            return 1

        return retVal





def main():
    matrix = []
    with open("input.txt") as file:
        currRow = []
        for line in file:
            currRow = []
            for ch in line.strip():
                currRow.append(ch)
            matrix.append(currRow)

    print(matrix)
    row = len(matrix)
    col = len(matrix[0])

    print('row is ' , row)
    print('col is ' , col)
    totVal = 0
    vis = {}
    for i in range(0 , row):
        for j in range(0 , col):
            if matrix[i][j] == 'X':
                for change in range(0 , len(dx)):
                    flag = True
                    newX = i
                    newY = j
                    for k in range(1 , 4):
                        newX += dx[change]
                        newY += dy[change]

                        if( not doesFit(newX , newY , row , col)):
                            flag = False
                            break
                        if(k == 1 and not matrix[newX][newY] =='M'):
                            flag = False
                            break
                        if(k == 2 and not matrix[newX][newY] =='A'):
                            flag = False
                            break
                        if (k == 3 and not matrix[newX][newY] == 'S'):
                            flag = False
                            break
                    if flag:
                        totVal += 1


    print(totVal)




if __name__ == '__main__':
    main()

