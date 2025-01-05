


def doesFit(i , j , row , col):
    if(i>= row or i<0 or j>= col or j<0):
        return False

    return True

dx = [0 , 0 , 1 , -1 , 1 , -1 , 1, -1]
dy = [-1 , 1 , 0 , 0 , 1 , -1 , -1 , 1]





def solver(matrix , row , col):

    retVal = 0

    for i in range(1, row-1):
        for j in range(1, col-1):
            if matrix[i][j] == 'A':
                if matrix[i-1][j-1]=='M' and matrix[i+1][j+1]=='S' and matrix[i+1][j-1]=='M' and matrix[i-1][j+1]=='S'\
                    or matrix[i-1][j-1]=='S' and matrix[i+1][j-1]=='M' and matrix[i+1][j+1]=='M' and matrix[i-1][j+1]=='S'\
                        or matrix[i-1][j-1]=='M' and matrix[i+1][j+1]=='S' and matrix[i-1][j+1]=='M' and matrix[i+1][j-1]=='S'\
                        or matrix[i-1][j-1]=='S' and matrix[i+1][j+1]=='M' and matrix[i+1][j-1]=='S' and matrix[i-1][j+1]=='M':
                    retVal+=1
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
    totVal = solver(matrix , row , col)


    print(totVal)




if __name__ == '__main__':
    main()

