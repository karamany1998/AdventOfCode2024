def convertToBinary(num):
    bin = ''
    while num :
        bin = str(num%2)+bin
        num /=2
        num = int(num)
    while(len(bin) < 3):
        bin = '0'+bin
    return bin
def convertToDecimal(program):
    expo = 0
    tot = 0
    for i in reversed(program):
        tot += int(i) * (2**expo)
        expo+=1
    return tot
##function to get the "combo" operand
def getOperand(operand , regA , regB , regC) :
    currVal = 0
    if operand >= 0 and operand <= 3:
        currVal = operand
    elif operand == 4:
        currVal = regA
    elif operand == 5:
        currVal = regB
    elif operand == 6:
        currVal = regC
    return currVal

def main() -> int:
    ans = ''
    regA = 0
    regB = 0
    regC = 0
    candidateList = []

    with open('input.txt') as file:
        for line in file:
            if len(line.strip())==0:   ##skip empty lines
                continue

            currLine = line.strip().split(' ')
            program = ''
            ##assign registers
            if currLine[0]=='Register' and currLine[1][0]=='A' :
                regA = int(currLine[2])
                continue
            elif currLine[0] == 'Register' and currLine[1][0]=='B':
                regB = int(currLine[2])
                continue
            elif currLine[0] == 'Register' and currLine[1][0] == 'C':
                regC = int(currLine[2])
                continue
            ##start processing the input
            else:
                program = currLine[1].split(',')

            for idx in range(0, len(program) + 1):
                candidateList.append([])
            candidateList[0].append(' ')

            for idx in range(0 , len(program)):
                print('-------------------------------------------------')
                print('candidate list is ' , candidateList)
                print('idx: ', idx)

                print('current goal is ' , int(program[len(program)-idx-1] ))

                currProgram = program[len(program)-idx-1]

                for currList in candidateList[idx]:
                    ##candidate list idx holds all the previous candidates
                    curr = []

                    for shift in range(0, 8):

                        newRegB = shift ^ 3  ## we do instruction (1,3)
                        currProgram2 =  convertToBinary(shift ^ 2)

                        ##just do with current variable
                        if len(candidateList[idx]) == 0 :
                            currProgram2 = convertToBinary(shift ^ 2)
                            for j in range(0, shift):
                                currProgram2 = currProgram2[:-1]  ##otherwise shift to right "shift" times

                            newC_int = convertToDecimal(currProgram2)

                            out = newRegB ^ newC_int
                            out = out % 8
                            if out == int(program[len(program) - idx - 1]):
                                x = shift ^ 2  ## we do instruction (1,2)
                                newVal = convertToBinary(shift ^ 2)
                                if(newVal not in candidateList[idx+1]):
                                    candidateList[idx + 1].append(convertToBinary(shift ^ 2))
                        ##loop over
                        else:
                            currProgram2 = ''
                            for num in candidateList[idx]:
                                currProgram2 = num.strip() + convertToBinary(shift ^ 2)
                                for j in range(0, shift):
                                    currProgram2 = currProgram2[:-1]  ##otherwise shift to right "shift" times
                                newC_int = convertToDecimal(currProgram2)

                                out = newRegB ^ newC_int
                                out = out % 8
                                if out == int(program[len(program) - idx - 1]):
                                    x = shift ^ 2  ## we do instruction (1,2)
                                    newVal = num.strip() + convertToBinary(shift ^ 2)
                                    if(newVal not in candidateList[idx+1]):
                                        candidateList[idx+1].append( num.strip() + convertToBinary(shift ^ 2))

            print(min(candidateList[len(candidateList)-1]))
            lastList = candidateList[len(candidateList)-1]
            newList = []
            for elem in lastList:
                newList.append(convertToDecimal(elem))
            print(min(newList))

        return 0
if __name__ == "__main__":
    main()
