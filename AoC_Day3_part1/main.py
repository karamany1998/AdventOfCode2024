import re



def main():
    tot = 0
    with open("input.txt") as file:
        for line in file:
            ansList = re.findall(r'mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)' , line)
            for item in ansList:
                vals = re.findall(r'[0-9][0-9]?[0-9]?' , item)
                ##print('vals found ' , vals)
                mult = 1
                for x in vals:
                    mult *= int(x)

                tot += mult

    print(tot)




if __name__ == '__main__':
    main()