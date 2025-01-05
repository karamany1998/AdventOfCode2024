from collections import defaultdict

dx = [0 , 0, -1 , 1]
dy = [-1 , 1 , 0 , 0 ]

cnt = 0
def dfs(graph , vis , i , j ):
    global cnt

    if int(graph[i][j]) == 9:
        cnt+=1
        print('FOUND at ' +str(i)+', '+str(j))
        return

    for ch in range(0 , 4):
        newX = i + dx[ch]
        newY = j + dy[ch]

        if vis[(newX , newY ,i , j)]:
            continue
        if newX>= len(graph) or newX<0 or newY>=len(graph[0]) or newY<0:
            continue

        if int(graph[newX][newY]) - int(graph[i][j]) ==1:
            vis[(newX , newY ,i ,j)] = True
            print('( '+str(i)+ ', '+str(j)+' ) --> ( '+str(newX)+' ,'+str(newY) +' )')
            dfs(graph , vis , newX , newY )
            vis[(newX, newY, i, j)] = False
    return


def main():
    line = ''
    graph = []
    with open('input.txt') as file:
        for line in file:
            #print('------------------------------------------')
            currLine = line
            if line[-1]=='\n':
                currLine = line[:-1]
            curr = list(currLine)
            graph.append(curr)
            #print(curr)

    #print(graph)

    for i in range(0 , len(graph)):
        for j in range(0 , len(graph[0])):
            if int(graph[i][j]) == 0:
                print('---------------------------------------------------')
                print('Another Traihead found at (' +str(i)+', '+str(j)+' )')
                vis = defaultdict(bool)
                vis[(i, j,i,j)] = True
                dfs(graph , vis , i , j )
                print(cnt)

    print(cnt)





if __name__=='__main__':
    main()