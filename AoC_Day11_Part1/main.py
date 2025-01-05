

import sys

sys.set_int_max_str_digits(20000)

def main():

    currList = []

    with open('input.txt') as file:
        line = file.readline()
        currList = line.strip().split(' ')

    for blink in range(0 , 25):
        # Open a file in write mode
        with open('output.txt', 'w') as file:
            # Use print with file parameter to write to the file
            print(currList, file=file)
            print('\n' , file=file)

        lenList = len(currList)
        i = 0
        while i < lenList:

            if int(currList[i]) ==  0:
                currList[i] = '1'

            elif len(currList[i])%2 == 0 :

                #print('old length is ' , len(currList))
                sz = len(currList[i])

                firstHalf = int(currList[i][0:int(sz/2)])
                secondHalf = int(currList[i][int(sz/2) : ])

                currList[i] = str(firstHalf)
                currList.insert(i+1 , str(secondHalf))
                i = i+2
                lenList = len(currList)
                #print('new  length is ', len(currList))
                continue

            else:

                currList[i] = str(2024 * int(currList[i]))

            i+=1


    #print(currList)
    print(len(currList))

if __name__=='__main__':
    main()