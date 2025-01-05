import re
def main():
    tot = 0
    with open("input.txt") as file:
        content = file.read().replace('\n', ' ')
        content = 'do' + content
        i = 0

        while i < len(content):
            print('total length of content: ', len(content))
            print('i equals ' , i )
            idx1 = content.find('do' , i)
            idx2 = content.find('don\'t' , i )

            flag = True
            while idx1 == idx2 and idx1!=-1 and idx2!=-1:
                flag = False
                i = idx2 + 4
                idx1 = content.find('do' , i)
                idx2 = content.find('don\'t', i)
                if(idx1 == -1):
                    break

            i = idx2 + 4

            print('idx1 equals ', idx1)
            print('idx2 equals ', idx2)


            ansList = re.findall(r'mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', content[idx1:idx2])

            for item in ansList:
                vals = re.findall(r'[0-9][0-9]?[0-9]?', item)
                ##print('vals found ' , vals)
                mult = 1
                for x in vals:
                    mult *= int(x)

                tot += mult
            print('curr Tot is ' , tot)
            print('-------------------------------------------------------------')

            if(idx1 == -1 or idx2 == -1):
                break

    print(tot)




if __name__ == '__main__':
    main()