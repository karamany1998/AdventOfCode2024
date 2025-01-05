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
            ##save starting position, id and size
            fileList.append([currPos , id , num])

            currPos += num
            id+=1

        ##block size
        else:
            num = int(line[i])
            ##save starting index of free space and its size
            freeIdx.append([currPos , num])

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
        currList_ID = currList[1]
        currList_size = currList[2]

        freeStart = -1

        for j in range(0 , len(freeIdx)):
            if freeIdx[j][0] <= currList_Idx and freeIdx[j][1]>=currList_size:
                freeStart = j
                break

        if freeStart  == -1:
            continue

        #print('old free block.. ', freeIdx[freeStart])

        #print('new free block.. ' , freeIdx[freeStart])
        for j in range(freeIdx[freeStart][0] , freeIdx[freeStart][0] + currList_size):
            position[j] = currList_ID
        for j in range(currList_Idx , currList_Idx+currList_size):
            position[j] = 0
        #print('---------------------------------------------------------------------')
        freeIdx[freeStart] = [freeIdx[freeStart][0] + currList_size, freeIdx[freeStart][1] - currList_size]

    #print('---------------------------------------------------------------------')
    sortedDict = sorted_dict = dict(sorted(position.items()))

    tot = 0
    for idx, value in sortedDict.items():
        print(str(idx) + ' : ' + str(value))
        tot += idx*value




    print(tot)




if __name__=='__main__':
    main()