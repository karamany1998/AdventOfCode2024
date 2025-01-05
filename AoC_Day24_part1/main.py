from collections import defaultdict

def main():
    tot = 0
    numZ =0
    constructNum = defaultdict(int)
    strToNum = defaultdict(int)
    isProcessed = defaultdict(bool)
    numRight = defaultdict(int)
    lst = []
    with open("input.txt") as file:

        for line in file:
            if(len(line.strip()) == 0):
                continue

            if ':' in line:
                curr = line.strip().split(' ')
                name = curr[0][0:-1]
                val = int(curr[1])
                isProcessed[name] = True
                strToNum[name] = val

            else:
                curr = line.strip().split(' ')
                lst.append([curr[0] , curr[1], curr[2] , curr[4]])
                numRight[curr[4]]+=1
                if(numRight[curr[4]] > 1):
                    print('found important number')

            #print('--------------------------------------------')
    #print('dict size is ' , len(strToNum))
    cnt = 0
    flag = True
    constructArray = []
    print(numRight)
    #print('numZ is ' , numZ)
    while flag :
        flag = False

        for expr in lst:
            if not isProcessed[expr[-1]]:
                if isProcessed[expr[0]] and isProcessed[expr[2]]:
                    #print('found candidate')
                    cnt+=1
                    isProcessed[expr[-1]] = True

                    if expr[-1][0] == 'z':
                        constructArray.append(expr[-1])

                    if expr[1]=='AND':
                        newVal = int(strToNum[expr[0]]) & int(strToNum[expr[2]])
                        strToNum[expr[-1]] = newVal

                    elif expr[1]=='OR':
                        newVal = int(strToNum[expr[0]]) | int(strToNum[expr[2]])
                        strToNum[expr[-1]] = newVal

                    elif expr[1]=='XOR':
                        newVal = int(strToNum[expr[0]]) ^ int(strToNum[expr[2]])
                        strToNum[expr[-1]] = newVal

                else:
                    flag = True

    tot = 0
    constructArray.sort()
    print('construct array: ', constructArray)
    for i in range(0 , len(constructArray)):
        print(strToNum[constructArray[i]])
        tot += (strToNum[constructArray[i]])*(2**i)
    print(tot)


if __name__=='__main__':

    main()