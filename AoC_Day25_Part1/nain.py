

def calculate(matrix):

    currLst = []

    for j in range(0 , len(matrix[0])):
        cnt =0
        for i in range(0 , len(matrix)):
            if matrix[i][j] =='#':
                cnt+=1


        currLst.append(max(cnt-1 , 0 ))

    return currLst


def main():
    key_matrix = []
    lock_matrix=[]
    key_lst = []
    lock_lst = []
    flag = False
    isKey = False
    isLock = False
    with open("input.txt") as file:
        line = file.readline()
        while line:

            if len(line.strip())==0 :
                if isKey:
                    key_lst.append(calculate(key_matrix))
                else:
                    lock_lst.append(calculate(lock_matrix))

                key_matrix = []
                lock_matrix =[]

                isKey = False
                isLock = False

                line = file.readline()


            if line[0]=='.':
                isKey = True
                isLock = False
                currList = []

                while(len(line.strip()) != 0) :
                    currList = []
                    for x in line:
                        if x != '\n':
                            currList.append(x)
                    key_matrix.append(currList)

                    line = file.readline()


                continue

            else:
                isLock = True
                isKey = False
                currList = []
                while (len(line.strip()) != 0):
                    currList = []
                    for x in line:
                        if x != '\n':
                            currList.append(x)
                    lock_matrix.append(currList)

                    line = file.readline()
                continue

    sz = 0
    if isKey:
        key_lst.append(calculate(key_matrix))
        sz = len(key_matrix)-2
    else:
        lock_lst.append(calculate(lock_matrix))
        sz = len(lock_matrix)-2
    print(key_matrix)
    print(lock_matrix)

    print(key_lst)
    print(lock_lst)
    print(sz)
    cnt =0
    for list1 in key_lst:
        for list2 in lock_lst:
            flag = True

            for i in range(0 , len(list1)):
                if (list1[i] + list2[i]) > sz:
                    flag = False
                    break

            if flag:
                cnt+=1

    print(cnt)












if __name__=='__main__':
    main()