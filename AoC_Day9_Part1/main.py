from collections import defaultdict

def main():
    line = ''
    with open('input.txt') as file:
        line = file.readline()

    position = defaultdict(int)
    currPos = 0
    freeIdx = []
    fileList = []
    id =0

    for i in range(0, len(line)):
        ##file size
        if line[i] == '\n':
            continue

        if i %2 ==0:

            num = int(line[i])
            for j in range(currPos , currPos + num):
                position[j] = id
                fileList.append([j , id])

            currPos += num
            id+=1

        ##block size
        else:
            num = int(line[i])
            for j in range(currPos , currPos + num):
                freeIdx.append(j)

            currPos += num

    print(freeIdx)
    print(fileList)

    for idx, value in position.items():
        print(str(idx) + ' : '+str(value))

    ##loop from back of list
    firstFreePos = 0
    for i in range(len(fileList)- 1 , -1 , -1):
        currList = fileList[i]
        currList_Idx = currList[0]
        currList_num = currList[1]

        if  currList_Idx <= freeIdx[firstFreePos]:
            break

        position[freeIdx[firstFreePos]] = currList_num
        position[currList_Idx] = 0 ##mark as empty
        freeIdx.append(currList_Idx)

        firstFreePos+=1

    print('---------------------------------------------------------------------')
    sortedDict = sorted_dict = dict(sorted(position.items()))

    tot = 0
    for idx, value in sortedDict.items():
        print(str(idx) + ' : ' + str(value))
        tot += idx*value




    print(tot)




if __name__=='__main__':
    main()