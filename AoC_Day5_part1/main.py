from email.policy import default
from collections import defaultdict

def main():
    previousElements = defaultdict(list)
    tot =0
    with open("input.txt") as file:

        for line in file:
            if len(line.strip()) == 0:
                continue

            if '|' in line:
                currInput = line.strip().split('|')
                print(currInput)
                previousElements[currInput[1]].append(currInput[0])

            ##check if in correct order
            else:
                flag = True
                currInput = line.strip().split(',')
                for i in range(1 , len(currInput)):
                    if not flag :
                        break
                    for j in range(0, i):

                        if currInput[i] in previousElements[currInput[j]]:
                            flag = False
                            break
                if flag:
                    mid = int(len(currInput)/2)
                    tot += int(currInput[mid])
    print(previousElements)
    print(tot)




if __name__=='__main__':
    main()
