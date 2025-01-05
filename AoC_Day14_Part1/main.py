
from collections import defaultdict

def main():
    matrix =[]

    with open('input.txt') as file:
        positions = defaultdict(int)
        for line in file:
            currLine = line.strip().split(' ')
            position = currLine[0]
            velocity = currLine[1]

            posXY = position.strip().split(',')
            posX = int(posXY[0][2:])
            posY = int(posXY[1])

            velXY = velocity.strip().split(',')
            velX = int(velXY[0][2:])
            velY = int(velXY[1])

            for i in range(0 , 100):
                posX = (posX + velX)%101
                posY = (posY + velY)%103

            positions[(posX , posY)] +=1

    quadrant1 = 0
    quadrant2 = 0
    quadrant3 = 0
    quadrant4 = 0

    for pos, num in positions.items():
        if pos[0]<int(101/2) and pos[1]<int(103/2):
            quadrant1 += num
        elif pos[0]<int(101/2) and pos[1]>int(103/2):
            quadrant2+= num
        elif pos[0]>int(101/2) and pos[1]<int(103/2):
            quadrant3 += num
        elif pos[0]>int(101/2) and pos[1]>int(103/2):
            quadrant4+=num
    print(quadrant1)
    print(quadrant2)
    print(quadrant3)
    print(quadrant4)
    print(quadrant1*quadrant2*quadrant3*quadrant4)












if __name__=='__main__':
    main()