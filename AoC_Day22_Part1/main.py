from collections import defaultdict

def main():
    sumVal =0
    arr = []
    arr2 = []
    changeDict = defaultdict(int)
    with open('input.txt') as file:

        ##generate all the secret numbers and also have an array of secret numbers and an array of the associated
        ##changes
        for line in file:
            lst = line.strip().split('\n')
            num = int(lst[0])
            #print(num)
            currArr = [num%10]
            changeArr = []

            for i in range(0, 2000):
                num = ((num*64)^num)%16777216 ##first operation
                num = (int((num/32)) ^ num)%16777216 ##second operation
                num = ((num*2048)^num)%16777216

                currArr.append(num%10)
                changeArr.append(num%10 - currArr[i])
            arr.append(currArr)
            arr2.append(changeArr)
            sumVal += num


    ##build the possibleChange set and the changeDict dictionary to be able to process the input
    possibleChange = set()
    for i in range(0 , len(arr)): ##loop over all buyers
        currBuyerArr = arr[i]

        for j in range(4, len(currBuyerArr)):
            currChange = arr2[i][j-4 : j]
            searchVariable = (i , currChange[0] , currChange[1] , currChange[2] , currChange[3])
            if searchVariable not in changeDict:
                changeDict[(i , currChange[0] , currChange[1] , currChange[2] , currChange[3])]=currBuyerArr[j]
            possibleChange.add((currChange[0] , currChange[1] , currChange[2] , currChange[3]))

    mxVal = 0
    bestChange = (0, 0 , 0 , 0)
    for ch in possibleChange: ##loop over all possible changes
        #print('current change is ' , ch)
        currSum = 0
        for i in range(0 , len(arr)):  ##loop over all buyers and maximize over the changes

            searchVariable = (i ,ch[0] , ch[1] , ch[2] , ch[3])

            if searchVariable not in changeDict:
                continue

            currMx= changeDict[searchVariable]
            currSum += currMx

        mxVal = max(mxVal , currSum)

    print(mxVal)





if __name__=='__main__':
    main()