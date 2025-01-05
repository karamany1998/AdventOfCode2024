availableItems = set()
tot = 0

def solver(input_str, start, memo  ):

    global tot
    ##base cases
    ##we were able to construct a string from substrings, so return 1

    if start == len(input_str):
        ##tot += 1
        return 1


    retVal = 0

    if input_str[start:] in memo:
        retVal = memo[input_str[start:]]
    else:
        for x in availableItems:
            if input_str[start:].startswith(x):
                retVal += solver(input_str , start + len(x) , memo )

    memo[input_str[start:]] = retVal
    return retVal

def main():

    global tot
    with open("input.txt") as file:
        content = file.readlines()

    # Parse available patterns
    availableItems.clear()  # Clear any previous patterns
    patterns = content[0].strip().split(',')
    for pattern in patterns:
        availableItems.add(pattern.strip())

    # Process each design

    for idx, line in enumerate(content[2:], 2):
        if len(line.strip())==0 :
            continue
        design = line.strip()
        #
        memo = {}
        ans = solver(design, 0, memo )
        tot+=ans
        if ans :
            print(design)
            print('idx ' , idx)
            print('curr ans is ' , ans)
            print('-------------------------------------')


    print('final answer is ' , tot)


if __name__ == '__main__':
    main()
